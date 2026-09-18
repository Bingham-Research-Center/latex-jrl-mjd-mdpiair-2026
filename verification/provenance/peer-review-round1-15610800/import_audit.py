from pathlib import Path
import csv
import hashlib
import json
import shutil
import subprocess

repo = Path.cwd()
source = Path(Path('/tmp/mdpiair-import-path').read_text())
handoff = source / 'layers/handoff'
returned = handoff / 'return'
closure = source / 'closure'
ref = '658bd005e20401f9ad8c8e88c5c2b506bb60e1a8'
receipt_dir = Path('verification/provenance/peer-review-round1-15610800')
receipt_path = Path('verification/provenance/reviewer-layer-import-15610800.json')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def rows(path):
    with Path(path).open(newline='') as stream:
        return list(csv.DictReader(stream))

inventory = {r['run_id']: r for r in rows('verification/provenance/run-inventory.csv')}
run_ids = {key: f'pelican_{forcing}_{feedback}_default_ysu_20130202'
           for key, forcing, feedback in [('gfs2','gfs','2way'), ('gfs1','gfs','1way'),
                                          ('nam2','nam','2way'), ('nam1','nam','1way')]}
stations = ['KVEL','QRS','QV4','USU01','USU02','USU03','USU04','USU05','USU07','USU08','UUT01']
generator = 'verification/scripts/analyze_wrf_retention.py'
generator_hash = hashlib.sha256(subprocess.check_output(['git','show',f'{ref}:{generator}'])).hexdigest()
baseline = {(r['pair'],r['metric']):r for r in rows('verification/data/retention_pair_summary.csv')}
wind = {(r['contrast'],r['metric']):r for r in rows('verification/data/reviewer_primary_wind_sensitivity.csv')}
summaries = []
for layer in ['50-500','50-250','100-500']:
    for step in [10,25,50]:
        key = f'{layer}_step-{step}'
        csv_path = Path(f'verification/data/reviewer_layer_{key}_pair_summary.csv')
        meta_path = Path(f'verification/provenance/reviewer_layer_{key}_metadata.json')
        meta = json.loads((returned/meta_path).read_text())
        assert meta['software']['generator']['sha256'] == generator_hash
        assert meta['inputs']['stations']['sha256'] == sha('verification/data/stations_2013_selection.csv')
        assert meta['stations'] == stations
        assert meta['window'] == {'start':'2013-02-02T14:00:00','end':'2013-02-02T18:00:00','n_hours':5}
        assert meta['inputs']['observations'] is None
        assert set(meta['runs']) == set(run_ids)
        bottom,top = map(int,layer.split('-'))
        assert meta['common_agl_m'] == list(range(bottom,top+1,step))
        for key_run,run in meta['runs'].items():
            assert run['run_dir'] == inventory[run_ids[key_run]]['archive_path']
            assert sorted(run['station_cells']) == stations
            assert [f['name'] for f in run['files']] == [f'wrfout_d02_2013-02-02_{hour}:00:00' for hour in range(14,19)]
        values = rows(returned/csv_path)
        assert len(values) == 10
        assert {(r['pair'],r['metric']) for r in values} == {
            (pair,metric) for pair in ['gfs2_minus_nam2','gfs1_minus_nam1']
            for metric in ['stability_k','transport_wind_ms','layer_mean_speed_ms','alignment_ratio','pblh_m']}
        for r in values:
            assert int(r['n_hours']) == 5 and int(r['n_stations_min']) == 11
            if r['metric'] == 'stability_k':
                assert int(r['negative_hours']) == 5 and float(r['hourly_maximum']) < 0
            if r['metric'] in ['transport_wind_ms','layer_mean_speed_ms']:
                assert int(r['positive_hours']) == 5 and float(r['hourly_minimum']) > 0
            if layer == '50-500' and step == 25:
                pair = (r['pair'],r['metric'])
                if pair in baseline:
                    for field in ['mean_hourly_spatial_median','hourly_minimum','hourly_maximum']:
                        assert abs(float(r[field])-float(baseline[pair][field])) < 1e-9
                if pair in wind:
                    assert abs(float(r['mean_hourly_spatial_median'])-float(wind[pair]['mean_of_hourly_paired_station_medians'])) < 1e-9
        summaries.append({'layer_m':layer,'step_m':step,'summary':str(csv_path),'metadata':str(meta_path),
                          'means':{r['pair']+' / '+r['metric']:float(r['mean_hourly_spatial_median']) for r in values},
                          'command':meta['command']})

for name,destination in [('diagnostic-numerical-checks.csv','verification/data'),
                         ('observation-evidence-summary.json','verification/provenance'),
                         ('USU04-metadata.json','verification/provenance'),
                         ('USU04-request-receipt.json','verification/provenance'),
                         ('inspected-original-files.sha256','verification/provenance')]:
    assert sha(closure/name) == sha(Path(destination)/name)

spread = max(max(s['means'][pair+' / '+metric] for s in summaries if s['layer_m']==layer)
             - min(s['means'][pair+' / '+metric] for s in summaries if s['layer_m']==layer)
             for layer in ['50-500','50-250','100-500']
             for pair in ['gfs2_minus_nam2','gfs1_minus_nam1']
             for metric in ['transport_wind_ms','layer_mean_speed_ms'])
assert spread < 0.02
receipt_dir.mkdir(parents=True,exist_ok=True)
imported = []
for path in sorted(returned.rglob('*')):
    if path.is_file():
        destination = path.relative_to(returned)
        assert not destination.exists(),destination
        shutil.copyfile(path,destination)
        imported.append(str(destination))
for name in ['submission.txt','sacct.txt','slurm.out','slurm.err','return_sha256.txt']:
    shutil.copyfile(handoff/name,receipt_dir/name)
    imported.append(str(receipt_dir/name))
shutil.copyfile(closure/'closure-files.sha256',receipt_dir/'closure-files.sha256')
shutil.copyfile(__file__,receipt_dir/'import_audit.py')
imported += [str(receipt_dir/'closure-files.sha256'),str(receipt_dir/'import_audit.py')]
receipt = {
 'source_commit':ref, 'import_base_commit':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
 'job_id':'15610800', 'job_state':'COMPLETED', 'job_exit_code':'0:0',
 'source_checkout':'/uufs/chpc.utah.edu/common/home/u0737349/gits/mdpi-air-review-layers-658bd00',
 'source_output_root':'/scratch/general/vast/u0737349/latex_jrl_review_layers/15610800',
 'archives':{name:sha(name) for name in ['latex_jrl_review_layers_15610800_handoff.tar.gz',
             'mdpiair-handoffs/peer-review-round1-chpc-closure-15610800.tar.gz']},
 'internal_hashes_verified':{'layers':19,'closure':12},
 'run_ids':run_ids, 'domain':'d02','stations':stations,
 'window_utc':{'start':'2013-02-02T14:00:00','end':'2013-02-02T18:00:00','n_hours':5},
 'generator_sha256':generator_hash, 'station_sha256':sha('verification/data/stations_2013_selection.csv'),
 'baseline_max_tolerance':1e-9, 'max_wind_mean_spread_over_increments_ms':spread,
 'configurations':summaries, 'imported_sha256':{name:sha(name) for name in imported},
 'local_audit_command':'python /tmp/import_mdpiair_return.py',
 'local_audit_source':str(receipt_dir/'import_audit.py'),
 'manuscript_locators':['sec:v3-common-agl','sec:v3-driving-response','tab:v3-layer-sensitivity',
                         'sec:v3-observed-context','sec:v3-disc-domains'],
 'limits':['CHPC plot inspection reports D1 label overlap/clipping in all nine diagnostics; no figure promoted.',
           'Hourly source tables and diagnostic plots remain on CHPC; local sign checks use hashed pair summaries.',
           'Observation searches are bounded; the provisional Roosevelt sounding starts outside the retained window.',
           'USU04 provider QC and metadata do not establish exposure or a causal mechanism.',
           'No WRF integration or scientific gate reopened.']}
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n')
manifest = Path('verification/data/manifest.csv')
fieldnames = list(rows(manifest)[0])
with manifest.open('a',newline='') as stream:
    writer = csv.DictWriter(stream,fieldnames=fieldnames,quoting=csv.QUOTE_ALL,lineterminator='\n')
    for index,s in enumerate(summaries,40):
        writer.writerow(dict(zip(fieldnames,[f'DATA{index}',s['summary'],'tracked reviewer layer sensitivity',
          'X6-X5; X10-X3; DATA01; archived d02 output','2013-02-02 14-18 UTC; 11 stations; five paired hourly medians',
          f'{generator}@{ref}; Slurm 15610800',str(receipt_path)+';'+s['metadata'],sha(s['summary']),'',
          'verified','reviewer sensitivity; main text and appendix table',
          f"{s['layer_m']} m AGL; {s['step_m']} m wind integration increment. All five paired hourly endpoint differences negative and scalar/vector speed differences positive; no transport or vertical validation claim."])))
print('Imported nine summaries, nine metadata files, run manifest and original receipts.')
print('Maximum paired wind-mean spread over integration increments:',spread,'m s-1')

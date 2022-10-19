#!/usr/bin/env python3
args = parse_arguments()

with open(args.json, 'r') as ijf:
    ijf_content = json.load(ijf)

# delete mad_qc-related fields
del ijf_content['calls']['rna.mad_qc']
del ijf_content['outputs']['rna.mad_qc.madQCmetrics']
del ijf_content['outputs']['rna.mad_qc.python_log']
del ijf_content['outputs']['rna.mad_qc.madQCplot']
del ijf_content['inputs']['mad_qc_disk']

with open(args.out_file, 'w') as ojf:
    json.dump(ijf_content, ojf, sort_keys = False, indent = 4)

print('Delete done!')

#!/usr/bin/env python3

'''
Delete the mad_qc-related fileds, because croo cannot work correctly for some reason, if mad_qc is run.
The only way that I can solve the bug is to delete the mad_qc-related filed.
'''

import json
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description = 'Delete mad_qc-related fields from metadata.json.')
    parser.add_argument('-j', '--json', metavar = 'JSON', type = str, required = True, help = 'input metadata.json file')
    parser.add_argument('-o', '--out_file', metavar = 'JSON', type = str, required = True, help = 'output revised metadata.json file')
    args = parser.parse_args()
    return args

def main():
    print('Start deleting ...')

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

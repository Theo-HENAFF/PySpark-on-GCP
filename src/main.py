# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:26:29 2019

@author: HENAFF
"""
import os, sys, argparse, pyspark, importlib

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')
        
parser = argparse.ArgumentParser()
parser.add_argument('--job', type=str, required=True)
parser.add_argument('--job-args', nargs='*')
args = parser.parse_args()
sc = pyspark.SparkContext(appName=args.job_name)
job_module = importlib.import_module('jobs.%s' % args.job)
job_module.analyze(sc, job_args)
#!/usr/bin/env bash
module load conda3
source activate moldyn
cd /home/_shared/_projects/gmx_template
jupyter nbconvert --ExecutePreprocessor.timeout=3600 --ExecutePreprocessor.kernel_name=python3 --to notebook --execute status.ipynb --output status.ipynb
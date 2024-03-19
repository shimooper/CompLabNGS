#!/bin/bash -x
#PBS -S /bin/bash
#PBS -q power-pupko
#PBS -o /groups/pupko/yairshimony/CompLabNGS/10-RNA2
#PBS -e /groups/pupko/yairshimony/CompLabNGS/10-RNA2
#PBS -N deseq
#PBS -r y
hostname
echo $PBS_JOBID

source ~/miniconda3/etc/profile.d/conda.sh
conda activate ngs
export PATH=$CONDA_PREFIX/bin:$PATH

cd /groups/pupko/yairshimony/CompLabNGS/10-RNA2
python de_analysis.py

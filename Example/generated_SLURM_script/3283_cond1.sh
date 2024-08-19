#!/bin/bash

# Assuming the first argument is FILES_DIR
FILES_DIR=$1$2
mkdir $FILES_DIR

#SBATCH --mem-per-cpu=6G
#SBATCH --cpus-per-task=16
#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --output=3283_cond1_res_%j.txt

# Execute the Python script using srun
srun python3 cond1.py $FILES_DIR $FILES_DIR/d2 $FILES_DIR/d1 2 0

if [ $? -eq 0 ]; then
    echo "0" >> "exit_code0_${SLURM_JOB_ID}.txt"
    exit 0
else
    echo "1" >> "exit_code1_${SLURM_JOB_ID}.txt"
    exit 1
fi

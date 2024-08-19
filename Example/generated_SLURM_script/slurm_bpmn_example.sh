#!/bin/bash

FILES_DIR=$(echo $RANDOM | md5sum | head -c 4)
FILES_DIR="OM2X5_$FILES_DIR"
job_id_3283=$(sbatch --parsable --dependency=afterany:$job_id_3031:$job_id_1373 3283_cond1.sh $FILES_DIR 74236)
job_id_2415=$(sbatch --parsable --dependency=afterany:$job_id_3031:$job_id_1373 2415_cond2.sh $FILES_DIR 74236)
job_id_4965=$(sbatch --parsable --dependency=afterok:$job_id_3283 4965_D.sh $FILES_DIR 74236)
job_id_8132=$(sbatch --parsable --dependency=afterany:$job_id_3072:$job_id_4965 8132_FEV__aff_iloop__F.sh $FILES_DIR 74236)
job_id_855=$(sbatch --parsable --dependency=afterok:$job_id_3283 855_D.sh $FILES_DIR 74236)
job_id_5493=$(sbatch --parsable --dependency=afterany:$job_id_855:$job_id_3072 5493_ojs__aff_iloop__F.sh $FILES_DIR 74236)
job_id_723=$(sbatch --parsable 723_A.sh $FILES_DIR 74236)
job_id_8359=$(sbatch --parsable --dependency=afterok:$job_id_5493,$job_id_8132 8359_G.sh $FILES_DIR 74236)
job_id_1373=$(sbatch --parsable --dependency=afterok:$job_id_723 1373_C.sh $FILES_DIR 74236)
job_id_3031=$(sbatch --parsable --dependency=afterok:$job_id_723 3031_B.sh $FILES_DIR 74236)
job_id_3072=$(sbatch --parsable --dependency=afterok:$job_id_2415 3072_E.sh $FILES_DIR 74236)

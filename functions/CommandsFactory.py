import config

def commands_content(run_command_file, sbatch_file_name):
    text1 = """#!/bin/bash

# Change mode of all files in the current directory to executable
chmod +x *

# Remove all files with the .log extension
rm -rf *.log
rm -rf *.txt

# Load Python module
module load Python/3.9.6

# Uninstall cvxopt
pip3 uninstall cvxopt -y

# Change mode of all files in the current directory to executable
chmod +x *

# Convert line endings from DOS to UNIX format for all files
dos2unix *

nohup ./squeue_logger.sh &

# Execute {0}
./{0}
""".format(sbatch_file_name)

    run_command_file.write(text1)

def create(run_command_filename, sbatch_file_name, should_be_uploaded_list):
    run_command_file_path = "{}/{}".format(config.bpmn.slurm_scripts_directory, run_command_filename)
    should_be_uploaded_list.add(run_command_file_path)
    run_command_file = open(run_command_file_path, 'w')
    commands_content(run_command_file, sbatch_file_name)
        
import os, sys
if getattr(sys, 'frozen', False):
    filedir = os.path.dirname(sys.executable)
elif __file__:
    filedir = os.path.dirname(os.path.abspath(__file__))

if getattr(sys, 'frozen', False):
    basedir = os.path.dirname(os.path.dirname(sys.executable))
elif __file__:
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from flask import Blueprint, request
from http import HTTPStatus
from server.response import response_json
from server.error_messages import messages
from functions import storageprocessor, SLURMprocessor, SRunFactory_new, SBatchFactory, graphObject
import pm4py
import random
import string
import shutil
import config

# Set up file and base directories
filedir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
basedir = os.path.dirname(os.path.dirname(filedir))

slurm_script_manager = Blueprint('slurm_script_manager', __name__)

@slurm_script_manager.route("/generate_slurm_script_from_files", methods=["POST"])
def generate_slurm_script_from_files():
    try:
        if request.files:
            storageprocessor.remove_dir(config.bpmn.slurm_scripts_directory)
            graphObject.JOB.remove_all_jobs()
            files = request.files

            if 'bpmn_file' in files:
                bpmn_file = files["bpmn_file"]
                bpmn_file_path = storageprocessor.save_file(bpmn_file, config.bpmn.slurm_scripts_directory)
                
                preprocessed_bpmn = SLURMprocessor.preprocessing_bpmn(bpmn_file_path)
                processed_bpmn = SLURMprocessor.postprocessing_bpmn(preprocessed_bpmn)

                net, im, fm = pm4py.convert_to_petri_net(processed_bpmn)
                pm4py.view_petri_net(net, im, fm)

                depend_script, should_be_uploaded_list = graphObject.create(net, im, fm, processed_bpmn)
                SRunFactory_new.create(should_be_uploaded_list)

                sbatch_file_name = f"{bpmn_file.filename.split('.')[0]}.sh"
                sbatch_file_path = os.path.join(config.bpmn.slurm_scripts_directory, sbatch_file_name)
                should_be_uploaded_list.add(sbatch_file_path)

                with open(sbatch_file_path, 'w') as sbatch_file:
                    main_CI = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
                    SBatchFactory.create(sbatch_file, main_CI)

                return response_json({"msg": messages["success"], "slurmDAG": ""}, HTTPStatus.OK)

            return response_json({"error": messages["required_files_not_found"]}, HTTPStatus.NOT_FOUND)

        return response_json({"error": messages["required_files_not_found"]}, HTTPStatus.NOT_FOUND)

    except Exception as e:
        print(e)
        return response_json({"error": messages["server_side_error"]}, HTTPStatus.INTERNAL_SERVER_ERROR)

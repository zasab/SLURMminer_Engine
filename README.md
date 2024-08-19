# SLURMminer_Engine

An automated tool for converting BPMN diagrams to SLURM-ready scripts using Python and Bootstrap.

## Getting Started

Follow these steps to set up and run the SLURMminer_Engine on your system.

### 1. Installation Procedure

To set up SLURMminer_Engine:

- **Install Node.js:**
    - Download the Node.js installer from the [official website](https://nodejs.org/en/download/).
    - Follow the installation instructions, ensuring both Node.js and NPM (Node Package Manager) are installed.
    - Verify the installation by opening a command prompt (or PowerShell) and running:
      ```bash
      node -v
      ```

- **Verify Python Installation:**
    - Ensure Python is installed on your system by running:
      ```bash
      python --version
      ```

- **Check for PIP:**
    - Confirm that PIP, the Python package manager, is installed by running:
      ```bash
      pip --version
      ```

- **Clone the Repository:**
    - Clone the SLURMminer_Engine repository from GitHub:
      ```bash
      git clone https://github.com/zasab/SLURMminer_Engine.git
      ```
    - Open the project in your preferred Integrated Development Environment (IDE).

### 2. Execution Procedure

To run SLURMminer_Engine, follow these steps:

1. **Install Required Packages:**
    - Run the `app.py` script. Then, install the necessary packages listed in the `requirements.txt` file using:
      ```bash
      pip install flask matplotlib networkx pm4py==2.3.3
      ```

2. **Update `pm4py` Package Files:**
    - Replace the following files in the `pm4py` package with the custom versions provided:
        - **File to Update:**  
          `\pm4py\objects\bpmn\importer\variants\lxml.py`  
          **Replace With:**
          [`/custom_pm4py/lxml.py`](./custom_pm4py/lxml.py)

        - **File to Update:**  
          `\pm4py\objects\bpmn\obj.py`  
          **Replace With:**
          [`/custom_pm4py/obj.py`](./custom_pm4py/obj.py)

   Make sure to update these files to ensure compatibility and proper functionality.

3. **Run the Application:**
    - Execute the `app.py` script:
      ```bash
      python app.py
      ```
    - You should see the following output:
      ```plaintext
      * Serving Flask app 'app'
      * Debug mode: on
      WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
      * Running on http://127.0.0.1:5000
      Press CTRL+C to quit
      * Restarting with stat
      ```

    - Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000). Here, you can upload your input SlurmBPMN file, and the tool will generate the corresponding SLURM scripts in a newly created folder named `slurm_scripts`.


## Example

This section demonstrates how SLURMminer_Engine can be used to convert SlurmBPMN diagrams into SLURM scripts. A SlurmBPMN diagram is a type of customized BPMN that includes all the necessary information for executing a workflow on SLURM. To create and visualize an input SlurmBPMN diagram, you can use the [bpmn.io](https://demo.bpmn.io/new) online tool. This tool allows you to easily draw BPMN diagrams, which can then be customized to serve as input for SLURMminer_Engine.

### Example SlurmBPMN Diagram

Below is a sample SlurmBPMN diagram that represents a simple workflow (the BPMN file is available here: ![Sample SlurmBPMN Diagram](./Example/slurm_bpmn_example.bpmn)):

![Sample SlurmBPMN Diagram](./Example/slurm_bpmn_example.png)

The SlurmBPMN model outlines the steps for analyzing sorting algorithms. It starts with selecting a sorting algorithm, followed by generating data and implementing the algorithm. The implementation is refined through repeated tasks. An XOR gateway then uses scripts (`Cond1.py` and `Cond2.py`) to determine the next step based on data size. Large datasets trigger the "Run First Experiment," while smaller ones lead to the "Run Second Experiment." Data is collected, and the results are analyzed to provide insights into the algorithm's efficiency. Each task is linked to a script executed with the `srun` command on SLURM.
    
| Label   | Name                                               |
|---------|----------------------------------------------------|
| $A.py$  | Selection of Sorting Algorithm                     |
| $B.py$  | Generate Data                                      |
| $C.py$  | Implement Algorithm                                |
| $d_1$   | Data dependency between $A.py$ and $C.py$          |
| $d_2$   | Data dependency between $B.py$, $D.py$, and $E.py$ |
| Cond1.py | Script for assessing data size condition 1        |
| Cond2.py | Script for assessing data size condition 2        |
| $D.py$  | Run First Experiment                               |
| $E.py$  | Run Second Experiment                              |
| $d_3$   | Data dependency between $D.py$ and $F.py$          |
| $d_4$   | Data dependency between $E.py$ and $F.py$          |
| $F.py$  | Collect Data                                       |
| $d_5$   | Data dependency between $F.py$ and $G.py$          |
| $G.py$  | Analysis of Results                                |

This example highlights three important decision structures:

1. **Condition-Based Execution:** Scripts like `Cond1.py` run on SLURM to check certain conditions. If the script returns a 0, the workflow continues.
2. **Explicit Loops:** Tasks like `C.py` can repeat a specified number of times, such as 1 or 2, ensuring that `C.py` is executed in sequence for the chosen number of repetitions.
3. **Implicit Loops:** Tasks like `D.py` can run with different inputs (e.g., thresholds 0.2 and 0.8) simultaneously, ensuring that all variations are processed in parallel.

### Generated SLURM Script

After uploading the SlurmBPMN file, click the 'Create Executable File' button to generate the output SLURM scripts. The tool generates a SLURM script that automates the workflow on a cluster environment:

![Generated SLURM Script](path/to/your/image2.png)

In this example, the SlurmBPMN diagram is converted into a SLURM script, ready to be executed on a SLURM-managed HPC cluster.



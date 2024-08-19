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

This section demonstrates how SLURMminer_Engine can be used to convert BPMN diagrams into SLURM scripts. To create and see input BPMN diagram, you can use the [bpmn.io](https://demo.bpmn.io/new) online tool. This tool allows you to easily draw BPMN diagrams that can be used as input for SLURMminer_Engine.

### Example BPMN Diagram

Below is a sample BPMN diagram that represents a simple workflow:

![Sample SlurmBPMN Diagram](slurm_bpmn_example.bpmn)

### Generated SLURM Script

After uploading the BPMN diagram to SLURMminer_Engine, the tool generates a SLURM script that automates the workflow on a cluster environment:

![Generated SLURM Script](path/to/your/image2.png)

In this example, the BPMN diagram is converted into a SLURM script, ready to be executed on a SLURM-managed HPC cluster.


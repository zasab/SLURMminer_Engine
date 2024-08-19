# SLURMminer_Engine

An automated tool for converting BPMN diagrams to SLURM-ready scripts using Python and Bootstrap.

## How to Get Started

### 1. Installation Procedure

To set up the SLURMminer_Engine on your system, follow these steps:

- **Install Node.js:**
    - Download the Node.js installer from the [official website](https://nodejs.org/en/download/).
    - Follow the installation instructions, ensuring both Node.js and NPM (Node Package Manager) are installed.
    - Verify the installation by opening a command prompt (or PowerShell) and running the following command:
      ```bash
      node -v
      ```

- **Verify Python Installation:**
    - Ensure that Python is installed on your system. You can verify this by running:
      ```bash
      python --version
      ```

- **Check for PIP:**
    - Confirm that PIP, the Python package manager, is installed by running:
      ```bash
      pip --version
      ```

- **Clone the Repository:**
    - Clone the SLURMminer_Engine repository from GitHub using the following command:
      ```bash
      git clone https://github.com/zasab/SLURMminer_Engine.git
      ```
    - Open the project in your preferred Integrated Development Environment (IDE).

### 2. Execution Procedure

To run the SLURMminer_Engine, follow these steps:

1. **Install Required Packages:**
    - Run the `app.py` script. Then, use the `pip install` command to install all necessary packages. Some package requirements are listed in the `requirements.txt` file.
    - Install the primary dependencies by running:
      ```bash
      pip install flask matplotlib networkx pm4py==2.3.3
      ```

2. **Update `pm4py` Package Files:**
    - Replace the following files in the `pm4py` package with the custom versions provided:
        - **File to Update:**  
          `\pm4py\objects\bpmn\importer\variants\lxml.py`  
          **New File Location:**  
          `/custom_pm4py/lxml.py`

        - **File to Update:**  
          `\pm4py\objects\bpmn\obj.py`  
          **New File Location:**  
          `/custom_pm4py/obj.py`

   Ensure these files are updated to maintain compatibility and proper functionality.

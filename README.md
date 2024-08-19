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
          `/custom_pm4py/lxml.py`

        - **File to Update:**  
          `\pm4py\objects\bpmn\obj.py`  
          **Replace With:**  
          `/custom_pm4py/obj.py`

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

    - Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000). Here, you can upload your input SlurmBPMN file, and the tool will generate the corresponding SLURM scripts.

---

This version organizes the information in a clear, structured manner, making it easier to follow the installation and execution procedures. The use of bullet points, code blocks, and links enhances readability and usability, ensuring that users can quickly get started with SLURMminer_Engine.

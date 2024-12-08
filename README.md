# Log Analysis Script

## Overview
The project focuses on assessing our ability to write a Python script that processes log files to extract and analyze key information. This assignment evaluates proficiency in file handling, string manipulation, and data analysis, which are essential skills for cybersecurity-related programming tasks.


## Setup and Usage
Instructions to run the repository locally.
1. Clone the repository:
   ```bash
   git clone https://github.com/aranya-jana/Log-Analysis-Script.git
   ```
1. Install dependencies:
   No Extra Dependencies are required. You just need to create or store a `sample.log` file and store your logs in it.
   For example,
   ```bash
   192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
    203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
    ```
1. Run the project:
    - On Windows
    ```bash
    python main.py
    ```
    - On Mac
    ```bash
    python3 main.py
    ```

## File Description
```
repository_directory/
├── main.py
├── log_analysis_results.csv
├── .gitignore
└── README.md
```
The Results are stored in the `log_analysis_results.csv` file.
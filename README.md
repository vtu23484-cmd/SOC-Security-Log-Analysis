# SOC Security Log Analysis

A beginner-friendly cybersecurity project that analyzes synthetic authentication logs to identify repeated failed login attempts and summarize potentially suspicious activity.

## Project Overview

This project simulates a basic Security Operations Center (SOC) log-triage task. A Python script processes authentication records, counts successful and failed logins, and highlights source IP addresses and user accounts with repeated failures.

**Note:** This project uses synthetic training data. It does not monitor live systems or prove that an attack occurred.

## Objectives

* Analyze authentication log records using Python.
* Count successful and failed login attempts.
* Identify IP addresses with three or more failed attempts.
* Identify user accounts with three or more failed attempts.
* Generate a readable analysis report.

## Tools and Technologies

* Python
* Git and GitHub
* CSV-style log processing
* Windows Command Prompt

## Project Structure

```text
SOC-Security-Log-Analysis/
├── analyze_logs.py
├── README.md
├── sample_logs/
│   └── auth.log
├── reports/
│   └── analysis_report.txt
└── screenshots/
```

## How to Run

1. Install Python 3 if it is not already installed.
2. Clone or download this repository.
3. Open Command Prompt in the project directory.
4. Run the script:

```bash
py analyze_logs.py
```

The analysis report is saved to `reports/analysis_report.txt`.

## Sample Results

The current synthetic dataset contains eight records.

| Metric                  | Result |
| ----------------------- | -----: |
| Total records processed |      8 |
| Successful logins       |      2 |
| Failed logins           |      6 |
| Invalid records         |      0 |

The script identifies two source IP addresses and two user accounts with at least three failed login attempts in this sample dataset.

Repeated failures may warrant further investigation, but they do not by themselves confirm malicious activity.

## Skills Practiced

* Basic Python scripting
* Authentication log analysis
* Failed-login pattern identification
* Security event triage fundamentals
* Report generation
* Git and GitHub version control

## Limitations

* Uses synthetic training records, not live security logs.
* Applies a simple threshold of three or more failed attempts.
* Does not perform real-time monitoring, threat attribution, or automated incident response.

## Future Improvements

* Add timestamps and time-window analysis.
* Support larger log files and malformed records.
* Add configurable detection thresholds.
* Create visual summaries of login activity.
* Practice investigating events using a SIEM platform such as Splunk.

## Author

**Lakshman Prasad**
Aspiring SOC Analyst | Cybersecurity

GitHub: https://github.com/vtu23484-cmd

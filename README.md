\# SOC Security Log Analysis



A beginner cybersecurity project that analyzes synthetic authentication logs using Python and identifies repeated failed login attempts.



\## Project Overview



This project demonstrates basic security log analysis for a Security Operations Center (SOC) learning environment. The script reads authentication records, counts successful and failed logins, identifies source IP addresses and usernames with repeated failures, and generates a text report.



\## Objectives



\* Practice analyzing authentication logs.

\* Identify repeated failed login attempts.

\* Summarize security events using Python.

\* Generate a report to support further investigation.



\## Technologies Used



\* Python

\* CSV parsing

\* `collections.Counter`

\* Windows Command Prompt



\## Project Structure



```text

SOC-Security-Log-Analysis/

├── analyze\_logs.py

├── sample\_logs/

│   └── auth.log

├── reports/

│   └── analysis\_report.txt

└── README.md

```



\## How to Run



1\. Install Python 3.

2\. Open Command Prompt in the project directory.

3\. Run the analysis script:



```bash

py analyze\_logs.py

```



The generated report is saved to `reports/analysis\_report.txt`.



\## Sample Results



The current synthetic dataset contains eight records.



\* Records processed: 8

\* Successful logins: 2

\* Failed logins: 6

\* Invalid records: 0

\* Source IPs with at least three failed attempts: 2

\* Usernames with at least three failed attempts: 2



These results describe the supplied sample data only. They are not findings from a live system.



\## Investigation Notes



Repeated authentication failures can warrant further investigation. However, this simple threshold-based script does not establish whether activity is malicious and does not perform real-time monitoring.



\## Limitations



\* Uses synthetic sample records rather than live security events.

\* Uses a fixed threshold of three failed attempts.

\* Does not correlate events across time windows.

\* Does not automatically block IP addresses or respond to incidents.



\## Future Improvements



\* Add automated tests and malformed-record test cases.

\* Support configurable thresholds.

\* Add time-window-based detection.

\* Explore analysis of exported Windows Security event logs.

\* Improve report formatting and visualization.



\## Disclaimer



This project is intended for educational purposes and uses synthetic training data.




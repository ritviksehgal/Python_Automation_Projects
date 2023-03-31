# Python Project - VirusTotal

In this project, I develop a security automation script for a very common task among Security Operations Analysts- using VirusTotal to detect malicious content as well as
false positives/ harmless content.

In today's ever- changing Threat landscape, endpoint security is becoming more commonplace within Cyber Security teams across industries. As a result, it is increasingly important to monitor endpoint devices in real- time to detect malicious/ suspicious processes and filter through network statistics of a local machine.

For simplicity, this project is broken up into two python scripts.

First, we have to extract real- time data from the endpoint detailing the processes running on the machine as well as the corresponding hash digest (displayed as MD5). Furthermore, the output is filtered by memory utilization. Often, threat actors, attempt to deploy executables commonly in an attempt to steal resources like memory from the host machine to run malicious programs in the background or carry out high- bandwidth activities like data exfiltration.

By running the script "get_real_time_data.py", we are able to obtain this information and save the output to an excel workbook called "All_process_hash_real_time.xlsx". For recordkeeping purposes, the current date and time are also in the filename.

In the second step, this information is then sent to VirusTotal for malware analysis via the VirusTotal API (Application programming interface). Here, the VirusTotal API reads the processes hash values from the excel sheet and returns the secure score. If the two or more antivirus software on VirusTotal output a result of "malicious" in response to an analysis, the file is determined to be malicious and result is written to a test file (.txt)

The output is written to the file "vt_results.txt". The following are examples of output:

1. process_name.exe - malicious
2. process_name.exe - Not malicious
3. "The secure score is not found" (if the MD5 hash digest is not found in the VirusTotal database)

These results can be very can be very useful to teams responsible to detecting malware and defining IOCs (Indicators of Compromise) for activities such as threat hunting. Also, these security automation scripts can relieve network monitoring team of manual tasks, effectively saving time and labor hours.

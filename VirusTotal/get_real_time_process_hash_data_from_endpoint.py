import xlsxwriter
import psutil
import hashlib
from datetime import datetime

# Create a new Excel file
filename = 'All_process_hash_real_time' + '.xlsx'
#+ datetime.now().strftime('%Y-%m-%d-%H-%M-%S') 
workbook = xlsxwriter.Workbook(filename)

# Add a new worksheet to the file
worksheet = workbook.add_worksheet()

# Get a list of all running processes
processes = psutil.process_iter()
# Sort the processes by highest memory utilization
processes = sorted(processes, key=lambda proc: proc.memory_info().rss, reverse=True)

# Iterate over the sorted processes
for i, proc in enumerate(processes):
    try:
        # Get the process name and calculate its hash
        process_name = proc.name()
        hash_object = hashlib.md5(process_name.encode())
        process_hash = hash_object.hexdigest()

        # Write the process name and hash to the worksheet
        worksheet.write(i, 0, process_name)
        worksheet.write(i, 1, process_hash)
    except Exception:
        pass

# Save the workbook
workbook.close()

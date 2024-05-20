from datetime import datetime

### Write the file name
import os
from datetime import datetime

# Using the format YYYYMMDD_HHMMSS
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"backup_{current_time}.txt"

# Save the file
with open(file_name, 'w') as file:
    file.write("This is a backup file.")

print(f"File saved as {file_name}")

#################
## Date Formats
#################
#YYYY-MM-DD
date_format_1 = datetime.now().strftime("%Y-%m-%d")
print(date_format_1)

# YYYYMMDD
date_format_2 = datetime.now().strftime("%Y%m%d")
print(date_format_2)

# DD-MM-YYYY
date_format_3 = datetime.now().strftime("%d-%m-%Y")
print(date_format_3)

# Month Day, Year
date_format_5 = datetime.now().strftime("%B %d, %Y")
print(date_format_5)

#################
## Time Format
#################
# HH:MM:SS
time_format_1 = datetime.now().strftime("%H:%M:%S")
print(time_format_1)

##################################
## Date and Time Combined Formats
##################################

# YYYY-MM-DD_HH-MM-SS
datetime_format_1 = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(datetime_format_1)

# DD-MM-YYYY_HH-MM-SS
datetime_format_3 = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
print(datetime_format_3)

# YYYYMMDD_HHMMSS
datetime_format_2 = datetime.now().strftime("%Y%m%d_%H%M%S")
print(datetime_format_2)

# DDMMYYYY_HHMMSS
datetime_format_4 = datetime.now().strftime("%d%m%Y_%H%M%S")
print(datetime_format_4)

# Month Day, Year Hour:Minute:Second
datetime_format_7 = datetime.now().strftime("%B %d, %Y %H:%M:%S")
print(datetime_format_7)

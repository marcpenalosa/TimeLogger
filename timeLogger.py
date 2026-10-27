# author: Marc Penalosa
# filename: timeLogger.py

# the purpose of this program is to accurately log the time I've spent doing work, research, or anything related to my OIT Junior Project

# imports
from datetime import datetime
from pathlib import Path

# get the current time
now = datetime.now()
print(now.date())
print(now.time())

# wait until logging starts
# start logging at this time
start = datetime.now()

# see if there's a folder that already exist for this date
path_string = "./logs/" + now.strftime("%Y-%m-%d")
dir_path = Path(path_string)
dir_path.mkdir(parents=True, exist_ok=True)

print("Your input:", end=" ")
str_var = input()

# some time has passed
end = datetime.now()
elapsedTime = end - start
print(elapsedTime)

# what happens if we quit prematurely
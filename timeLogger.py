# author: Marc Penalosa
# filename: timeLogger.py

# the purpose of this program is to accurately log the time I've spent doing work, research, or anything related to my OIT Junior Project

# imports
from datetime import datetime
from pathlib import Path

def main():
    # get the current time
    now = datetime.now()
    print(now.date())
    print(now.time())

    start = datetime.now()

    # create a logs folder if there isn't one already
    path_string = "./logs/" + now.strftime("%Y-%m-%d")
    dir_path = Path(path_string)
    dir_path.mkdir(parents=True, exist_ok=True)

    print(parse_string())

    # some time has passed
    end = datetime.now()
    elapsedTime = end - start
    print(elapsedTime)

    return 0

# Purpose:
#   read string input
# Precondition:
#   N/A
# Postcondition:
#   returns an int as exit status
def parse_string():
    str_input = input()

    # splits the input into 2 parts
    # [0] = command input
    # [1] = rest of the string
    parsed_input = str_input.split(maxsplit=1)

    match(parsed_input[0]):
        case "--note" | "--n":
            print("note command")
            return 0
        case _:
            return 1

main()

# what happens if we quit prematurely
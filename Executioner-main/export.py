
# Purpose of this script: 
# export the data from the json files to a csv file. 


import csv
import json
from glob import glob

LOG_FOLDER = "logs"
LOG_GLOB = LOG_FOLDER + "/*/*/*/*.json"
DEFAULT_SAVE_LOCATION = "results.csv"
FIELDS = [
    "agent",
    "domain",
    "problem",
    "learning",
    "success",
    "cpu-time",
    "wall-time",
    "stderr",
    "actions",
    "perception-requests",
    "terminated",
]


def main(): # uses glob to iterate over all *.json files in all subdirectories
    
    csv_path = input( # for command line interface
        "This is the CSV log exporter. Currently it exports to "
        + DEFAULT_SAVE_LOCATION
        + ". Press enter to continue or type here an alternative saving file: "
    )
    writer = csv.writer(open(csv_path if csv_path else DEFAULT_SAVE_LOCATION, "w"))

    # add predefined fields to the CSV table 
    writer.writerow(FIELDS)

    # iterate over all *.json files in the logs folder
    for file_path in glob(LOG_GLOB):
        try:
            with open(file_path) as problem_run:
                data = json.loads(problem_run.read())
                # data is the json string of the current file

            # now the data will be written into a row in the CSV file
            writer.writerow([data[field] for field in FIELDS])
        except json.JSONDecodeError:
            pass


if __name__ == "__main__":
    main()

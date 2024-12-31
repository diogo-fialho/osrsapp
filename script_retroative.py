
import datetime
import os
import csv

def load_values():

    # load from csv files
    files_directory = 'C:\\Users\\diogo\\OneDrive\\Osrs_exp\\'
    # insert values in mongodb in pi
    result = []

    for x in os.listdir(files_directory):
        if x.endswith(".csv"):
            with open(files_directory + x, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                for row in spamreader:
                    if row[0] != "Date":
                        result.append({
                            'player': 'kingracado',
                            'name': x.replace('_experiences.csv', ''),
                            'level': int(row[2]),
                            'experience': int(row[1]),
                            'type': 'skill',
                            'request_date': datetime.datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S")
                        })

    return result
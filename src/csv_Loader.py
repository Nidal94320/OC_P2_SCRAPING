import csv
import datetime

""" getting timestamp """

timestamp = "_" + str(datetime.datetime.now())[0:16].replace(" ", "_").replace(":", "h")

""" Load a list into a csv file """

def csv_Loader(books_data):
    output_csv = "./data/" + "output" + timestamp + ".csv"
    with open(output_csv, "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=",")
        for line in books_data:
            writer.writerow(line)


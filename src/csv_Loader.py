import csv

""" Load a list into a csv file """


def csv_Loader(HEADER, book):
    output_csv = "./data/" + book[1] + "_data.csv"
    data_csv = []
    data_csv.append(HEADER)
    data_csv.append(book)
    with open(output_csv, "w") as f:
        writer = csv.writer(f, delimiter=",")
        for line in data_csv:
            writer.writerow(line)

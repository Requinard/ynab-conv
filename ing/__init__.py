import csv


def transform(input, output):
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    is_start = True

    for row in spamreader:
        if is_start:
            is_start = False
            continue
        new_row = []

        # Add date time
        year = row[0][:4]
        month = row[0][4:6]
        day = row[0][6:8]
        new_row.append("{0}/{1}/{2}".format(day, month, year))


        # Add payee
        new_row.append(row[1])

        # Category
        new_row.append(row[4])

        # Memo
        new_row.append(row[8])

        if(row[5] == "Af"):
            new_row.append(row[6])
            new_row.append(" ")
        else:
            new_row.append(" ")
            new_row.append(row[6])

        output_file.append(new_row)
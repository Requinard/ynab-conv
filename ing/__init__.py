import util


def transform(input, output):
    is_start = True

    for row in input:
        if is_start:
            is_start = False
            continue
        new_row = []

        year = row[0][:4]
        month = row[0][4:6]
        day = row[0][6:8]
        datetime = "{0}/{1}/{2}".format(day, month, year)

        if (row[5] == "Af"):
            new_row = util.format_output(datetime, row[1], row[4], row[8], row[6], " ")
        else:
            new_row = util.format_output(datetime, row[1], row[4], row[8], " ", row[6])

        output.append(new_row)

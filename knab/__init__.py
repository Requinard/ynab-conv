import util

def transform(input, output):
    line = 0

    for row in input:
        if line <= 1:
            line += 1
            continue

        new_row = []

        if(row[3] == '"D"'):
            new_row = util.format_output(row[1], row[6], row[8], row[9], row[4], " ")
        else:
            new_row = util.format_output(row[1], row[6], row[8], row[9], " ", row[4])

        output.append(new_row)



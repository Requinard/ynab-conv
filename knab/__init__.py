def transform(input, output):
    line = 0

    for row in input:
        if line <= 1:
            line += 1
            continue

        new_row = []

        # Add date
        new_row.append(row[1])

        # Add payee
        new_row.append(row[6])

        # Add category
        new_row.append(row[8])

        # Add memo
        new_row.append(row[9])

        # Add payment

        # C is bij, D is af
        if(row[3] == '"D"'):
            new_row.append(row[4])
            new_row.append(" ")
        else:
            new_row.append(" ")
            new_row.append(row[4])

        output.append(new_row)



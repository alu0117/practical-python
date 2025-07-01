# fileparse.py
#
# Exercise 3.3
import csv
def parse_csv(filename, select = None):
    '''
    Parse a CSV file into a list of record
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        headers = next(rows)
        indices = list(range(len(headers))) #default indices if no selection 
        if select:
            indices = [headers.index(s) for s in select]
        else:
            select = headers

        records = []
        for row in rows:
            if not row: #Skip rows with no data
                continue
            record = {col:row[ndx] for col,ndx in zip(select,indices)}
            records.append(record)
    return records
 
#!/usr/bin/python

def convert_data(file_name):
    fp = open('poker-hand-testing.data', 'r')
    
    for row in fp.readlines():
        row_modified = row.replace('\r\n', '')
        print row_modified.split(',')
    fp.close()

if __name__ == "__main__":
    convert_data('poker-hand-testing.data')
    convert_data('poker-hand-training-true.data')

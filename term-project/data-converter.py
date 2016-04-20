#!/usr/bin/python
import io

def convert_data(file_name, dest_name):
    fp = open(file_name, "r")
    modified_csv = ""
    
    for row in fp.readlines():
        row_modified = row.replace("\r\n", "").split(",")

        # S1 Suit of Card 1 
        if row_modified[0] == "1":
            modified_csv += "0,0,"
        elif row_modified[0] == "2":
            modified_csv += "0,1,"
        elif row_modified[0] == "3":
            modified_csv += "1,0,"
        elif row_modified[0] == "4":
            modified_csv += "1,1,"
        else:
            modified_csv += "ERROR,ERROR,"

        # C1 Rank of card 1
        if row_modified[1] == "1":
            modified_csv += "0,0,0,0,"
        elif row_modified[1] == "2":
            modified_csv += "0,0,0,1,"
        elif row_modified[1] == "3":
            modified_csv += "0,0,1,0,"
        elif row_modified[1] == "4":
            modified_csv += "0,0,1,1,"
        elif row_modified[1] == "5":
            modified_csv += "0,1,0,0,"
        elif row_modified[1] == "6":
            modified_csv += "0,1,0,1,"
        elif row_modified[1] == "7":
            modified_csv += "0,1,1,0,"
        elif row_modified[1] == "8":
            modified_csv += "0,1,1,1,"
        elif row_modified[1] == "9":
            modified_csv += "1,0,0,0,"
        elif row_modified[1] == "10":
            modified_csv += "1,0,0,1,"
        elif row_modified[1] == "11":
            modified_csv += "1,0,1,0,"
        elif row_modified[1] == "12":
            modified_csv += "1,0,1,1,"
        elif row_modified[1] == "13":
            modified_csv += "1,1,0,0,"
        else:
            "ERROR,ERROR,ERROR,ERROR,"

        # S2 Suit of Card 2
        if row_modified[2] == "1":
            modified_csv += "0,0,"
        elif row_modified[2] == "2":
            modified_csv += "0,1,"
        elif row_modified[2] == "3":
            modified_csv += "1,0,"
        elif row_modified[2] == "4":
            modified_csv += "1,1,"
        else:
            modified_csv += "ERROR,ERROR,"

        # C2 Rank of card 2
        if row_modified[3] == "1":
            modified_csv += "0,0,0,0,"
        elif row_modified[3] == "2":
            modified_csv += "0,0,0,1,"
        elif row_modified[3] == "3":
            modified_csv += "0,0,1,0,"
        elif row_modified[3] == "4":
            modified_csv += "0,0,1,1,"
        elif row_modified[3] == "5":
            modified_csv += "0,1,0,0,"
        elif row_modified[3] == "6":
            modified_csv += "0,1,0,1,"
        elif row_modified[3] == "7":
            modified_csv += "0,1,1,0,"
        elif row_modified[3] == "8":
            modified_csv += "0,1,1,1,"
        elif row_modified[3] == "9":
            modified_csv += "1,0,0,0,"
        elif row_modified[3] == "10":
            modified_csv += "1,0,0,1,"
        elif row_modified[3] == "11":
            modified_csv += "1,0,1,0,"
        elif row_modified[3] == "12":
            modified_csv += "1,0,1,1,"
        elif row_modified[3] == "13":
            modified_csv += "1,1,0,0,"
        else:
            "ERROR,ERROR,ERROR,ERROR,"

        # S3 Suit of Card 3
        if row_modified[4] == "1":
            modified_csv += "0,0,"
        elif row_modified[4] == "2":
            modified_csv += "0,1,"
        elif row_modified[4] == "3":
            modified_csv += "1,0,"
        elif row_modified[4] == "4":
            modified_csv += "1,1,"
        else:
            modified_csv += "ERROR,ERROR,"

        # C3 Rank of card 3
        if row_modified[5] == "1":
            modified_csv += "0,0,0,0,"
        elif row_modified[5] == "2":
            modified_csv += "0,0,0,1,"
        elif row_modified[5] == "3":
            modified_csv += "0,0,1,0,"
        elif row_modified[5] == "4":
            modified_csv += "0,0,1,1,"
        elif row_modified[5] == "5":
            modified_csv += "0,1,0,0,"
        elif row_modified[5] == "6":
            modified_csv += "0,1,0,1,"
        elif row_modified[5] == "7":
            modified_csv += "0,1,1,0,"
        elif row_modified[5] == "8":
            modified_csv += "0,1,1,1,"
        elif row_modified[5] == "9":
            modified_csv += "1,0,0,0,"
        elif row_modified[5] == "10":
            modified_csv += "1,0,0,1,"
        elif row_modified[5] == "11":
            modified_csv += "1,0,1,0,"
        elif row_modified[5] == "12":
            modified_csv += "1,0,1,1,"
        elif row_modified[5] == "13":
            modified_csv += "1,1,0,0,"
        else:
            "ERROR,ERROR,ERROR,ERROR,"

        # S3 Suit of Card 4
        if row_modified[6] == "1":
            modified_csv += "0,0,"
        elif row_modified[6] == "2":
            modified_csv += "0,1,"
        elif row_modified[6] == "3":
            modified_csv += "1,0,"
        elif row_modified[6] == "4":
            modified_csv += "1,1,"
        else:
            modified_csv += "ERROR,ERROR,"

        # C3 Rank of card 4
        if row_modified[7] == "1":
            modified_csv += "0,0,0,0,"
        elif row_modified[7] == "2":
            modified_csv += "0,0,0,1,"
        elif row_modified[7] == "3":
            modified_csv += "0,0,1,0,"
        elif row_modified[7] == "4":
            modified_csv += "0,0,1,1,"
        elif row_modified[7] == "5":
            modified_csv += "0,1,0,0,"
        elif row_modified[7] == "6":
            modified_csv += "0,1,0,1,"
        elif row_modified[7] == "7":
            modified_csv += "0,1,1,0,"
        elif row_modified[7] == "8":
            modified_csv += "0,1,1,1,"
        elif row_modified[7] == "9":
            modified_csv += "1,0,0,0,"
        elif row_modified[7] == "10":
            modified_csv += "1,0,0,1,"
        elif row_modified[7] == "11":
            modified_csv += "1,0,1,0,"
        elif row_modified[7] == "12":
            modified_csv += "1,0,1,1,"
        elif row_modified[7] == "13":
            modified_csv += "1,1,0,0,"
        else:
            "ERROR,ERROR,ERROR,ERROR,"

        # S3 Suit of Card 5
        if row_modified[8] == "1":
            modified_csv += "0,0,"
        elif row_modified[8] == "2":
            modified_csv += "0,1,"
        elif row_modified[8] == "3":
            modified_csv += "1,0,"
        elif row_modified[8] == "4":
            modified_csv += "1,1,"
        else:
            modified_csv += "ERROR,ERROR,"

        # C3 Rank of card 5
        if row_modified[9] == "1":
            modified_csv += "0,0,0,0,"
        elif row_modified[9] == "2":
            modified_csv += "0,0,0,1,"
        elif row_modified[9] == "3":
            modified_csv += "0,0,1,0,"
        elif row_modified[9] == "4":
            modified_csv += "0,0,1,1,"
        elif row_modified[9] == "5":
            modified_csv += "0,1,0,0,"
        elif row_modified[9] == "6":
            modified_csv += "0,1,0,1,"
        elif row_modified[9] == "7":
            modified_csv += "0,1,1,0,"
        elif row_modified[9] == "8":
            modified_csv += "0,1,1,1,"
        elif row_modified[9] == "9":
            modified_csv += "1,0,0,0,"
        elif row_modified[9] == "10":
            modified_csv += "1,0,0,1,"
        elif row_modified[9] == "11":
            modified_csv += "1,0,1,0,"
        elif row_modified[9] == "12":
            modified_csv += "1,0,1,1,"
        elif row_modified[9] == "13":
            modified_csv += "1,1,0,0,"
        else:
            "ERROR,ERROR,ERROR,ERROR,"
        
        # Class Poker Hand
        if row_modified[10] == "0":
            modified_csv += "0,0,0,0\r\n"
        elif row_modified[10] == "1":
            modified_csv += "0,0,0,1\r\n"
        elif row_modified[10] == "2":
            modified_csv += "0,0,1,0\r\n"
        elif row_modified[10] == "3":
            modified_csv += "0,0,1,1\r\n"
        elif row_modified[10] == "4":
            modified_csv += "0,1,0,0\r\n"
        elif row_modified[10] == "5":
            modified_csv += "0,1,0,1\r\n"
        elif row_modified[10] == "6":
            modified_csv += "0,1,1,0\r\n"
        elif row_modified[10] == "7":
            modified_csv += "0,1,1,1\r\n"
        elif row_modified[10] == "8":
            modified_csv += "1,0,0,0\r\n"
        elif row_modified[10] == "9":
            modified_csv += "1,0,0,1\r\n"
        else:
            modified_csv += "ERROR,ERROR,ERROR,ERROR\r\n"
    
    fn = open(dest_name, "w+")
    fn.write(modified_csv)

    fp.close()
    fn.close()

if __name__ == "__main__":
    convert_data("poker-hand-testing.data", "testing.csv")
    convert_data("poker-hand-training-true.data", "training.csv")

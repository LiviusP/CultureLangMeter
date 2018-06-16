import csv


def main():
    with open("messages.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter='|')
        for row in reader:
           message = row[2]

        
	print message   

if __name__ == '__main__':
    main()

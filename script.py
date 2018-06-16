import csv
import paralleldots

API_KEY = "mfEFDGHIALHCwJSDLx5uTsBrxtmn1Ol2yqkz1uIk7bI"


def main():
	paralleldots.set_api_key(API_KEY)

	with open("messages.csv") as csv_file:
		reader = csv.reader(csv_file, delimiter='|')
		for row in reader:
			message = row[2]

	response = paralleldots.language_detection(message)
	language = response['output']

	print language    

if __name__ == '__main__':
    main()
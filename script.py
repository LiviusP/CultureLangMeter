import csv
import paralleldots

API_KEY = "mfEFDGHIALHCwJSDLx5uTsBrxtmn1Ol2yqkz1uIk7bI"
TEST_MESSAGES=["Thank you for your message", "Danke fur deine text"]

def main():
	paralleldots.set_api_key(API_KEY)

	with open("messages.csv") as csv_file:
		reader = csv.reader(csv_file, delimiter='|')
		for row in reader:
			message = row[2]

	response = paralleldots.batch_language_detection(TEST_MESSAGES)

	languages = []

	for result in response['batch']:
		languages.append(result['output'])

	print languages    

if __name__ == '__main__':
    main()
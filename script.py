import csv
import paralleldots

API_KEY = "mfEFDGHIALHCwJSDLx5uTsBrxtmn1Ol2yqkz1uIk7bI"


def main():
	paralleldots.set_api_key(API_KEY)
	messages = []
	with open("messages.csv") as csv_file:
		reader = csv.reader(csv_file, delimiter='|')
		for row in reader:
			messages.append(row[2])

	#response = paralleldots.language_detection(message)
	#language = response['output']

	messages = messages[1:]
	response = paralleldots.batch_emotion(messages)

	emotions = []
	for result in response['batch']:
		emotions.append(result['emotion']['emotion'])

	print emotions    

if __name__ == '__main__':
    main()
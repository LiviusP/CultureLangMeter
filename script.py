import csv
import paralleldots
import xlwt

API_KEY = "mfEFDGHIALHCwJSDLx5uTsBrxtmn1Ol2yqkz1uIk7bI"
TEST_MESSAGES=["Thank you for your message", "Danke fur deine text"]

def main():
	paralleldots.set_api_key(API_KEY)
	messages = []
	with open("messages.csv") as csv_file:
		reader = csv.reader(csv_file, delimiter='|')
		for row in reader:
			messages.append(row[2])

	messages = messages[1:]


	emotions = []
	response = paralleldots.batch_emotion(messages)
	for result in response['batch']:
		emotions.append(result['emotion']['emotion'])

	languages = []
	response = paralleldots.batch_language_detection(messages)
	for result in response['batch']:
		languages.append(result['output'])

	sentiments = []
	response = paralleldots.batch_sentiment(messages)
	for result in response['batch']:
		sentiments.append(result['sentiment'])
	
	data = {}

	data['languages'] = languages
	data['emotions'] = emotions
	data['sentiments'] = sentiments

	generareRaport(data)


def generareRaport(data):

	wb = xlwt.Workbook()
	style_percent = xlwt.easyxf(num_format_str='0.00%')

	for key in data:
		ws = wb.add_sheet(key)
		counter = {}
		for item in data[key]:
			total = len(data[key])

			if counter.get(item, None) == None:
				counter[item] = 1
			else:
				counter[item] = counter[item] + 1

		i = 0

		for item in counter:
			ws.write(i, 0, item)
			ws.write(i, 1, counter[item])
			ws.write(i, 2, (float(counter[item])/float(total)), style_percent)
			i = i + 1


		ws.write(i + 2, 0, "Total")
		ws.write(i + 2, 1, total)

	wb.save('example.xls')

if __name__ == '__main__':
    main()
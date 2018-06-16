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

	#response = paralleldots.language_detection(message)
	#language = response['output']

	messages = messages[1:]
	response = paralleldots.batch_emotion(messages)

	emotions = []
	for result in response['batch']:
		emotions.append(result['emotion']['emotion'])

	response = paralleldots.batch_language_detection(messages)

	languages = []

	for result in response['batch']:
		languages.append(result['output'])

	data = {}

	data['languages'] = languages
	data['emotions'] = emotions

	generareRaport(data)


def generareRaport(data):

	print data
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
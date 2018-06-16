import paralleldots


API_KEY = "mfEFDGHIALHCwJSDLx5uTsBrxtmn1Ol2yqkz1uIk7bI"
TEST_MESSAGE = "This is a test message"

def main():
    paralleldots.set_api_key(API_KEY)

    response = paralleldots.language_detection(TEST_MESSAGE)
    language = response['output']

    print language

if __name__ == '__main__':
    main()





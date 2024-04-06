from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
)
import requests


# Replace with your file path
PATH_TO_FILE = 'SOME_FILE.wav'

def main():
    deepgram = DeepgramClient('api')

    with open('Testing.m4a', 'rb') as buffer_data:
        payload = { 'buffer': buffer_data }

        options = PrerecordedOptions(
            smart_format=True, model="nova-2", language="en-US", diarize=True
        )

        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process.')

        response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
        # xresponse.to_json(indent=1))
        transcript = response.results.channels[0].alternatives[0].paragraphs.transcript
        g = transcript.replace('Speaker 0', 'Ayush')
        g = g.replace('Speaker 1', 'Sebastian')

        response = requests.post('https://lucky-cups-show.loca.lt/add_data', json={'data': g})

        if response.status_code == 200:
            print('Data sent successfully.')
        else:
            print('Error sending data:', response.status_code)


if __name__ == '__main__':
    main()
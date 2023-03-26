def whisper():
# Speech to Text

    import openai
    # transcript = {'text':'I have frequent loose and watery stool, I feel abdominal pain and cramps.'}
    
    # fetching key from file 'OpenAI-API.txt'
    key = open('OpenAI-API.txt','r').readline() # Enter <API-key> in a file named as 'OpenAI-API.txt' in a project folder.
    print('Key for Whisper API fetched')
    openai.api_key = key
    print('Transcribing...')
    with open("recorded_audio.wav", "rb") as f:
        transcript = openai.Audio().transcribe("whisper-1", f)
    # return transcript['text']

    print('Transcribed User Input: '+str({transcript['text']}))
    prompt = open('GPT-3.5_data.txt','a+')
    input = '\nuser: '+str(transcript['text'])
    prompt.write(input)

    print('Transcribed Input saved in a data file.')

# whisper()
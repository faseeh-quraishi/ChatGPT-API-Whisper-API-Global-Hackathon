def whisper():
# Speech to Text

    import openai
    # transcript = {'text':'I have frequent loose and watery stool, I feel abdominal pain and cramps.'}
    
    # fetching key
    key = open('OpenAI-API.txt','r').readline()
    openai.api_key = key
    print('transcribing...')
    with open("recorded_audio.wav", "rb") as f:
        transcript = openai.Audio().transcribe("whisper-1", f)
    # return transcript['text']

    print('Transcribed User Input: '+{transcript['text']})
    prompt = open('GPT-3.5_data.txt','a+')
    input = '\nuser: '+transcript['text']
    prompt.write(input)

# whisper()
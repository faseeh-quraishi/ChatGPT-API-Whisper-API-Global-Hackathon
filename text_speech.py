
def text_to_speech(text):
    import pyttsx3
    text_speech = pyttsx3.init()
    text_speech.say(text)
    text_speech.runAndWait()

# text_to_speech('According to your described symptoms, you might have urine Migrain. There are herbal treatment you should take Feverfew, Butterbur, Peppermint, Willow, Ginger, Caffeine, Valerian and Coriander seed.')
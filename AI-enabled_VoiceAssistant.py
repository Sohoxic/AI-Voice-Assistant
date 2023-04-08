import openai
import pyttsx3 # converts text to speech
import speech_recognition as sr # to transcribe speech to text
import time
# Setting up OpenAPI key
openai.api_key = "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"

#Initialising the text-to-speech engine
engine = pyttsx3.init() # creating an instance of the text-to-speech engine using the init method

#function to transcribe our voice commands into text for our python program to understand
def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            print("Skipping unknown error")

#function to generate response from chatgpt
def generate_response(prompt):   #prompt is the text that we want to generate a response for
    response = openai.Completion.create(
        engine="text-davinci-003",      #specifying the engine as gpt3 model by inserting text-davinci-003
        prompt=prompt,
        max_tokens=4000,    #max tokkens is the max no. of characters that the gpt will respond with, if we reduce the max token size then the response will be faster.
        n=1,
        stop=None,
        temperature=0.5,    #temperature is a parameter to control the creativity or randomness of the generated text. A value of 0.5 balances between the predictability and creativity in the generated text
    ) 
    return response["choices"][0]["text"]

#creating a simple function for speaking our responses from the assistant so that it's voice interactive
def speak_text(text):   #this function will convert the text to speech using the pyttsx3
    engine.say(text)    #engine.say() is used to specify the text to be spoken
    engine.runAndWait() #this is used to play the speech

def main():
    while True:
        print("Say 'Sorry Bhai to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "sorry bhai":  #check if the person said sorry bhai or not
                    # Record audio
                    filename="input.wav"
                    print("Say your question...")   # is transcribed text="sorry bhai" then record more audio files into input.wav
                    with sr.Microphone () as source:
                        recognizer = sr. Recognizer()
                        source.pause_threshold :1
                        audio = recognizer.listen (source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                    # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print("You said: {text}")

                        #Generate response using GPT-3
                        response = generate_response(text)
                        print("GPT-3 says: {response}")

                        #Read response using text-to-speech
                        speak_text(response)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    main()
    




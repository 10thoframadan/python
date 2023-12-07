from openai import OpenAI
api_key="YOUR_OPEN_API_KEY_HERE"
client=OpenAI(api_key=api_key)
text="""
Hello world
"""
response=client.audio.speech.create(
    model="tts-1" # models: tts-1 and tts-1-hd,
    voice="echo" #voices: onyx and echo and fable and shimmer and nova,
    input=text,
    speed=1.0,
)
response.stream_to_file("output.mp3")
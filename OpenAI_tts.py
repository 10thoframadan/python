from openai import OpenAI
api_key="YOUR_OPEN_API_KEY_HERE"
client=OpenAI(api_key=api_key)
text="""
Hello world
"""
response=client.audio.speech.create(
    model="tts-1",
    voice="echo",
    input=text,
    speed=1.0,
)
response.stream_to_file("output.mp3")
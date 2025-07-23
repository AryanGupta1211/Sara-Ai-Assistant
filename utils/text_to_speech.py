import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
from gtts import gTTS
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def play_audio_ffplay_silent(output_filepath):
    try:
        if platform.system() == "Windows":
            # Hide the console window
            CREATE_NO_WINDOW = subprocess.CREATE_NO_WINDOW
            subprocess.Popen(
                ['ffplay', '-nodisp', '-autoexit', output_filepath],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=CREATE_NO_WINDOW
            )
        else:
            # macOS/Linux (won't show terminal either)
            subprocess.Popen(
                ['ffplay', '-nodisp', '-autoexit', output_filepath],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text= input_text,
        voice_id="9BWtsMINqrJLrRacOk9x", #"JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_22050_32", 
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            play_audio_ffplay_silent(output_filepath)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            play_audio_ffplay_silent(output_filepath)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# input_text = "Hi, I am doing fine, how are you? This is a test for AI with Aryan"
# output_filepath = "test_text_to_speech.mp3"
# text_to_speech_with_elevenlabs(input_text, output_filepath)
# text_to_speech_with_gtts(input_text, output_filepath)
import os
import glob
import shutil
from pathlib import Path

def collect_audio_files():
    home = Path.home()
    directories = [home,"D:\\"]
    audio_files = []
    audio_extensions = ['.mp3','.wav','.ogg', '.flac', '.acc']

    for directory in directories:
        for root, dirs, files in os.walk(directory):
            if 'System' in dirs:
                dirs.remove('System')
            if 'Windows' in dirs:
                dirs.remove('Windows')
            for file in files:
                if file.lower().endswith(tuple(audio_extensions)):
                    audio_files.append(os.path.join(root, file))
    return audio_files

def copying_the_audio_to_one_folder():
    destination_path = Path("D:\\All_Music_Files")
    destination_path.mkdir(exist_ok=True)

    if os.path.exists(destination_path):
        audio_files = collect_audio_files()

        for file in audio_files:
            shutil.copy(file, destination_path)
        print(f'All the audio files have been copied in this folder {destination_path}')
    else:
        print(f'This {destination_path} file path does not exits')

copying_the_audio_to_one_folder()

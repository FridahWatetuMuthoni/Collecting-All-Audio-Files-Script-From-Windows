def collect_audio(path):
    audio_files = []
    audio_extensions = ['.mp3','.wav','.ogg', '.flac', '.acc']

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(tuple(audio_extensions)):
                audio_files.append(os.path.join(root, file))
    return audio_files


def copy_files(path):
    destination_path = Path("D:\\All_Music_Files")
    destination_path.mkdir(exist_ok=True)
    if os.path.exists(destination_path):
        audio_files = collect_audio(path)

        for file in audio_files:
            shutil.copy(file, destination_path)
        print(f'All the audio files have been copied in this folder {destination_path}')
    else:
        print(f'This {destination_path} file path does not exits')

path = 'D:\\MUSIC\\pop'
copy_files(path)

import os
from pydub import AudioSegment

# Folder path to be converted
folder_path = "/Users/seong-gyeongjun/Downloads/논문 프로젝트- 음악 구분 딥러닝/음원 길이 편집한 음원/dream theater/bass"

# Generate a list of all files and folders within the folder
all_files = os.listdir(folder_path)

# Select only mp4a files for conversion to wav
for file_name in all_files:
    if file_name.endswith(".mp4a"):
        mp4a_file_path = os.path.join(folder_path, file_name)
        wav_file_path = os.path.join(folder_path, file_name.replace(".mp4a", ".wav"))
        sound = AudioSegment.from_file(mp4a_file_path, format="mp4")
        sound.export(wav_file_path, format="wav")

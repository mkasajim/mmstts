import urllib.request
import os
import tarfile
import shutil
from ttsmms import TTS

def download_file(url, destination):
    urllib.request.urlretrieve(url, destination)
    with tarfile.open(destination, 'r:gz') as tar:
        tar.extractall('data/')

def work(language, text):
    url = f"https://dl.fbaipublicfiles.com/mms/tts/{language}.tar.gz"
    # Create the 'data' directory
    os.makedirs('data', exist_ok=True)
    destination = f"data/{language}.tar.gz"
    download_file(url, destination)
    tts = TTS(f"data/{language}")
    tts.synthesis(text.lower(), wav_path="output.wav")
    shutil.rmtree('data')
    
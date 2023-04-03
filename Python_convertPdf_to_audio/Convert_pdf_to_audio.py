#import libraries which we are using
from gtts import gTTS
import pdfplumber
from pathlib import Path
from art import tprint

def pdf_to_audio(file_path='test.pdf', language='en'):

    if Path(file_path).suffix == '.pdf' and Path(file_path).is_file():

        print(f'[+] File name: {Path(file_path).name}')
        print(f'[+] Processing file...')
        
        with pdfplumber.PDF(open(file = file_path, mode = 'rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages] # reading text from pdf file

        text = ''.join(pages)
        text = text.replace('\n', ' ') # making text from pdf easier to read for gTTs, for one line

        audio = gTTS(text=text, lang=language, slow=False) # configure audio
        file_name = Path(file_path).stem # reading file name
        audio.save(f'{file_name}.mp3') # saving audio to mp3 file

        return f'[+] {file_name}.mp3 saved successfully, thank you for using!'
        
    

        

    else:
        return 'File is not exist, try another one path'
    

def main():
    tprint('PDF >> to >> audio')
    file_path = input('Please enter file path: ')
    language = input('Please choose language of pdf, for example "en": ')
    print(pdf_to_audio(file_path = file_path, language=language)) # sharing path of pdf file to pdf_to_audio function


if __name__ == '__main__':
    main()
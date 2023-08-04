import kivy
kivy.require('2.2.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from gtts import gTTS
import PyPDF2
import os

class TextToSpeechApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Text-to-Speech section
        self.text_input = TextInput(hint_text="Enter text to convert to speech", multiline=True)
        self.layout.add_widget(self.text_input)

        self.convert_text_button = Button(text="Convert Text to Speech", on_press=self.convert_text_to_speech)
        self.layout.add_widget(self.convert_text_button)

        # PDF-to-Speech section
        self.file_chooser = FileChooserListView(path=os.getcwd(), filters=["*.pdf"])
        self.layout.add_widget(self.file_chooser)

        self.convert_pdf_button = Button(text="Convert PDF to Speech", on_press=self.convert_pdf_to_speech)
        self.layout.add_widget(self.convert_pdf_button)

        return self.layout

    def convert_text_to_speech(self, instance):
        text = self.text_input.text
        language = 'en'  # You can change the language code as needed

        try:
            tts = gTTS(text=text, lang=language, slow=False)
            tts.save("output.mp3")
            print("Text converted to speech and saved as 'output.mp3'")
        except Exception as e:
            print("An error occurred:", str(e))

    def convert_pdf_to_speech(self, instance):
        pdf_path = self.file_chooser.selection[0]
        language = 'en'  # You can change the language code as needed

        try:
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                pdf_text = ""
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    pdf_text += page.extractText()
            
            tts = gTTS(text=pdf_text, lang=language, slow=False)
            tts.save("output.pdf.mp3")
            print("PDF content converted to speech and saved as 'output.pdf.mp3'")
        except Exception as e:
            print("An error occurred:", str(e))

if __name__ == "__main__":
    TextToSpeechApp().run()

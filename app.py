from flask import Flask, render_template, request, send_from_directory, make_response
import speak

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak_text():
    print("Received request at /speak")  # Debugging log

    language = request.form['language']
    text = request.form['text']
    print(f"Language: {language}, Text: {text}")  # Debugging log

    speak.work(language, text)

    print("Audio file generated")  # Debugging log

    response = make_response(send_from_directory(directory='.', path='output.wav', as_attachment=False))
    response.headers['Content-Type'] = 'audio/wav'
    return response

if __name__ == '__main__':
    app.run()
from flask import Flask, render_template, request
import processor


app = Flask(__name__, template_folder='templates', static_url_path="")
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(processor.chatbot_response(userText))

if __name__ == '__main__':
    app.run(debug=True)

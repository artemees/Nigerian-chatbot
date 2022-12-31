from flask import Flask, render_template, request
import processor

app = Flask(__name__, template_folder='templates', static_url_path="")
@app.route('/', methods=["GET", "POST"])
@cache.cached(timeout=60)
def index():
    return render_template('index1.html', **locals())


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(processor.chatbot_response(userText))

if __name__ == '__main__':
    app.run(host="0.0.0.0")

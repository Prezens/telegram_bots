# TODO
# Getter messages
# Setter messages

from flask import Flask
from flask import request
from flask import jsonify
# from flask_sslify import SSLify
import requests
import json

app = Flask(__name__)
# sslify = SSLify(app)

URL = 'https://api.telegram.org/bot609170116:AAFlrhw8htnlpN7sokJO4QmqISimsL3vP9Q/'


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# def get_updates():
#     # https://api.telegram.org/bot609170116:AAFlrhw8htnlpN7sokJO4QmqISimsL3vP9Q/getUpdates
#     url = URL + 'getUpdates'
#     r = requests.get(url)
#     # write_json(r.json())
#
#     return r.json()


def send_message(chat_id, text='...'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)

    return r.json()


# def main():
#     # r = requests.get(URL + 'getMe')
#     # write_json(r.json())
#     # r = get_updates()
#     # chat_id = r['result'][-1]['message']['chat']['id']
#     # print(chat_id)
#     pass


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        if 'bitcoin' in message:
            send_message(chat_id, text='...')

        # write_json(r)

        return jsonify(r)

    return '<h1>Bot welcome you</h1>'


if __name__ == '__main__':
    # main()
    app.run()

from flask import Flask, render_template, request, jsonify
from utils.kafkaUtils import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<bootstrap_servers>')
def get_list(bootstrap_servers):
    print(request.path)
    bootstrap_servers = bootstrap_servers.split("=")[1]
    print(bootstrap_servers)
    str_topics = get_kafka_topics(bootstrap_servers)
    return jsonify(str_topics)

@app.route('/<name>/<topic_name>')
def get_messages(name, topic_name):
    print(request.path)
    bootstrap_servers = name.split("=")[1]
    print(bootstrap_servers)
    print(topic_name)
    list_messages = get_messages_from_topic(bootstrap_servers, topic_name)
    list_messages = ["</br>" + x.decode("utf-8") for x in list_messages]
    return str(list_messages)

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.run(debug=True)
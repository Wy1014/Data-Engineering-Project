from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import joblib
import pandas as pd

model = joblib.load('tweet.model')
data = pd.read_csv('./tweet_fin.csv')


app = Flask(__name__)


def get_result(text):
    if text == '':
        return ''
    test = text.split(' ')
    vec = model.infer_vector(doc_words=test,alpha=0.025,steps=500)
    sim = model.docvecs.most_similar([vec],topn=20)
    tweet = list(data['ori_tweet'])
    responce = ''
    for count,sims in sim:
        sentence = tweet[count]
        words=''
        for word in sentence:
            words = words + word + ''
        responce = responce + words + ""
#        print(words)
    return responce

@app.route('/', methods=['GET', 'POST'])
def index():
    text = u''
    result = ''
    if request.method == 'POST':
        text = request.form.get("text",False)
        result = get_result('text')
        return render_template('twitter.html',text=text,result=result)
    return render_template('twitter.html',text=text,result=result)


if __name__ == '__main__':
    redis_client = StrictRedis(host='redis', port=6379)
    app.run(host='0.0.0.0')

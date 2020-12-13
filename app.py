from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import joblib
import pandas as pd

model = joblib.load('Doc2Vec.model')
data = pd.read_csv('./tweet_fin.csv')


app = Flask(__name__)

	
#def get_tweet(text):
#	if text=='':
#		return ''
#	result = model.get_result([text])
#	responce = "Result:" + result
#	return responce

def get_result(text):
    test = text.split(' ')
    vec = model.infer_vector(doc_words=test,alpha=0.025,steps=500)
    sim = model.docvecs.most_similar([vec],topn=20)
    tweet = list(data['text'])
    for count,sims in sim:
        sentence = tweet[count]
        words=''
        for word in sentence:
            words = words + word + ''
    return words
	
@app.route('/', methods=['GET', 'POST'])
def index():
	text = ''
	result = ''
	if request.method == 'POST':
		text = request.form['text']
		result = get_result(text)
		return render_template('twitter.html')	
	return render_template('twitter.html')

if __name__ == '__main__':
	redis_client = StrictRedis(host='redis', port=6379)
	app.debug = True
	app.run(host='0.0.0.0')
	
	
	
	
	
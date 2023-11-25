from flask import Flask,render_template,redirect,request
from openai import OpenAI

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def generator():
        title = 'Your Image will be generated here'

        key = open("gen_key.txt","r").read()

        client = OpenAI(api_key= str(key))

        text = str(request.form.get('textget'))

        response = client.images.generate(
        model="dall-e-3",
        prompt= text,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        source = response.data[0].url


        return render_template(
            'show.html',
            title = title,
            source = source)
    
    
    return app
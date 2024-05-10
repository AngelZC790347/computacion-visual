from flask import Flask, render_template, request, redirect
import tempfile
import os
import base64
app = Flask(__name__, static_folder="/static")


@app.get('/')
def home():
    return render_template("index.html")


@app.post('/upload')
def upload_image():
    try:
        # check if the post request has the file part
        print(request.form)
        img_data = request.form.get('image-data').replace("data:image/png;base64,","")
        print(img_data)
        aleatorio = request.form.get('numero')
        print(aleatorio)
        with tempfile.NamedTemporaryFile(delete = False, mode = "w+b", suffix='.png', dir=str(aleatorio)) as fh:
            fh.write(base64.b64decode(img_data))
        print("Image uploaded")
    except Exception as err:
        print("Error occurred")
        print(err)

    return redirect("/", code=302)


if __name__ == '__main__':
    digits = ['U', 'P', 'C', 'H']
    for d in digits:
        if not os.path.exists(str(d)):
            os.mkdir(str(d))
    app.run(debug=True,port=1000)

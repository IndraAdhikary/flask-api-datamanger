from flask import Flask,render_template,request
import os

app = Flask(__name__)

app.config["UPLOAD_PATH"] = "D:/"

@app.route("/upload_file",methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        f=request.files['file_name']
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
        return render_template("upload-file.html",msg="File has been uploaded successfully")
    return render_template('/upload-file.html',msg="Select your file")


if __name__== '__main__':
    app.run()
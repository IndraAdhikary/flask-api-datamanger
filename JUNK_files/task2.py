import pandas as pd
from flask import Flask,render_template,request
import os


app = Flask(__name__)

@app.route("/download_task2_file",methods=["GET","POST"])
def download_task2_files():
    if request.method == 'POST':
    
        df = pd.read_excel('D://mass_spec_data_assgnmnt.xlsx-I.xlsx')

        df.dropna(inplace=True)

        df['Retention Time Roundoff (in mins)'] = pd.Series([int(round(i)) for i in df['Retention time (min)']])
        
        df.to_excel('D://task2_added_column.xlsx')
        
        return render_template("download-task2-file.html",msg="File has been downloaded successfully")
    
    return render_template('/download-task2-file.html',msg="Download task 2 files")
    


if __name__== '__main__':
    app.run()
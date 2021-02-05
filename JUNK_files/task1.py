import pandas as pd
from flask import Flask,render_template,request
import os


app = Flask(__name__)

@app.route("/download_task1_file",methods=["GET","POST"])
def download_task1_files():
    if request.method == 'POST':
    
        df = pd.read_excel('D://mass_spec_data_assgnmnt.xlsx-I.xlsx')

        df.dropna(inplace=True)

        PC_df = df[df['Accepted Compound ID'].str[-2:]==('PC')]

        LPC_df = df[df['Accepted Compound ID'].str[-3:]==('LPC')]

        plas_df = df[df['Accepted Compound ID'].str[-11:]==('plasmalogen')]
        
        PC_df.to_excel('D://task1_PC_names_output1.xlsx')
        LPC_df.to_excel('D://task1_LPC_names_output2.xlsx')
        plas_df.to_excel('D://task1_plas_names_output3.xlsx')
        
        return render_template("download-task1-file.html",msg="Files have been downloaded successfully")
    
    return render_template('/download-task1-file.html',msg="Download task 1 files")
    


if __name__== '__main__':
    app.run()
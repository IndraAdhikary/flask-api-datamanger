import pandas as pd
from flask import Flask,render_template,request
import os


app = Flask(__name__)

@app.route("/download_task3_file",methods=["GET","POST"])
def download_task3_files():
    if request.method == 'POST':
    
        df = pd.read_excel('D://mass_spec_data_assgnmnt.xlsx-I.xlsx')

        df.dropna(inplace=True)

        df['Retention Time Roundoff (in mins)'] = pd.Series([int(round(i)) for i in df['Retention time (min)']])
        
        list_metabols = [i for i in df if i not in ['m/z','Retention time (min)','Accepted Compound ID']]
        
        new_df = pd.DataFrame()
        
        for i in list_metabols:
            new_df[i] = df[i]
            
        by_rettime = new_df.groupby('Retention Time Roundoff (in mins)')
        
        df_mean = by_rettime.mean()
        
        df_mean.to_excel('D://task3_mean_by_metabols.xlsx')
        
        return render_template("download-task3-file.html",msg="File has been downloaded successfully")
    
    return render_template('/download-task3-file.html',msg="Download task 3 files")
    


if __name__== '__main__':
    app.run()
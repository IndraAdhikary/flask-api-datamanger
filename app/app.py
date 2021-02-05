import pandas as pd
from flask import Flask,render_template,request
import os

app = Flask(__name__)

app.config["UPLOAD_PATH"] = "D:/"

@app.route("/")
def index():
    return render_template('/index.html')


@app.route("/upload_file",methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        f=request.files['file_name']  # request file name
        f.save(os.path.join("D:/",f.filename)) #upload file in D:/ directory of host
        return render_template("upload-file.html",msg="File has been uploaded successfully")
    return render_template('/upload-file.html',msg="Select your file")

@app.route("/download_task1_file",methods=["GET","POST"])
def download_task1_files():
    if request.method == 'POST':
    
        df = pd.read_excel('D://mass_spec_data_assgnmnt.xlsx-I.xlsx')  #extract file saved in D:/ directory

        df.dropna(inplace=True) #remove null values in the dataframe

        PC_df = df[df['Accepted Compound ID'].str[-2:]==('PC')]  #names ending with PC

        LPC_df = df[df['Accepted Compound ID'].str[-3:]==('LPC')] #names ending with LPC

        plas_df = df[df['Accepted Compound ID'].str[-11:]==('plasmalogen')] #names ending with plasmalogen
        
        #saving corresponding files under D:/ drive
        
        PC_df.to_excel('D://task1_PC_names_output1.xlsx') 
        LPC_df.to_excel('D://task1_LPC_names_output2.xlsx')
        plas_df.to_excel('D://task1_plas_names_output3.xlsx')
        
        return render_template("download-task1-file.html",msg="Files have been downloaded successfully and saved under D directory")
    
    return render_template('/download-task1-file.html',msg="Download task 1 files")

@app.route("/download_task2_file",methods=["GET","POST"])
def download_task2_files():
    if request.method == 'POST':
    
        df = pd.read_excel('D://mass_spec_data_assgnmnt.xlsx-I.xlsx') #extract file saved in D:/ directory

        df.dropna(inplace=True) #remove null values in the dataframe

        df['Retention Time Roundoff (in mins)'] = pd.Series([int(round(i)) for i in df['Retention time (min)']]) #round off and save as a new column
        
        #saving corresponding file under D:/ drive
        
        df.to_excel('D://task2_added_column.xlsx')
        
        return render_template("download-task2-file.html",msg="File has been downloaded successfully and saved under D directory")
    
    return render_template('/download-task2-file.html',msg="Download task 2 files")

@app.route("/download_task3_file",methods=["GET","POST"])
def download_task3_files():
    if request.method == 'POST':
    
        df = pd.read_excel('D://mass_spec_data_assgnmnt.xlsx-I.xlsx') #extract file saved in D:/ directory

        df.dropna(inplace=True) #remove null values in the dataframe

        df['Retention Time Roundoff (in mins)'] = pd.Series([int(round(i)) for i in df['Retention time (min)']]) #round off and save as a new column
        
        list_metabols = [i for i in df if i not in ['m/z','Retention time (min)','Accepted Compound ID']] #selecting list of required columns only
        
        new_df = pd.DataFrame()
        
        #curating a new dataframe
        
        for i in list_metabols:
            new_df[i] = df[i]
            
        #group by rounded off retention time 
            
        by_rettime = new_df.groupby('Retention Time Roundoff (in mins)')
        
        df_mean = by_rettime.mean()  #producing means
        
        #saving corresponding file under D:/ drive
        
        df_mean.to_excel('D://task3_mean_by_metabols.xlsx')
        
        return render_template("download-task3-file.html",msg="File has been downloaded successfully and saved under D directory")
    
    return render_template('/download-task3-file.html',msg="Download task 3 files")
    



if __name__== '__main__':
    app.run()
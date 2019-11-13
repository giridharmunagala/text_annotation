from flask import Flask, render_template, request
from flask import jsonify
import os
import json

app = Flask(__name__)


list_sentences = list()
remaining_files = list()
current_filename = ''
current_line = ''
current_entities = list()


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/get_next_file',methods=["POST"])
def get_next_file():
    lines_dict = {'status':False}
    
    if remaining_files:
        fileName = remaining_files[0]
        with open(os.path.join(source_folder,remaining_files.pop(0) + '.txt'),'r') as file:
            lines = file.read()
            lines_dict['fileName'] = fileName
            lines_dict['lines'] = lines
            lines_dict['status'] = True
            lines_dict["completed"] = False
    else:
        return jsonify({"completed":True})
    

    return jsonify(lines_dict)


@app.route('/write_entities_file', methods=["POST"])
def write_entities_file():
    global dest_folder
    file_name = request.form['fileName']
    entities = json.loads(request.form['entities'])['entities']
    print(type(entities))
    print(entities)
    if entities:
        with open(os.path.join(dest_folder,file_name+'.json'),'w') as file:
           json.dump({'entities':entities} , file)
    
    return {'status':True}


if __name__ == "__main__":
    cwd = os.getcwd()
    source_folder = os.path.join(cwd,'data','raw_text_files')
    dest_folder = os.path.join(cwd,'data','annotated_text')
    source_files = [filename for filename,_ in [os.path.splitext(file) for file in os.listdir(source_folder)]]
    dest_files = [filename for filename,_ in [os.path.splitext(file) for file in os.listdir(dest_folder)]]
    remaining_files = [file for file in source_files if file not in dest_files]
    app.run(port=5076)

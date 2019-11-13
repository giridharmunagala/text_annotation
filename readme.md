## Guidelines
1. Application requires Python 3.5 or above
2. Install requirements using **pip install -r requirements.txt**
3. Put your files in text format into /data/raw_text_files folder
4. Annotated files will be written to /data/annotated_text folder in json format
5. Run api using **python text_annotation_api.py**
6. Open a web browser and go to **http://localhost:5076/** 

## Description

Python application for Entity annotation in text.

Annotations available
1. Name
2. Location
3. CollegeName
4. Skill
5. EduCertName
6. Duration
7. Designation
8. Company

Annotation format
{"entities": [{"startIndex": 0, "endIndex": 21, "text": "Munagala Giridhar", "label": "name"}]}

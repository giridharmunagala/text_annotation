## Guidelines
1. Install requirements using **pip install -r requirements.txt**
2. Put your files in text format into /data/raw_text_files folder
3. Annotated files will be written to /data/annotated_text folder in json format
4. Open a web browser and go to **http://localhost:5076/** 

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

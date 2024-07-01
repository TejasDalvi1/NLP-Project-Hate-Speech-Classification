===============================================================================
# NLP-Project-Hate-Speech-Classification
===============================================================================
## Tech stack:
        (1)Python
        (2)Tensorflow
        (3)NLTK
        (4)Google cloud (Bucket for storing data and model)
        (5)FastAPI
        (6)CircleCI
        (7)Docker
        (8)AWS (EC2,ECR for deployment)
-------------------------------------------------------------------------------
## Steps to run:

### (1) Create Environment
```bash
conda create -n hatespeech python=3.8 -y
```
```bash
conda activate hatespeech
```
### (2) Install "requirements.txt"
```bash
pip install -r requirements.txt
```
### (3) Run "app.py"
```bash
python app.py
```

## Setup GCloud using cli
```bash
#Add credentials
gcloud init
```
-------------------------------------------------------------------------------
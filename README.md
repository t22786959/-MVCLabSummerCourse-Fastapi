# -MVCLabSummerCourse-Fastapi
## How to run  
Step 1: Install Python Packages 
pip install -r requirements.txt

Step 2: Run by uvicorn (Localhost)
uvicorn main:app --reload
Default host = 127.0.0.1, port = 8000  

Step 3: Test your API using Swagger UI
http://127.0.0.1:8000/docs


## GET Method
### /male-animals  
* Get all the 'male' animals 
### /all-names
* Get all the animals' name
### /older-animals
* Get animals name and age which age is greater than five
### /delete-lastone
* test
### /show-animals
* Get all animals

## POST Method
### /add-animal
* add new animal to the zoo, each animal's information include  
'name': str  
'species': str   
'gender': str   
'age': float   

### /upload
* upload a json file to the server




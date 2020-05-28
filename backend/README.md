# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : "Science",
'2' : "Art",
'3' : "Geography",
'4' : "History",
'5' : "Entertainment",
'6' : "Sports"}

```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    'success': False,
    'error': 400,
    'message': "bad request"
}
```
The API will return five error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Sever Error

## Endpoints
### GET /categories
- General: Retrieve all categories.
    - Request Arguments: None.
    - Return: success value and a dictionary of categories.
- Sample: `curl http://127.0.0.1:5000/categories`
```

{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}

```

### GET /questions
- General: Retrieve all questions, and the results are paginated in groups of 10.
    - Request Arguments: None.
    - Return: success value, a list of a dictionary of questions, total number of questions, a dictonary of categories, and a list of categories of currently displayed questions.
- Sample: `curl http://127.0.0.1:5000/questions`
```

{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": [
    5,
    5,
    4,
    5,
    4,
    6,
    6,
    4,
    3,
    3
  ],
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"    
    },
    {
      "answer": "Edward Scissorhands",       
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 
1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"      
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to 
play in every soccer World Cup tournament?"  
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",  
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 19
}

```

### DELETE /questions/{question_id}
- General: Delete question using a question ID.
    - Request Arguments: an ID of a question to delete.
    - Return: success value, an ID of a deleted question, and total number of questions.
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/4?page=1`
```

{
  "deleted": 4,
  "success": true,
  "total_questions": 18
}

```

### POST /questions
- General: Create a new question using a question, answer, difficulty, and category.
    - Request Arguments: None.
    - Return: success value, an ID of a created question, and total number of questions.
- Sample: `curl http://127.0.0.1:5000/questions?page=2 -X POST -H "Content- 
Type: application/json" -d '{"question":"Who succeeded in Pop art  
industry with screen print images of Marilyn Monroe and soup cans?",  
"answer":"Andy Warhol", "difficulty":"2", "category": "2"}'`

```
{
  "created": 24,
  "success": true,
  "total_questions": 20
}

```

### POST /search
- General: Retrieve questions based on a search term. The search term is a substring of the question, and is case-insensitive.
    - Request Arguments: None.
    - Return: success value, a list of a dictionary of questions corresponding to a search term, total number of searched questions, and a list of categories of searched questions.
- Sample: `curl http://127.0.0.1:5000/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": 1990}'`
```
{
  "current_category": [
    5
  ],
  "questions": [
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed 
by Tim Burton about a young man with multi-bladed appendages?"     
    }
  ],
  "success": true,
  "total_questions": 1
}

```

### GET /categories/{category_id}/questions
- General: Retrieve questions of a selected category.
    - Request Arguments: an ID of a category.
    - Return: success value, a list of a dictionary of questions corresponding to the ID of a category, total number of questions, and a list of categories of currently displayed questions.
- Sample: `curl http://127.0.0.1:5000/categories/3/questions`
```
{
  "current_category": [
    3,
    3,
    3
  ],
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 3
}

```

### POST /quizzes
- General: Retrieve a random question within the given category or all questions to play the quiz.
    - Request Arguments: None.
    - Return: success value and a dictionary of a question.
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"id":"6", "type": "Sports"}}'`

```

{
  "question": {
    "answer": "Uruguay",
    "category": 6,
    "difficulty": 4,
    "id": 11,
    "question": "Which country won the first ever soccer World Cup 
in 1930?"
  },
  "success": true
}

```
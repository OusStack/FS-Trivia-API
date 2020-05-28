import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}"\
            .format('postgres', 'postgres', 'localhost:5432',
                    self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'Who succeeded in Pop art industry with\
            screen print images of Marilyn Monroe and soup cans?',
            'answer': 'Andy Warhol',
            'difficulty': 2,
            'category': '2'
        }

        self.new_question_fail = {
            'question': '',
            'answer': '',
            'difficulty': 1,
            'category': ''
        }

        self.quiz = {
            "previous_questions": [],
            "quiz_category": {'id': 6, 'type': 'Sports'}
        }

        self.quiz_fail = {
            "previous_questions": [],
            "quiz_category": {'id': 10, 'type': 'Cooking'}
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for
    successful operation and for expected errors.
    """
    def test_retrieve_categories(self):
        """Test all categories are retrieved."""
        res = self.client().get('/categories')
        data = json.loads(res.data)

        CATEGORY_COUNT = 6
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['categories']), CATEGORY_COUNT)
        self.assertIsInstance(data['categories'], dict)

    def test_retrieve_paginated_questions(self):
        """Test questions are paginated."""
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        QUESTIONS_PER_PAGE = 10
        TOTAL_QUESTIONS = 19
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['questions']), QUESTIONS_PER_PAGE)
        self.assertIsInstance(data['questions'], list)
        self.assertEqual(data['total_questions'], TOTAL_QUESTIONS)
        self.assertIsInstance(data['total_questions'], int)
        self.assertIsInstance(data['categories'], dict)
        self.assertIsInstance(data['current_category'], list)

    def test_retrieve_paginated_questions_fail(self):
        """Test 404 is sent when invalid page number is given."""
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_question(self):
        """
        Test a question is deleted only when the id exists,
        otherwise test fails.
        """
        res = self.client().delete('/questions/5')
        data = json.loads(res.data)
        question = Question.query.get(5)

        TOTAL_QUESTIONS = 19
        TEST_CREATE_QUESTION = 1
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], 5)
        self.assertEqual(data['total_questions'],
                         TOTAL_QUESTIONS - 1 + TEST_CREATE_QUESTION)
        self.assertIsInstance(data['total_questions'], int)
        self.assertIsNone(question)

    def test_delete_question_fail(self):
        """Test 422 is sent when the question does not exist."""
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

    def test_create_new_question(self):
        """Test a question is created."""
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['created'])
        self.assertIsInstance(data['total_questions'], int)

    def test_create_new_question_no_value_fail(self):
        """Test 422 is sent when no value is given."""
        res = self.client().post('/questions', json=self.new_question_fail,
                                 content_type='application/json')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'unprocessable')

    def test_create_new_question_with_wrong_url_fail(self):
        """Test 405 is sent when a wrong URL is given."""
        res = self.client().post('/questions/45', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'method not allowed')

    def test_search_questions_with_results(self):
        """Test questions are retrieved by keyword."""
        res = self.client().post('/search', json={'searchTerm': 1990})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['questions']), 1)
        self.assertTrue(data['total_questions'])
        self.assertIsInstance(data['total_questions'], int)
        self.assertIsInstance(data['current_category'], list)

    def test_search_questions_without_results(self):
        """Test questions are not retrieved by keyword."""
        res = self.client().post('/search', json={'searchTerm': 1993})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['questions']), 0)
        self.assertFalse(data['total_questions'])
        self.assertIsInstance(data['total_questions'], int)
        self.assertIsInstance(data['current_category'], list)

    def test_retrieve_questions_by_category(self):
        """Test questions are retrived by category."""
        res = self.client().get('/categories/3/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['questions'])
        self.assertEqual(len(data['questions']), 3)
        self.assertIsInstance(data['total_questions'], int)
        self.assertIsInstance(data['current_category'], list)

    def test_retrieve_questions_by_category_fail(self):
        """Test 404 is sent when invalid category id is given."""
        res = self.client().get('/categories/10/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

    def test_quizzes(self):
        """Test a quiz is retrieved."""
        res = self.client().post('/quizzes', json=self.quiz)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['question'])

    def test_quizzes_fail(self):
        """Test 404 is sent when a wrong category id is given."""
        res = self.client().post('/quizzes', json=self.quiz_fail)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'resource not found')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

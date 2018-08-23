import psycopg2
from api.db_connect import conn, cur

class Questions_model():    
    def __init__(self, question_title, question_details, user_id):
        self.question_title = question_title
        self.question_details = question_details
        self.user_id = user_id

    def get_questions():
        all_questions = list()

        try:
            cur.execute("SELECT * FROM questions")
                                  
            
        except psycopg2.DatabaseError as error:
            print(error)

        results = cur.fetchall()

        for result in results:
            all_questions.append(dict(question_id = result[0] , user_id = result[1], question_title = result[2], question_detail = result[3]))

            
        print(all_questions)
        return all_questions

    
    def insert_question(self):

        data = dict(user_id = self.user_id, question_title=self.question_title, question_details = self.question_details)

        submit = cur.execute("""INSERT INTO questions (user_id, question_title, question_details, created_at) VALUES 
                    (%(user_id)s, %(question_title)s, %(question_details)s, current_timestamp )""", data)

        conn.commit()

        return "Successfully added question"
"""Random Quiz Generator and File Manipulation"""

import random
print("Hello World!")



class QuizRandom:

    def __init__(self):

        capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
        'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
        'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
        'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
        'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
        'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
        'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
        'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
        'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
        'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
        'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
        'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


    def generate_quiz(self):

        for quizNum in range(35):

            with open('capitalsquiz%s.txt' % (quizNum + 1), 'w') as quizfile:

                # lets write the header of the quiz
                quizfile.write('Name:\n\nPeriod:\n\n')
                quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
                quizfile.write('\n\n')

                print(quizfile)

            with open('capitalsquiz_answers.txt%s.txt' % (quizNum + 1), 'w') as answerKeyFile:

                print(answerKeyFile)
            
quiz_gen = QuizRandom()
genn = quiz_gen.generate_quiz()
print(genn)
            





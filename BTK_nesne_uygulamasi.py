import os                 #Terminal temizlemek için
os.system('cls||clear')

class Question:
    def __init__(self,text,choise,answer):
        self.text=text
        self.choise=choise
        self.answer=answer
    def checkAnswer(self,answer):
        return self.answer==answer

class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0
        self.questionindex=0

    def getquestion(self):
        return self.questions[self.questionindex]

    def displayquestion(self):
        question=self.getquestion()
        print(f'Soru {self.questionindex+1}:{question.text}')

        for q in question.choise:
            print('-'+q)

        answer=input('cevap:')
        self.guess(answer)
        self.loadquestion()

    def showscore(self):
        print('Score:',self.score)

    def displayprogress(self):
        totalquestion=len(self.questions)
        questionnumber=self.questionindex+1

        if questionnumber>totalquestion:
            print('Quiz finished')
        else:
            print(f'Question {questionnumber} of {totalquestion}'.center(50,'*'))

    def guess(self,answer):
        question=self.getquestion()
        if question.checkAnswer(answer):
            self.score+=1
        self.questionindex+=1

    def loadquestion(self):
        if len(self.questions)==self.questionindex:
            self.showscore()
        else:
            self.displayprogress()
            self.displayquestion()
        

q1=Question('en iyi programlama dili hangisi',['C#','python','java'],'python')
q2=Question('en hızlı programlama dili hangisi',['C#','python','java'],'python')
q3=Question('en kazançlı programlama dili hangisi',['C#','python','java'],'python')
questionsss=[q1,q2,q3]

#print(q1.checkAnswer('python'))
#print(q2.checkAnswer('java'))

quizz=Quiz(questionsss)
quizz.loadquestion()
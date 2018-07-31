class nonTeach():
    sName=''
    marks=int()
    
class teach(nonTeach):
    number=int()
    aggregate=int()

class prin(teach):
    parentNumber=int()
    address=''
    
nonT=nonTeach()
nonT.sName='a'
nonT.marks=90
print("\n\nNon teacher can access:\nName-",nonT.sName,"\nMarks-",nonT.marks)


tea=teach()
tea.sName='a'
tea.marks=90
tea.number=9456713214
tea.aggregate=84
print("\n\nNon teacher can access:\nName-",tea.sName,"\nMarks-",tea.marks,
      "\nNumber-",tea.number,"\nAggregate-",tea.aggregate)

pr=prin()
pr.address="Bangalore"
pr.sName='a'
pr.marks=90
pr.number=9456713214
pr.aggregate=84
pr.parentNumber=7854621354
print("\n\nNon teacher can access:\nName-",tea.sName,"\nMarks-",tea.marks,
      "\nNumber-",tea.number,"\nAggregate-",tea.aggregate,
      "\nAddress-",pr.address,"\nParent number-",pr.parentNumber)
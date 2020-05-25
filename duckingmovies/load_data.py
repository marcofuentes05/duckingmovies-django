from actors.models import Actor

a = Actor(name='Jenniffer', lastName='Anniston',
    birthDate='1990-05-05',
    birthPlace='New York',
    netWorth ='90000000',
    height ='1.85',
    nickname ='Jen',
)
a.save()
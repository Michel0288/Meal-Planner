import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
fake = Faker()
import random
from random import randint
f = open("demofile3.sql", "w")


for i in range(10):
    value=randint(0,1000)
    fname=fake.first_name()
    lname=fake.last_name()
    p_age=randint(0,100)
    height=str(randint(1,8))+' '+'ft'+' '+str(randint(1,10))+' '+'in'
    weight=randint(50,1000)
    allergies=[ 'eggs','peanuts','shellfish','strawberries','tomatoes', 'chocolate','pollen','beef','soy']
    lifestyle=['Vegan','Vegetarian','Pescatarian']
    gender=['Male','Female']
    goal=['None','Lose Weight','Gain Weight','Maintain Weight']
    pic=['db1.jpg','db2.png','db3.png','db4.png','db5.png']
    f.write('INSERT INTO account VALUES('+'"'+fname+'"'+','+'"'+lname+'"'+','+'"'+fname+str(value)+'"'+','+'"'+lname+str(value)+'"'+','+str(p_age)+','+'"'+random.choice(gender)+'"'+','+'"'+height+'"'+','+str(weight)+','+'"'+random.choice(allergies)+'"'+','+'"'+random.choice(lifestyle)+'"'+','+'"'+random.choice(goal)+'"'+','+'"'+random.choice(pic)+'"'+');'+'\n')
f.close()
    # print('INSERT INTO account VALUES ('+fname,',',lname,',',fname+str(value),',',p_age,',',random.choice(gender),',',height,',', weight,',',random.choice(allergies),',',random.choice(lifestyle),',',random.choice(goal),',',random.choice(pic),')')
    
# df_fake_data = pd.DataFrame(fake_data)
# print(df_fake_data)
# engine = create_engine('mysql://root:@127.0.0.1/test2', echo=False)
# df_fake_data.to_sql('user', con=engine,index=False)

import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
fake = Faker()
fake_data = defaultdict(list)


for i in range(100):
    fake_data["account_id"].append(i+1)
    fake_data["firstname"].append( fake.first_name() )
    fake_data["lastname"].append( fake.last_name() )
df_fake_data = pd.DataFrame(fake_data)
print(df_fake_data)
# engine = create_engine('mysql://root:@127.0.0.1/test2', echo=False)
# df_fake_data.to_sql('user', con=engine,index=False)

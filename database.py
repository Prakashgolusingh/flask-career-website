from sqlalchemy import create_engine,text
import os
# pymssql
#dialect+driver://username:password@host:port/database
#dialect+driver://username:password@host/database_name

db_connect_string = os.environ['db_connect_string']


engine = create_engine(db_connect_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
'''
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  data = []
  #for row in result.all():
  result_all = result.mappings().all()
  for row in result_all:
    data.append(dict(row))
  print(type(result_all))
  print(result_all)
  print(type(data[0]))
  #print(dict(result_all[0]))
     # list.append(dict(row))

'''

def load_data_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    list = []
    for row in result.mappings().all():
      list.append(dict(row))
  return list







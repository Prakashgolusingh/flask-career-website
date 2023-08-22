from sqlalchemy import create_engine,text
import os
# pymssql
#dialect+driver://username:password@host:port/database
#dialect+driver://username:password@host/database_name

#acessing secret value of key db_connect_string through os module.
db_connect_string = os.environ['db_connect_string']

# ssl secure connection
engine = create_engine(db_connect_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    list = []
    for row in result.mappings().all():
      list.append(dict(row))
  return list

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), {'val' : id}).mappings().all()
    if(len(result) == 0):
      return None
    else:
      return dict(result[0])




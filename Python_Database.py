#mysql , oracle, mongodb
#sqlconnector,cx_oracle , pymongo

import sqlite3
db_connection = sqlite3.connect('virat.db')
query = """create table student ("name" text , "score" int)"""
db_execution = db_connection.execute(query)
db_connection.commit()  #important statement 
db_connection.close()   #important statement 


##import sqlite3
##try:
##    
##   db_connection = sqlite3.connect('jayesh.db')
##   query = """create table staff ("name" text , "score" int)"""
##   db_execution = db_connection.execcute(query)
##
##except Exception as Ex:
##
##    print(Ex)
##
##finally:
##
##    db_connection.commit()  #important statement 
##    db_connection.close()   #important statement 
##
##

# DDl , DML (query catogeries )



import sqlite3
##try:
##    
##   db_connection = sqlite3.connect('jayesh.db')
##   #query = """create table staff ("name" text , "score" int)"""
##   #query = """ insert into student (name , score) values ('kohli',44) """
##   query = """select * from student"""
##   db_execution = db_connection.execute(query)
##   print(db_execution)
##   output = db_execution.fetchall()  #for printing output
##   print(output)
##
##except Exception as Ex:
##
##    print(Ex)
##
##finally:
##
##    db_connection.commit()  #important statement 
##    db_connection.close()   #important statement 
##

##def My_DB_Execution(query , db):
##    
##   try:
##    
##      db_connection = sqlite3.connect('jayesh.db')
##      db_execution = db_connection.execute(query)
##      output = db_execution.fetchall()  #for printing output
##      return output
##    
##
##    except Exception as Ex:
##        print(Ex)
##
##    finally:
##        db_connection.commit()  #important statement 
##        db_connection.close()   #important statement 
##
##query = """select * from student"""
##output = My_DB_Execution (query , 'jayesh.db')
##print(output)


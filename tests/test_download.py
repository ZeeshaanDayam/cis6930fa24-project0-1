import pytest
import sys
import io
from project0 import main

db=None
resp=None
data=[]
url="https://www.normanok.gov/sites/default/files/documents/2024-08/2024-08-01_daily_incident_summary.pdf"


def test_fetchPDFData():
    global resp,url

    try:
        resp=main.fetchPDFData(url)

        if resp:
            assert True
        else:
            assert False
    except Exception as e:
        print("Error while fetching data from URL: "+str(e),file=sys.stderr)
        assert False

def test_extractPDFData():
    global resp,data

    try:
        data=main.extractPDFData(resp)
        for row in data:
            if len(row) != 5:
                assert False
        assert True
    except Exception as e:
        print("Error while extracting and formatting data: "+str(e),file=sys.stderr)
        assert False

def findTable(db,table_name):
    cur=db.cursor()
    res=cur.execute("SELECT name FROM sqlite_master")
    if table_name in res.fetchone():
        return True
    else:
        return False

def test_createdb():
    global db

    try:
        db=main.createdb()
        if db:
            assert findTable(db,"incidents")
        else:
            assert False
    except Exception as e:
        print("Error while creating the database: "+str(e),file=sys.stderr)
        assert False

def checkDbData(db):
    cur=db.cursor()

    res=cur.execute("SELECT * FROM incidents")

    if res.fetchall():
        return True
    else:
        return False

def test_populatedb():
    global data,db

    try:
        main.populatedb(data,db)
        assert checkDbData(db)
    except Exception as e:
        print("Error while inserting data in database: "+str(e),file=sys.stderr)
        assert False

def checkOutput(func,*args,**kwargs):
    #create a String IO
    captured_output=io.StringIO()
    #save the current stdout
    old_stdout=sys.stdout
    #redirect stdout to out StringIO object
    sys.stdout=captured_output

    try:
        func(*args,**kwargs)

        output=captured_output.getvalue()
    finally:
        sys.stdout=old_stdout

    if output:
        return True
    else:
        return False

def test_status():
    global db

    try:
        assert checkOutput(main.status,db)
    except Exception as e:
        print("Error while fetching and printing data: "+str(e),file=sys.stderr)
        assert False










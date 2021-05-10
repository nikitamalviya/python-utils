# linux
server = 'server.domain.local' #'localhost'
database = 'databasename'
port = 1433
password = 'Password'
username = 'SA'

cnxn = pyodbc.connect('DRIVER={FreeTDS};SERVER=server.domain.local;PORT=1433;UID=DOMAIN\user;PWD=mypassword;DATABASE=mydatabasename;UseNTLMv2=yes;TDS_Version=8.0;Trusted_Domain=domain.local;')

# windows
server = 'SQL_SERVER'
database = 'db_name'
username = 'admin'
password = 'pwd'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect(f"DRIVER={drivername}"+';SERVER='+server+';DATABASE='+database, trusted_connection='yes')


# insert into db 
try:
    cursor_custom = cnxn.cursor()
    now = datetime.datetime.now()
    createddate = now.strftime('%Y-%m-%d %H:%M:%S')
    res = cursor_custom.execute("INSERT INTO aadhaarocr (applicationnumber,clienttype,gender, dob, fathername, name, address, createddate) values (?,?,?,?,?,?,?,?)",
        applicationnumber, "pred", aadhaarres["gender"], aadhaarres["dob"], aadhaarres["fathername"], aadhaarres["name"], aadhaarres["address"], createddate)
    print("res : ", res)
    cnxn.commit()
    cursor_custom.close()
except Exception as ex:
    print("Exception : ", ex, sys.exc_info()[-1].tb_lineno)


# connect to mysql linux using cmd
sqlcmd -S localhost -U SA -P password

# execute sql script
mysql -u username -p databasename < database.sql

# note : mysqldump is a command-line utility that is used to generate the logical backup of the MySQL database

# backup of ALL DATABASES within MySQL server
mysqldump -u root -p –all-databases > C:\MySQLBackup\all_databases_20200424.sql

# backup of whole DATABASE
mysqldump -u root -p databasename > C:\MySQLBackup\mydatabase.sql

# backup of a TABLE in database 
mysqldump -u root -p –databases databasename tablename > C:\MySQLBackup\dbname_tablename_20200424.sql

# backup of a database WITHOUT DATA 
mysqldump -u root -p –no-data database_name > C:\MySQLBackup\sakila_objects_definition_20200424.sql



# USE THE ABOVE SCRIPTS
drop database databasename;
mysql > create databasename tablename;

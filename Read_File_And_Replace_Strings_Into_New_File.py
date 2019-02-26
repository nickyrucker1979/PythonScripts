# Example with Canvas DDL to Exasol DDL Conversions

filename = 'canvas_ddl.txt'
newfilename = 'canvas_ddl_clean.txt'

schema = 'CANVAS_DATA_STG.'

# Read in the file
with open(filename, 'r') as file :
  filedata = file.read()

# Create Tables ddl
# filedata = filedata.replace('DROP TABLE', '# DROP TABLE')
filedata = filedata.replace('CREATE TABLE', 'CREATE OR REPLACE TABLE')
filedata = filedata.replace('TABLE ', 'TABLE ' + schema)

# Update datatypes to Exasol datatypes
filedata = filedata.replace(' TEXT', ' VARCHAR(50000)')
filedata = filedata.replace(' BIGINT', ' DECIMAL(18,0)')
filedata = filedata.replace(' FLOAT', ' DECIMAL(18,3)')
filedata = filedata.replace(' INTEGER', ' DECIMAL(18,0)')

# Update fieldnames
filedata = filedata.replace('position ', 'field_position ')
filedata = filedata.replace('generated ', 'field_generated ')
filedata = filedata.replace('date TIMESTAMP', 'field_date TIMESTAMP')
filedata = filedata.replace('timestamp TIMESTAMP', 'field_timestamp TIMESTAMP')

# Write the file out again
with open(filename, 'w') as file:
  file.write(filedata)

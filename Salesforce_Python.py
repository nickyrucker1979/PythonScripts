from simple_salesforce import Salesforce
import requests

session = requests.Session()
sf = Salesforce(
    username='',
    password='',
    security_token='',
    domain='test',
    session=session)

test_qry = sf.query("SELECT Id, Email from Contact where LastName = 'WiemeierTEST1'")
print(test_qry)

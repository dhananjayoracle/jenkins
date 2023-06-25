import jenkins
import json
import os


host='http://localhost:8080'
username='Dhananjay'
password='11140211df0da837b9dca5dac1ca0f4841'
server=jenkins.Jenkins(host,username=username,password=password,timeout=10)

# user=server.get_whoami()
# print(user['id'])

jobs=server.get_all_jobs()
print(jobs)




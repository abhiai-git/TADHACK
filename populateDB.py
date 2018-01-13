#!/usr/bin/python

from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import pandas as pd

def main():
    collection = MongoClient('127.0.0.1',27017)["foreseeing"]["users"]

    df = pd.read_csv("userdata.csv")
    for index, row in df.iterrows():
        user = row['Username']
        employeeid =row['EmployeeID']
        image_url =row["Image_url"]
        role ="manager"
        domain =row['Role']
        company=row['Hospital']
        active="true"
        validity="01/12/2016"
        email =row["Email"]
        phone=row["Mobile"]
        name=row["Name"]
        pass_hash = generate_password_hash(row['Password'], method='pbkdf2:sha256')
    # Connect to the DB
    # collection = MongoClient('127.0.0.1',27017)["foreseeing"]["users"]

    # # Ask for data to store
    # user = "abhishek"
    # password = "abhishek"
    # role="manager"
    # domain="Neurologits"
    # name="Abhishek Bhardwaj"

    # email="abhishekbhardwaj13506@gmail.com"
    # validity="01/12/2016"
    # active="true"

    # pass_hash = generate_password_hash(password, method='pbkdf2:sha256')
    # phone=""
    # # Insert the user in the DB
        try:
            collection.insert({"_id": user, "password": pass_hash,"role":role,"name":name,"email":email,"validity":validity,"status":active,'phone':phone,'company':company,'image_url':image_url,'domain':domain,'employeeid':employeeid})
            print "User created."
        except DuplicateKeyError:
            print "User already present in DB."


if __name__ == '__main__':
    main()

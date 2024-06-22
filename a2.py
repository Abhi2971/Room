import pyautogui
import time

commands = [
    ['show dbs'],
    ['use students'],
    ['db.createCollection("info")'],
    ['show dbs'],
    ['show collections'],
    ['db.info.insertMany([{name:"abhi",mobile:9766502971,email:"abhishelke297127@gmail.com",gender:"m",percentage:90},{name:"Ganesh",mobile:7447823511,email:"gsnesh297127@gmail.com",gender:"f",percentage:42},{name:"Hemant",mobile:9834428049,email:"hem420480@gmail.com",gender:"f",percentage:45},{name:"Sunil",mobile:8595746524,email:"sunil5125@gmail.com",gender:"f",percentage:35},{name:"Abhishek",mobile:9766502971,email:"abhishelke2971@gmail.com",gender:"m",percentage:95}])'],
    ['db.info.find()'],
    ['db.info.findOne({name:"abhi"})'],
    ['db.info.find({name:"abhi"})'],
    ['db.info.find({name:"Abhi"})'],
    ['db.info.updateOne({name:"Ganesh"},{$set:{gender:"m"}})'],
    ['db.info.updateOne({name:"Hemant"},{$set:{gender:"m"}})'],
    ['db.info.find()'],
    ['db.info.updateOne({name:"Hemant"},{$set:{gender:"m"}})'],
    ['db.info.find()'],
    ['db.info.find({},{name:1,mobile:1})']
]

time.sleep(4) 

for row in commands:
    for index, element in enumerate(row):
       for ab in element:
           pyautogui.typewrite(ab)
    pyautogui.press("enter")
    time.sleep(4) 
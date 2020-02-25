# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 11:54:09 2019

@author: zyy19
"""
from flask import Flask, render_template, request, jsonify
import random
import string
import time

#Collaborators: Qiqi Wang, Wenzhe Liu
###################################################
# Please change localhost to you local host address
###################################################
localhost = "http://127.0.0.1:5000" 

app = Flask(__name__)
idArr = []
tokenDic = {}
tokenRoom = {}
chatData = {}
inviteTokenDic = {}
inviteTokenRoom = {}
numPeopleInChatroom = {}

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html', Localhost = localhost)

@app.route('/create', methods=['POST'])
def create_chat_room():
    username = request.form.get('username')
    ##create chat_id
    numChatRoom = len(idArr)
    idStr = str(numChatRoom+1)
    idArr.append(idStr)
    ##session token
    token = randomString(15)
    tokenDic[token] = time.time()
    tokenRoom[token] = idStr
    
    return render_template('info.html', Chat_ID = idStr, Session_Token = token,
                           Username = username, Localhost = localhost)

@app.route('/1', methods=['GET', 'POST'])
@app.route('/2', methods=['GET', 'POST'])
@app.route('/3', methods=['GET', 'POST'])
@app.route('/4', methods=['GET', 'POST'])
@app.route('/5', methods=['GET', 'POST'])
@app.route('/6', methods=['GET', 'POST'])
@app.route('/7', methods=['GET', 'POST'])
@app.route('/8', methods=['GET', 'POST'])
@app.route('/9', methods=['GET', 'POST'])
@app.route('/10', methods=['GET', 'POST'])
@app.route('/11', methods=['GET', 'POST'])
@app.route('/12', methods=['GET', 'POST'])
@app.route('/13', methods=['GET', 'POST'])
@app.route('/14', methods=['GET', 'POST'])
@app.route('/15', methods=['GET', 'POST'])
@app.route('/16', methods=['GET', 'POST'])
@app.route('/17', methods=['GET', 'POST'])
@app.route('/18', methods=['GET', 'POST'])
@app.route('/19', methods=['GET', 'POST'])
@app.route('/20', methods=['GET', 'POST'])
def get_chatroom():
    if request.method == 'GET':
        url = request.path
        data = url.split("/")
        idStr = data[-1]
        if idStr not in chatData:
            chatData[idStr] = []
            numPeopleInChatroom[idStr] = 1
        return render_template('chat_room.html', Chat_ID = idStr, 
                               numPeople = numPeopleInChatroom[idStr], Localhost = localhost)
    else:
        message = str(request.headers.get('message'))
        chat_id = str(request.headers.get('Chat_ID'))
        chatData[chat_id].append(message)
        return ""

@app.route('/data', methods=['POST'])
def getData():
    token = request.headers.get('token')
    chat_id = request.headers.get('chat_id')
    if str(token) in tokenDic:
        if time.time() - tokenDic[str(token)] > 6*3600: #expire in 6 hours
            del tokenRoom[str(token)]
        elif tokenRoom[str(token)] == str(chat_id):
            return "match"
        
    return "unmatch"

@app.route('/updateMessage', methods=['GET'])
def update():
    #token = request.headers.get('token')
    chat_id = str(request.headers.get('Chat_ID'))
    if chat_id != "null":
        return jsonify(chatData[chat_id])

@app.route('/<chat_id>/invite', methods=['GET'])
def invite(chat_id):
    return render_template('invite.html', Chat_ID = chat_id, Localhost = localhost)


@app.route('/<chat_id>/invite', methods=['POST'])
def inviteData(chat_id):
    #record number of people
    if numPeopleInChatroom[chat_id] >= 6:
        return localhost + "/create"     
    numPeopleInChatroom[chat_id] += 1   
    token = request.headers.get('token')
    username = request.headers.get('username')
    if str(token) in tokenDic:
        if time.time() - tokenDic[str(token)] > 6*3600: #expire in 6 hours
            del tokenRoom[str(token)]
        elif tokenRoom[str(token)] == str(chat_id):
            inviteToken = randomString(15)
            inviteToken += "_" + chat_id + "_" + username
            inviteTokenDic[inviteToken] = "time"
            inviteTokenRoom[inviteToken] = chat_id
            return localhost + "/inviting/" + inviteToken
    return "Fail"
    
@app.route('/inviting/<inviteToken>', methods=['GET'])
def inviting(inviteToken):
    if inviteToken in inviteTokenDic:
        data = inviteToken.split("_")
        username = data[-1]
        chat_id = data[-2]
        ##session token
        token = randomString(15)
        tokenDic[token] = time.time()
        tokenRoom[token] = chat_id
        
        return render_template('info.html', Chat_ID = chat_id, Session_Token = token, 
                               Username = username, Localhost = localhost)
        
if __name__ == '__main__':
    app.run()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
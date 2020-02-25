from flask import Flask, request, jsonify
#from functools import wraps
import random
import string
import time 

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

localhost = "http://127.0.0.1:5000" 

chat_idArr = []
tokenDic = {}
tokenRoom = {}
inviteTokenDic = {}
inviteTokenRoom = {}
chatData = {}

def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@app.route('/')
@app.route('/chat/<int:chat_id>')
def index(chat_id=None):
    return app.send_static_file('index.html')


# -------------------------------- API ROUTES ----------------------------------

@app.route('/api/create', methods=['POST'])
def create ():
    # TODO: create a chat data structure in global memory
    # TODO: also send a username
    username = request.headers.get('username')
    # create chat_id
    numChatRoom = len(chat_idArr)
    chat_id = str(numChatRoom+1)
    chat_idArr.append(chat_id)
    # session token
    token = randomString(15)
    tokenDic[token] = time.time()
    tokenRoom[token] = chat_id
    # invite token
    inviteToken = randomString(15)
    inviteToken += "_" + chat_id + "_" + username
    inviteTokenDic[inviteToken] = "time"
    inviteTokenRoom[inviteToken] = chat_id
    # chat data: [magic link, number of people]
    chatData[chat_id] = [localhost + "/?magic_key=" + inviteToken, 1]

    return {
        "Localhost": localhost,
        "chat_id": chat_id,
        "username":username,
        "session_token": token,
        "magic_invite_link": localhost + "/?magic_key=" + inviteToken,
        "num_people": chatData[chat_id][1]
    }
    
@app.route('/checkAccess', methods=['POST'])
def getData():
    token = request.headers.get('token')
    chat_id = request.headers.get('chat_id')
    if str(token) in tokenDic:
        if time.time() - tokenDic[str(token)] > 6*3600: #expire in 6 hours
            del tokenRoom[str(token)]
        elif tokenRoom[str(token)] == str(chat_id):
            return "match"
        
    return "unmatch"

@app.route('/api/authenticate', methods=['POST'])
def authenticate():
    # TODO: check if the request body contains a chat_id and the correct magic_key for that chat
    # TODO: also send a username
    invite_token = str(request.headers.get('invite_token'))
    chat_id = str(request.headers.get('chat_id'))
    magic_link = chatData[chat_id][0]
    authToken = magic_link.split("magic_key=")[1]
    if authToken == invite_token:
        if chatData[chat_id][1] >= 6: # up to 6 people
            return "Full"
        token = randomString(15)
        tokenDic[token] = time.time()
        tokenRoom[token] = chat_id
        
        return {"session_token": token}
    else:
        return "Fail"

@app.route('/api/messages', methods=['GET', 'POST'])
def messages ():
    # TODO: check if the request body contains a chat_id and valid session token for that chat
    if request.method == 'POST':
        # TODO: add the message
        message = str(request.headers.get('message'))
        chat_id = str(request.headers.get('Chat_ID'))
        chatData[chat_id].append(message)
        return ""

    chat_id = str(request.headers.get('Chat_ID'))
    if chat_id != "null":
        return jsonify(chatData[chat_id])
    
@app.route('/api/invite_create', methods=['POST'])
def invite_create ():
    username = str(request.headers.get('username'))
    chat_id = str(request.headers.get('chat_id'))
    chatData[chat_id][1] += 1

    return {
        "username":username,
        "magic_invite_link": chatData[chat_id][0],
        "num_people": chatData[chat_id][1]
    }

    
    
if __name__ == '__main__':
    app.run()

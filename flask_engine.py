
from flask import Flask, render_template
from flask_socketio import SocketIO
import json
import time
import subprocess 
import os
import psutil

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.route("/killswitch")
def killswitch():
    find_and_kill_ProcessIdByName("python") #kills all the previous procceses



@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):

  
    import json

    print('received my event: ' + str(json))
    while(True):
        time.sleep(3)
        #here we need to set up a subprocess which keeps listeninig and returns only when something meaning full is said
        print("Subprocess returned with a status call number:",subprocess.call(['python', 'nlp_engine.py']))
        #using a subprocess as we will contonue to run this script in the background all the time in the future      
        
        #let's open the file and read something
        buffer_file = open("buffer.txt","r")
        data_read  = buffer_file.read()
        print("the data read from the file was:", data_read)
        data = {'user_name': 'Server', 'message': str(data_read)}
        data = json.dumps(data)
        socketio.emit('my response', data, callback=messageReceived)

def find_and_kill_ProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''

    listOfProcessObjects = []

    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
            # Check if process name contains the given name string.
            if processName.lower() in pinfo['name'].lower() :
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
            pass

    currentId = os.getpid()
    # Find PIDs od all the running instances of process that contains 'chrome' in it's name

    if len(listOfProcessObjects) > 0:
        # print('Process Exists | PID and other details are')
        for elem in listOfProcessObjects:
            processID = elem['pid']
            # if(int(processID)!=currentId):
            try:
                os.system("kill -9 {}".format(processID))
            except:
                pass


if __name__ == '__main__':
    socketio.run(app, debug=True)

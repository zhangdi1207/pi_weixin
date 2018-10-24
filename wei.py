import itchat
controlMsg='1122'

def dosth(ctrlType):
    if ctrlType=='1':
        print('one')
    elif ctrlType=='2':
        print('two')
    else:
        print('not in the list')

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    if msg.text[:len(controlMsg)]==controlMsg:
        ctrlType=msg.text[len(controlMsg):]
        dosth(ctrlType)
        return 'get Message: ' + ctrlType
itchat.auto_login()
itchat.run()

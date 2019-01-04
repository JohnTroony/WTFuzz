from sulley import *

s_initialize("TFTP")

# head
s_static("\x00\x01")
s_string("test")
s_static("\x00netascii\x00")
s_static("\r\n")


# fuzz target (with IP) 
sess = sessions.session(session_filename="tftp.session",proto="udp")
target = sessions.target("192.168.56.101",69)
sess.add_target(target)
sess.connect(s_get("TFTP"))
sess.fuzz()




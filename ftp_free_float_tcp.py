from sulley import *

def banner(sock):
	sock.recv(1024)


s_initialize("FFLOAT_FTP")

# User
s_static("USER ")
s_string("test")
s_static("\r\n")

# Password
s_static("PASS ")
s_string("test")
s_static("\r\n")



# fuzz target (with IP) 
sess = sessions.session(session_filename="free_ftp.session",proto="tcp")
target = sessions.target("127.0.0.1",21)
target.netmon = pedrpc.client("127.0.0.1",26001)
target.procmon = pedrpc.client("127.0.0.1",26002)
target.procmon_options = {
"pro_name":"ftpserver.exe",
"start_comands":["C:\Documents and Settings\Troony\Desktop\ftpserver.exe"],
}

sess.pre_send = banner
sess.connect(s_get("FFLOAT_FTP"))
sess.add_target(target)
sess.fuzz()




"""*******************************************************************************************************

This script provide ssh ping commands for DSC.
1. ssh_long_ping(hostname,username,password,sourceip,destinationip,time_mins)
2. ssh_onetime_ping(hostname,username,password,sourceip,destinationip)

Before using the script below, please first do:  pip install paramiko

Author: Jason Qin
Version: 2018.04.17

*******************************************************************************************************"""

import paramiko
from pexpect import popen_spawn
import pexpect, pexpect.popen_spawn
import getpass, os
import time


"""****************************************************************************************************"""
"""***************************             ssh long ping             **********************************"""
"""****************************************************************************************************"""

def ssh_long_ping(hostname,username,password,sourceip,destinationip,time_mins):

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=hostname, port=22, username=username, password=password)

	#execute command
	pingtime=time_mins*60
	#ping_result.log is saved in your account home folder
	cmd="ping -I "+ sourceip  + " "+ destinationip + " -s1472 -c " + str(pingtime) + """ | awk '{print $0"\\t"  strftime("%c",systime())} '"""+" > ping_result.log &"
	
	print(cmd)
	ssh.exec_command(cmd)

	#close the connection
	ssh.close()

#ssh_long_ping("10.162.28.187","g800472","Gaoding5658$","173.209.220.115","173.209.215.102",3)


"""****************************************************************************************************"""
"""***************************            ssh ping onetime           **********************************"""
"""****************************************************************************************************"""

def ssh_onetime_ping(hostname,username,password,cmd):

	#paramiko.util.log_to_file('paramiko.log')
	
	#creat SSH object
	ssh = paramiko.SSHClient()

	#skip key
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	#connect to DSC
	ssh.connect(hostname=hostname, port=22, username=username, password=password)
	#stdin.write("Y")

	#execute command
	stdin, stdout, stderr = ssh.exec_command(cmd)
	
	result=[]
	return stdout.readlines()
	#for std in stdout.readlines():
	#	print(std.strip())
	#print(std.strip())
	#return result
	#print(result)

	for std in stderr.readlines():
		#print(std.strip())
		result.append(std.strip())
	return result
	#print(result)

	#close the connection
	ssh.close()

#ssh_onetime_ping("10.162.28.187","g800472","Python666$","ping -I 173.209.220.115 111.71.235.1 -s1472 -c3")




"""****************************************************************************************************"""
"""***************************            ssh jump server commands           **********************************"""
"""****************************************************************************************************"""

"""def ssh_jump_server_cmd(jump_server_ip,username,password,command):

	ssh_newkey = 'Are you sure you want to continue connecting'
	#child = pexpect.popen_spawn.PopenSpawn('ssh -l %s %s %s' %(username, jump_server_ip, command))
	child = pexpect.popen_spawn.PopenSpawn('ssh '+ username+'@'+jump_server_ip)
	#command='ssh '+ username+'@'+jump_server_ip
	#print(command)
	#child = pexpect.popen_spawn.PopenSpawn(command)
	#fout = open('mylog.txt','w')
	#child.logfile = fout
	i = child.expect([pexpect.EOF,pexpect.TIMEOUT, ssh_newkey, 'password: '])
	
	if i == 0:
		print('Jason, EoF met')
		print(child.before)
		print(child.after)
	if i == 1: 
		print('ERROR!')
		print('SSH could not login. Here is what SSH said:')
		print(child.before, child.after)
		return None
	if i == 2: 
		child.sendline ('yes')
		child.expect ('password:')
	#child.sendline(password)
	#fout.close()
	child.sendline('Python666$')
	child.sendline('show route 223.224.118.49')
	child.expect (pexpect.EOF) 
	print(child.before)
	print(child.after)


#ssh_jump_server_cmd("10.12.7.16","g800472","Python666$","pwd")
#ssh_jump_server_cmd("10.162.28.187","g800472","Python666$","pwd")"""

def ssh_jump_server_cmd(hostname,username,password,cmd):

	#trans = paramiko.Transport(hostname, 22)
	#trans.connect(username=username,password=password)
	#paramiko.util.log_to_file('paramiko.log')
	
	#creat SSH object
	ssh = paramiko.SSHClient()
	#ssh._transport = trans



	#skip key
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	#connect to DSC
	ssh.connect(hostname=hostname, port=22, username=username, password=password)

	chan=ssh.invoke_shell()
	chan.send('ssh r003-sng2-ngn'+'\n')
	res=chan.recv(65535)
	time.sleep(4)
	chan.send(password+'\n')
	time.sleep(2)
	res=chan.recv(65535)
	chan.send(cmd+'\n')
	time.sleep(2)

	result = ''
	while True:
		time.sleep(2)
		res = chan.recv(65535).decode('utf8')
		result = res
		if result:
			results=result.strip('\n')
			if 'UTC' in results:
				return results.split(' UTC')[1].strip()
			else:
				return results

		if res.endswith('> '):
			break
	
	#execute command
	#stdin, stdout, stderr =ssh.exec_command(cmd)"""
	#stdin, stdout, stderr =ssh.exec_command('pwd;ssh r003-sng2-ngn',get_pty=True)
	#stdin, stdout, stderr =ssh.exec_command('pwd;ls',get_pty=True)
	#stdin.write(password+'\n')
	
	#stdin, stdout, stderr = ssh.exec_command('show route 223.224.40.16')
	#stdin, stdout, stderr = ssh.exec_command('pwd')
	"""result=['1']
	
	for std in stdout.readlines():
		print(std.strip())
	return stdout.readlines()

		for std in stderr.readlines():
		#print(std.strip())
		result.append(std.strip())
	return stderr.readlines()
	#print(result)

	#close the connection"""
	ssh.close()

if __name__=="__main__": 
	print('before')
	results=ssh_jump_server_cmd("10.12.7.16","g800472","Python666$","show route 131.166.129.151")
	print('after')
	print('results: ')
	print(results)

	"""result_final=""
	for result in results:
		result_final=result_final+result
	print("result_final:"+result_final)"""






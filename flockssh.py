#flockssh 
#v0.0 16-05-18 master@owlh.net

import paramiko
import flocklogger

flogger = flocklogger.flocklogger

def run_cmd(cmd, ssh):
    try:
        stdin, stdout, stderr = ssh.exec_command(cmd)

        for l in stdout :
            print("stdout : %s" % l.strip())

        for l in stderr:
            print("stderr : %s" % l.strip())
    except Exception as inst:
        print "Oops!  there was a problem: ", inst
        flogger("Oops!  there was a problem: %s" % str(inst))
        return False

def check_owl_alive(owl):
    owl_user="jose"
    owl_pass="polilla"
    owl_ip=owl["ip"]
    flogger("check if owl %s (%s) is alive" % (owl["name"], owl["ip"]))

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
    try:
        ssh.connect(owl_ip, username=owl_user, key_filename='/Users/jizquierdo/.ssh/owl')
        #ssh.connect(owl_ip, username=owl_user, password=owl_pass)
    except Exception as inst:
        print "Oops!  there was a problem: ", inst
        flogger("Oops!  there was a problem: %s" % str(inst))
        return False
    cmd='pwd; ls; date'
    print('\n test 1\n cmd %s\n' % cmd)
    run_cmd(cmd, ssh)

def nothing():
    bastion_ip='ip'     # you have to edit and provide valid IP address 
    bastion_pass='pass' # you have to edit it and provide valid password 

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
    ssh.connect(bastion_ip, username='root', password=bastion_pass)

    chan = ssh.invoke_shell()

    # other cloud server 
    priv_ip='private_ip'  # you have to edit it and provide valid private IP 10.176.0.0/12
    passw='pass'          # valid password 

    test_script='/root/check_rackconnect.sh'

    cmd='pwd; ls; date'
    print('\n test 1\n cmd %s\n' % cmd)
    run_cmd(cmd)

    scp_opt=""
    cmd='scp -q ' + scp_opt + ' -o NumberOfPasswordPrompts=1 -o StrictHostKeyChecking=no %s root@%s:~/; echo $? done.' % ( test_script, priv_ip )
    print('\n test 2\n cmd %s\n' % cmd)
    run_cmd(cmd)

    scp_opt="-v"
    cmd='scp -q ' + scp_opt + ' -o NumberOfPasswordPrompts=1 -o StrictHostKeyChecking=no %s root@%s:~/; echo $? done.' % ( test_script, priv_ip )
    print('\n test 3\n cmd %s\n' % cmd)
    run_cmd(cmd)
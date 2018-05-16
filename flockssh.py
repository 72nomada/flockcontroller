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
        flogger("Oops!  there was a problem: %s" % str(inst),"WARNING")
        return False

def owl_connect(owl):
    owl_user="jose"
    owl_key="/Users/jizquierdo/.ssh/owl"
    owl_ip=owl["ip"]

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
    try:
        ssh.connect(owl_ip, username=owl_user, key_filename=owl_key)
    except Exception as inst:
        flogger("Oops!  there was a problem: %s" % str(inst),"WARNING")
        return False, ""
    
    return True, ssh

def check_owl_alive(owl):
    flogger("check if owl %s (%s) is alive" % (owl["name"], owl["ip"]))
    alive, ssh = owl_connect(owl)
    if alive:
        cmd='pwd; ls; date'
        print('\n test 1\n cmd %s\n' % cmd)
        run_cmd(cmd, ssh)
        return True
    flogger("owl %s (%s) is not alive" % (owl["name"], owl["ip"]))
    return False

def nothing():
    scp_opt=""
    cmd='scp -q ' + scp_opt + ' -o NumberOfPasswordPrompts=1 -o StrictHostKeyChecking=no %s root@%s:~/; echo $? done.' % ( test_script, priv_ip )
    print('\n test 2\n cmd %s\n' % cmd)
    run_cmd(cmd)

    scp_opt="-v"
    cmd='scp -q ' + scp_opt + ' -o NumberOfPasswordPrompts=1 -o StrictHostKeyChecking=no %s root@%s:~/; echo $? done.' % ( test_script, priv_ip )
    print('\n test 3\n cmd %s\n' % cmd)
    run_cmd(cmd)
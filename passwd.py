#!/usr/bin/python

fich=open("/etc/passwd","r")
maquinas=fich.readlines()

for maquina in maquinas:
    user=maquina.split(':')[0]
    shell=maquina.split(':')[-1]
    print "user: " + user, " shell: " + shell,
print str(len(maquinas)) + " users."
fich.close()

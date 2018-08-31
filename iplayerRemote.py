#GET_IPLAYER DLZ QUEUER

#REMOTE SCRIPT

import os

_MY_SECRET_IP = os.environ.get('UK_IP')
_SCP_DESTINATION = '/Volumes/Gigantosaur/Media/iPlayer/'
_SCP_SOURCE = '''rsh='ssh -p22257 porter@%s/home/porter/iPlayer/''' % _MY_SECRET_IP

def cdRemoteDirectory(directory):
    os.chdir(directory)

def order66(theList):
    command = 'screen get_iplayer --get '
    for i in theList:
        command += '--url ' + i
    os.system(command)
        
    
def queue_and_download_programs():
    dlz_list = []
    i = 1
    print('''

************************************************************************************************
Welcome to the remote server, comrade.

Enter iPlayer URL to queue and hit enter to add to queue. Then:
- Type \'go\' to download all, then auto-synchronise this remote directory with your local one.
- Type \'skip\' to skip straight to synchronising remote and local directories.
************************************************************************************************

''')
    while True:
        dlz_url = input(str(i) +') >> ')
        if dlz_url.lower() == 'go':
            order66(dlz_list)
            return('All downloaded.')
        if dlz_url.lower() == 'skip':
            return('Downloads skipped.')
        else:
            dlz_list.append(dlz_url + ' ')
            i += 1


#### HERE WE GOOOOO!

cdRemoteDirectory('/home/porter/iplayer')
queue_and_download_programs()

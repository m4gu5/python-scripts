#!/usr/bin/python

# Author: @m4gu5
# Issues an Update command periodically for a BOINC project on a given host.
# This can be used to grab Workunits even if there are only very few available.
# Example usage:
# boincUpdate.py --host 192.168.2.5 --passwd 'notsosecurepassword' --project http://www.worldcommunitygrid.org

import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description='Periodically update a BOINC project')
parser.add_argument('--host', default='127.0.0.1', help='The host to contact (default: localhost)', type=str)
parser.add_argument('--passwd', default='""', help='The password of the BOINC instance (default: empty)', type=str)
parser.add_argument('--project', help='The URL of the project which should be queried', type=str, required=True)
parser.add_argument('--interval', default=120, help='Number of seconds to wait between each update request (default: 120)', type=int)
args = parser.parse_args()

host = args.host
passwd = args.passwd
project = args.project
interval = args.interval
query = True

while query:
    try:
        print('[' + time.strftime('%Y-%m-%d %H:%M:%S') + '] Updating ' + project + ' on host ' + host)
        p = subprocess.Popen(['boinccmd', '--host', host, '--passwd', passwd, '--project', project, 'update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        p.stdout.close()
        p.stderr.close()
        time.sleep(interval)
    except KeyboardInterrupt:
        query = False

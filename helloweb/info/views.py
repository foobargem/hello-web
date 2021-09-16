import socket
import subprocess
from django.shortcuts import render


def index(request):
    results = []

    cmd = ['printenv']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    results.append({
        'cmd': ' '.join(cmd),
        'stdout': stdout.decode(),
        'stderr': stderr.decode(),
    })

    cmd = ['cat', '/etc/resolv.conf']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    results.append({
        'cmd': ' '.join(cmd),
        'stdout': stdout.decode(),
        'stderr': stderr.decode(),
    })

    cmd = ['dig', 'rds.allu.dev']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    results.append({
        'cmd': ' '.join(cmd),
        'stdout': stdout.decode(),
        'stderr': stderr.decode(),
    })

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = sock.connect_ex(('ec.allu.dev', 6379))
    _stdout = 'not open'
    if res == 0:
        _stdout = 'open'
    sock.close()

    results.append({
        'cmd': 'telnet ec.allu.dev 6379',
        'stdout': _stdout,
        'stderr': '',
    })

    return render(request, 'info/index.html', {
        'results': results,
    })

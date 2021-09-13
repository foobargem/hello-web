import subprocess
from django.shortcuts import render


def index(request):
    results = []

    cmd = ['cat', '/etc/resolv.conf']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    results.append({
        'cmd': ' '.join(cmd),
        'stdout': stdout.decode(),
        'stderr': stderr.decode(),
    })

    cmd = ['dig', 'dev.allu']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()

    results.append({
        'cmd': ' '.join(cmd),
        'stdout': stdout.decode(),
        'stderr': stderr.decode(),
    })

    return render(request, 'info/index.html', {
        'results': results,
    })

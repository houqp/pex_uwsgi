import os
import sys


def activate_pex():
    entry_point = os.environ.get('UWSGI_PEX')
    if not entry_point:
        sys.stderr.write('couldnt determine pex from UWSGI_PEX environment variable, bailing!\n')
        sys.exit(1)

    sys.stderr.write('PEX bootstrap: entry_point=%s\n' % entry_point)

    sys.path[0] = os.path.abspath(sys.path[0])
    sys.path.insert(0, entry_point)
    sys.path.insert(0, os.path.abspath(os.path.join(entry_point, '.bootstrap')))

    from _pex.pex_bootstrapper import bootstrap_pex_env
    bootstrap_pex_env(entry_point)
    sys.stderr.write('PEX bootstrap: sys.path=%s\n\n' % sys.path)

activate_pex()

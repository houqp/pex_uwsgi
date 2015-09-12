import os
import copy
import sys


def activate_pex():
    entry_point = os.environ.get('UWSGI_PEX')
    if not entry_point:
        sys.stderr.write('couldnt determine pex from UWSGI_PEX environment variable, bailing!\n')
        sys.exit(1)

    sys.stderr.write('PEX bootstrap: entry_point=%s\n' % entry_point)

    cur_path = os.path.abspath(sys.path.pop(0))
    sys.path.insert(0, entry_point)
    sys.path.insert(0, os.path.abspath(os.path.join(entry_point, '.bootstrap')))
    old_sys_path = copy.copy(sys.path)

    from _pex.pex_bootstrapper import bootstrap_pex_env
    bootstrap_pex_env(entry_point)

    # move system path to the end
    sys.path = [p for p in sys.path if p not in old_sys_path]
    sys.path += old_sys_path
    # insert current working path so it's eaiser to hot patch app
    sys.path.insert(0, cur_path)
    sys.stderr.write('PEX bootstrap: sys.path=%s\n\n' % sys.path)

activate_pex()

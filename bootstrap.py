import os
import sys

def activate_pex():
  entry_point = os.environ.get('UWSGI_PEX')
  if not entry_point:
    sys.stderr.write('couldnt determine pex from UWSGI_PEX environment variable, bailing!\n')
    sys.exit(1)

  sys.stderr.write('entry_point=%s\n' % entry_point)

  sys.path[0] = os.path.abspath(sys.path[0])
  sys.path.insert(0, entry_point)
  sys.path.insert(0, os.path.abspath(os.path.join(entry_point, '.bootstrap')))

  from _pex import pex_bootstrapper
  from _pex.environment import PEXEnvironment
  from _pex.finders import register_finders
  from _pex.pex_info import PexInfo

  pex_bootstrapper.monkeypatch_build_zipmanifest()
  register_finders()

  pex_info = PexInfo.from_pex(entry_point)
  env = PEXEnvironment(entry_point, pex_info)
  working_set = env.activate()

  sys.stderr.write('sys.path=%s\n\n' % sys.path)

  return entry_point, pex_info, env, working_set

activate_pex()


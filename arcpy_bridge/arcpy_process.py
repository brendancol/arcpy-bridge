import os
import subprocess

def run_model(toolbox_path, model_name, model_args=[]):
    py = find_python_interpreter()
    print 'using python interpreter {}'.format(py)
    bridge = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'arcpy_bridge.py'))
    print 'using bridge file {}'.format(bridge)

    bridge_args = ','.join([str(a) for a in model_args])
    proc = subprocess.Popen([py, bridge,  'run_model', toolbox_path, model_name, bridge_args], stdout=subprocess.PIPE, shell=True)
    return proc.communicate()

def find_python_interpreter():
    for v in ['C:/', 'D:/']:
        for dirname, dirnames, filenames in os.walk(v):
            if 'arcgis10' in dirname:
                for f in filenames:
                    if 'python27.exe' in f:
                        return os.path.join(dirname, f)

    raise Exception('Unable to find ArcGIS python interpreter')

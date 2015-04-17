import os
import subprocess

def run_model(toolbox_path, model_name, model_args=None):
    py = find_python_interpreter()
    print 'using python interpreter {}'.format(py)
    bridge = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'arcpy_bridge.py')
    print 'using bridge file {}'.format(bridge)
    print model_args    
    bridge_args = model_args and ','.join([str(a) for a in model_args]) or model_args
    proc = subprocess.Popen([py, bridge, 'run_model', toolbox_path, model_name, bridge_args], stdout=subprocess.PIPE, shell=True)
    results, err = proc.communicate()
    return results, err

def find_python_interpreter(x64=True):

    install_hints = ['python27']

    if x64:
        install_hints.append('arcgisx6410.')
    else:
        install_hints.append('arcgis10.')

    for v in ['C:/', 'D:/']:
        
        if not os.path.exists(v):
            continue

        for dirname, dirnames, filenames in os.walk(v):
            dir_lower = dirname.lower()
            if all([s in dir_lower for s in install_hints]):
                for f in filenames:
                    print dirname, f
                    if 'python27.exe' in f.lower():
                        return os.path.join(dirname, f)
    raise Exception('Unable to find ArcGIS python interpreter')

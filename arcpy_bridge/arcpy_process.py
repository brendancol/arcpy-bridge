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

def find_python_interpreter(x64=False):

    if x64:
        arcpy_folder_start = 'arcgisx6410.'
    else:
        arcpy_folder_start = 'arcgis10.'

    for v in ['C:\\', 'D:\\']:
        
        if not os.path.exists(v):
            continue

        for dirname, dirnames, filenames in os.walk(v):
            if os.path.split(dirname)[1].lower().startswith(arcpy_folder_start):
                return os.path.join(dirname, 'python.exe')

    raise Exception('Unable to find ArcGIS python interpreter')

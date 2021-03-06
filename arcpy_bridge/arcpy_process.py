import os
import subprocess

def run_model(toolbox_path, model_name, model_args=None, interpreter=None):
    py = interpreter and interpreter or find_python_interpreter()
    bridge = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'arcpy_bridge.py')
    bridge_args = model_args and ','.join([str(a) for a in model_args]) or model_args
    proc = subprocess.Popen([py, bridge, 'run_model', toolbox_path, model_name, bridge_args], stdout=subprocess.PIPE, shell=True)
    results, err = proc.communicate()
    return results, err

def find_python_interpreter(x64=False):
    arcpy_folder_start = x64 and 'arcgisx6410.' or 'arcgis10.' 
    for v in ['C:\\', 'D:\\']:
        if not os.path.exists(v):
            continue
        for dirname, dirnames, filenames in os.walk(v):
            if 'Python27' in dirname and os.path.split(dirname)[1].lower().startswith(arcpy_folder_start):
                return os.path.join(dirname, 'python.exe')
    raise Exception('Unable to find ArcGIS python interpreter')

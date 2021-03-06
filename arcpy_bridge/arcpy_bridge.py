import os
import arcpy
import sys

def run_model(toolbox_path, model_name, model_args=None):
    print 'running model'
    toolbox_name = os.path.splitext(os.path.split(toolbox_path)[1])[0]
    model_args = model_args and model_args.split(',') or model_args
    arcpy.ImportToolbox(toolbox_path, toolbox_name)
    model_func = '{}_{}'.format(model_name, toolbox_name)
    print 'about to run model {}'.format(model_func)
    if model_args:
        return getattr(arcpy, model_func)(*model_args)
    else:
        return getattr(arcpy, model_func)()

def main():
    funcs = {}
    funcs['run_model'] = run_model
    bridge_func = sys.argv[1]
    bridge_args = sys.argv[2:]
    return funcs[bridge_func](*bridge_args)

if __name__ == '__main__':
    main()

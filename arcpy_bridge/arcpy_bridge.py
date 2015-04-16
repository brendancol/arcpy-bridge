
import os
import arcpy
import sys

def run_model(toolbox, model_label, model_name,  model_args):
    print 'running model'
    model_args = model_args.split(',')
    arcpy.ImportToolbox(toolbox, model_label)
    model_func = '{}_{}'.format(model_name, model_label)
    print 'about to run model {}'.format(model_func)
    return getattr(arcpy, model_func)(*model_args)

def main():
    bridge_func = sys.argv[1]
    bridge_args = sys.argv[2:]
    return locals()[bridge_func](*bridge_args)

if __name__ == '__main__':
    main()

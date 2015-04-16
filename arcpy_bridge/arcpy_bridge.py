
import os
import arcpy
import sys

def run_model(toolbox, model_name, model_args):
    model_args = model_args.split(',')
    arcpy.ImportToolbox(toolbox, model_name)
    return eetattr(arcpy, 'Model_' + model_name)(*model_args)

def main():
    bridge_func = sys.argv[1]
    bridge_args = sys.argv[2:]
    return locals()[bridge_func](*bridge_args)

if __name__ == '__main__':
    main()

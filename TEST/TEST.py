import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir =  os.path.dirname(current_dir)
API_dir = os.path.abspath(os.chdir(root_dir/API))

print(API_dir)
""" Module with configuration for Walker environment """

import os
import inspect

CURRENT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
os.sys.path.insert(0, PARENT_DIR)

MONITOR_PATH = '.\training\motor'
SUMMARY_DIR = '.\training\summary'

WALKER = "Walker2DBulletEnv-v0"
HALFCHEETAH = "HalfCheetahBulletEnv-v0"
HUMANOID = "HumanoidBulletEnv-v0"

MODEL = "human"
RENDER_ENV = False


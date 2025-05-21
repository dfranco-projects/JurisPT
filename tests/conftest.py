import sys
from os.path import abspath, dirname, join

# add the scripts directory to the Python path
scripts_dir = abspath(join(dirname(__file__), "..", "scripts"))
sys.path.insert(0, scripts_dir)
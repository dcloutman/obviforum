import sys, os
INTERP = '/path/to/your/local/python'
if sys.executable != INTERP:
    os.execl(INTERP, *sys.argv)
sys.path.append(os.getcwd())
from main import app as application

# Uncomment next two lines to enable debugging
# from werkzeug.debug import DebuggedApplication
# application = DebuggedApplication(application, evalex=True)

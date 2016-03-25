import os, sys

activate_this = os.path.join('/home/rogerhoward/.virtualenvs/funcaas/bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append('/var/www/funcaas.com')

from server import app as application
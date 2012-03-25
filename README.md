pyMonitor
=========

Periodically checks if a webserver is ON. It uses GTK widgets to display the status of each webpage on config.json.

![example](http://s16.postimage.org/pmqkley5x/py_Monitor.png)

Usage
-----

Just run pyMonitor.py and keep your eye on your widget bar. I added the ./pyMonitor.py to my xinitrc, but everytime I had to restart X for some reason, another pyMonitor would run in addition to the first. Using start.sh checks if there's already a pyMonitor running. Make sure you set your full path to the pyMonitor.py file inside start.sh.

> $ ./start.sh 

If there's already an instance of pyMonitor running, it will output:

> $ ./start.sh 
> There is already an instance of [FULL PATH]/pyMonitor.py running.

You can add this line inside your initialization script, such as initrc.

License
-------

pyMonitor is distributed in the public domain.
The three icons I added are part of the GTK project (http://www.gtk.org/), which is distributed under the GNU LGPL license (http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)

# [CG3002 Dance Dance Project](Docs/Handouts/CG3002-dance.pdf "CG3002 Embedded System Design Project")

## Main code

### Arduino Mega
1. [Arduino Code](Arduino_Code.ino "Arduino_Code.ino")  

### Raspberry Pi 3

1. [Recording raw data](Pi_1_Record_Raw_Data.py "Pi_1_Record_Raw_Data.py")  
2. [Compiling raw data collected - Modular](Pi_2_Compile_Raw_Data.py "Pi_2_Compile_Raw_Data.py")  
3. [Learn from raw data](Pi_3_Learn_From_Processed_Data.py "Pi_3_Learn_From_Processed_Data.py")  
4. [Main Code for Live Recognition](Pi_4_Live_Recognition.py "Pi_4_Live_Recognition.py")  

### Server

1. [Final evaluation server](final_eval_server.py "final_eval_server.py")  

## Setting up

### Windows
1. [GitKraken 3.2.2](https://www.gitkraken.com/)
2. [Anaconda 5.0.1](https://www.anaconda.com/download/)
    - Update: `conda update --all`
    - `conda install -c anaconda pyserial`
3. [RealVNC Viwer](https://www.realvnc.com/en/connect/download/viewer/)
    - Get the `Standalone EXE x64` if you do not wish to install
4. [Arduino IDE 1.8.5](https://www.arduino.cc/en/Main/Software)

### Raspberry Pi
1. [Noobs 2.4.4](https://www.raspberrypi.org/downloads/noobs/)
    - [Installation Guide](https://lifehacker.com/the-always-up-to-date-guide-to-setting-up-your-raspberr-1781419054)
2. Update system (use Terminal)
    - Fetch latest versions
        - `sudo apt-get update`
    - Download and update local versions
        - `sudo apt-get upgrade`
    - Install VNC Server for remote access [Source](https://www.raspberrypi.org/documentation/remote-access/vnc/)
        - `sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer`
    - Restart
        - `sudo reboot`
3. Update [Python](https://www.python.org/downloads/) and packages (Choose one)
    1. Python 3.6.3 (Will override terminal commands)
        - Download [Berryconda3-2.0.0-Linux-armv7l.sh](https://github.com/jjhelmus/berryconda) to desktop
        - `cd Desktop`
        - `sudo chmod +x Berryconda3-2.0.0-Linux-armv7l.sh` [Source](http://www.circuitbasics.com/how-to-write-and-run-a-shell-script-on-the-raspberry-pi/)
        - Double click file on desktop and `Execute in Terminal`
        - Follow instructions
        - `conda update --all` to update from Python 3.6.1 to Python 3.6.3 [Source](https://anaconda.org/anaconda/python)
        - `conda install -c anaconda pyserial`
        - `conda install pandas` to install numpy and pandas
        - `conda install scikit-learn`
        - `conda install pycrypto`
    2. Python 3.5.3-1
        - `apt-get install python3-pandas`
        - `sudo apt-get install python3-pip` [Source](https://www.raspberrypi.org/documentation/linux/software/python.md)
        - `pip3 install -U scikit-learn[alldeps]`
        - `pip3 install pyserial`
    3. Python 2.7.13-2
        - Install the Python basics
            - `sudo apt-get install build-essential python-dev python-distlib python-setuptools python-pip python-wheel libzmq-dev libgdal-dev`
        - Install pandas dependencies
            - `sudo apt-get install xsel xclip libxml2-dev libxslt-dev python-lxml python-h5py python-numexpr python-dateutil python-six python-tz python-bs4 python-html5lib python-openpyxl python-tables python-xlrd python-xlwt cython python-sqlalchemy python-xlsxwriter python-jinja2 python-boto python-gflags python-googleapi python-httplib2 python-zmq libspatialindex-dev`
            - `sudo pip install bottleneck rtree`
        - Install the scientific Python stack
            - `sudo apt-get install python-numpy python-matplotlib python-mpltoolkits.basemap python-scipy python-sklearn python-statsmodels python-pandas`
        - Install other useful packages
            - `sudo apt-get install python-requests python-pil python-scrapy python-geopy python-shapely python-pyproj`
            - `sudo pip install jupyter geopandas osmnx`
4. To run Python programs
    - First change directory to where program is located i.e. `cd Desktop`
    ```python
    pi@raspberrypi:~ $ python2
    Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
    [GCC 6.3.0 20170124] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    [1]+  Stopped                 python2
    pi@raspberrypi:~ $ python3.5
    Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
    [GCC 6.3.0 20170124] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    [2]+  Stopped                 python3.5
    pi@raspberrypi:~ $ python3.6
    Python 3.6.3 | packaged by rpi | (default, Oct  6 2017, 12:22:32) 
    [GCC 4.9.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    [3]+  Stopped                 python3.6
    pi@raspberrypi:~ $ python
    Python 3.6.3 | packaged by rpi | (default, Oct  6 2017, 12:22:32) 
    [GCC 4.9.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
    ``` 
    1. Python 3.6.3
        - `python filename.py`
        - or `python3 filename.py`
        - or `python3.6 filename.py`
    2. Python 3.5.3-1
        - `python3 filename.py`(if Python 3.6.3 not installed)
        - or `python3.5 filename.py`
    3. Python 2.7.13-2
        - `python filename.py` (if Python 3.6.3 not installed)
        - or `python2 filename.py`
        - or `python2.7 filename.py`
        - Notes:
          - In `joblib.dump()`, change parameter `protocol=2` i.e.
          ```python
          joblib.dump(rf_model, 'model_rf.pkl', protocol=2)

#### Useful Stuffs
- Check ip address
    - `sudo ifconfig`
- [.BASHRC AND .BASH_ALIASES](https://www.raspberrypi.org/documentation/linux/usage/bashrc.md)
    - i.e. `alias python=/usr/local/bin/python2.7` to reset `python` to use Python 2.7 [Source](https://stackoverflow.com/questions/19256127/two-versions-of-python-on-linux-how-to-make-2-7-the-default)
    - Check version locations with these commands (using Python 2.7.13 as example) [Source](https://stackoverflow.com/questions/6767283/find-where-python-is-installed-if-it-isnt-default-dir)
    ```python
    pi@raspberrypi:~ $ python2
    Python 2.7.13 (default, Jan 19 2017, 14:48:08)
    [GCC 6.3.0 20170124] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> sys.executable
    '/usr/bin/python2'
    >>> sys.exec_prefix
    '/usr'
    >>> print '\n'.join(sys.path)

    /usr/lib/python2.7
    /usr/lib/python2.7/plat-arm-linux-gnueabihf
    /usr/lib/python2.7/lib-tk
    /usr/lib/python2.7/lib-old
    /usr/lib/python2.7/lib-dynload
    /home/pi/.local/lib/python2.7/site-packages
    /usr/local/lib/python2.7/dist-packages
    /usr/lib/python2.7/dist-packages
    /usr/lib/python2.7/dist-packages/PILcompat
    /usr/lib/python2.7/dist-packages/gtk-2.0
    >>>
    ```
- Command to list history of apt-get [Source](https://askubuntu.com/questions/17012/is-it-possible-to-get-a-list-of-most-recently-installed-packages)
    - `grep " install " /var/log/apt/history.log`
- List the installed system packages and installed Python packages and dump them to files, just for reference
    - `dpkg -l > ~/Desktop/packages.list`
    - `pip freeze > ~/Desktop/pip-freeze-initial.list`
- [[Python-Dev] Benchmarks: Comparison between Python 2.7 and Python 3.6 performance](https://mail.python.org/pipermail/python-dev/2016-November/146800.html)
- [Old Google docs](https://docs.google.com/document/d/1n0aq0Fke1nN6KIOq7vN-SbGGLUNK3Z5TUAT3TFU51hQ/edit?usp=sharing)

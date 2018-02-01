# JestemGraczem.pl
[![Updates](https://pyup.io/repos/github/otlet/JestemGraczem.pl/shield.svg?token=bce824c2-2d11-467b-9aac-dd6ffd1c46db)](https://pyup.io/repos/github/otlet/JestemGraczem.pl/)
[![Python 3](https://pyup.io/repos/github/otlet/JestemGraczem.pl/python-3-shield.svg?token=bce824c2-2d11-467b-9aac-dd6ffd1c46db)](https://pyup.io/repos/github/otlet/JestemGraczem.pl/)
[![Build Status](https://img.shields.io/travis/otlet/JestemGraczem.pl/master.svg?branch=master)](https://travis-ci.org/otlet/JestemGraczem.pl)

Streaming player and something more (probably). We love coffee.

## DOCUMENTATION
Work in progress!

## INSTALL
* Prerequisites:
    * Python 3.6+
    * pip
    * VirtualEnv
    * PostgreSQL
    * Patients
* Installation:
    * `virtualenv ENV`
    * `./ENV/bin/activate`
    * `pip install -r requirements.txt`
    * Configure static file location in nginx/Apache/other config
    * `gunicorn --bind unix:{PROJECT_LOCATION}/jg.sock -w 3 --log-file - JestemGraczem.wsgi`
    * `Cry`
    
## CONTRIBUTING
You can help us with:
* Report bugs (issues)
* Fork, make something and try to merge
* Love us
    
## License
GNU AGPL 3.0

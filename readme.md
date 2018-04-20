You need to install selenium with chrome installed

https://www.seleniumhq.org/download/


The script uses python to fetch a series of random websites based on links.txt in the current working directory.

It will randomly pick a link from the list in links.txt, then pick a link on the website 5 times and repeat.






For Ubuntu:
===========

Included is the ubuntu dpkg --get-selections from my test machine

You will need selenium and chrome installed.  You will also need the chromedriver for selenium







For Windows:
============
`
Install chrome
`
python.27: https://www.python.org/downloads/

pip install -U selenium

Place selium chromedriver in folder with this script: https://sites.google.com/a/chromium.org/chromedriver/


For Both
========

The script occasional gets stuck with AJAX/continiously downloading website.  Scheduled task to kill the browse will fix. Run the killbrowser.sh/.bat once an hour or so.

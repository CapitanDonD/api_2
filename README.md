# Bitly url shorterer

This program allows you to make shorter links using the
Bitly service and watch the number of clicks on short links.

### How to install

For the program to work, you need a Bitly key. It can be obtained
on this site - bitly.com, by going to the site, register and the API item
will appear in the settings, after clicking on "Generate token". Then,
in the program folder, create a file called ".env". In it you need to
insert this:
```
BITLY_TOKEN="your token"
```

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### How to run
To run the program itself, you need to write the following command on the command line:
```
python main.py *your url or bitly*
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

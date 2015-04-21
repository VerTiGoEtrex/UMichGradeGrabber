UMichGradeGrabber
=================

Notifies you of updated grades

Requires Selenium (pip install selenium)

In command line: `python main.py UNIQNAME PW EMAIL_SENDER EMAIL_PW EMAIL_RECEIVER BROWSER_TYPE`
Replace the following parameters:
* `UNIQNAME` is your umich unique name
* `EMAIL_SENDER` is gmail account name (It must be a gmail-based address currently -- this includes UMich addresses)
* `EMAIL_RECEIVER` is the receiver of the notification
* `BROWSER_TYPE` is the type of browser to use ('f' for firefox, 'c' for chrome)

You can test that it's setup correctly by modifying "oldtranscript.txt" and running the script. You should receive an e-mail containing a diff between your old and new transcripts.

You will receive an e-mail looking like this. Have a good laugh at my garbage GPA too ;)

![Example Email](https://raw.githubusercontent.com/vertigoetrex/umichgradegrabber/master/readmeresources/emailExample.png "Example E-mail")

Improved from here: https://github.com/ethanjyx/wolverineGradeGraber

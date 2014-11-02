UMichGradeGrabber
=================

Notifies you of updated grades

Requires Selenium (pip install selenium)

In command line: `python main.py UNIQNAME PW EMAIL_SENDER EMAIL_PW EMAIL_RECEIVER`
Replace the following parameters:
* `UNIQNAME` is your umich unique name
* `PW` is your umich password
* `EMAIL_SENDER` is gmail account name (It must be something@gmail.com currently)
* `EMAIL_PW` is gmail password
* `EMAIL_RECEIVER` is the receiver of the notification

Depending on how complex your password is, you might need to use quotes or escaping to get the special characters to parse correctly

You can test that it's setup correctly by modifying "oldtranscript.txt" and running the script. You should recieve an e-mail containing a diff between your old and new transcripts.

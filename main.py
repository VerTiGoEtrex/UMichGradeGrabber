from sender import EmailSender
from graber import GradeGraber
import time
import sys
import os
import filecmp
import difflib
import shutil
import re

curTranscript = 'transcript.txt'
oldTranscript = 'oldtranscript.txt'

for idx, arg in enumerate(sys.argv):
    print str(idx) + ' ' + str(arg)

while True:
    diffTool = difflib.HtmlDiff()
    graber = GradeGraber()
    graber.grab(sys.argv[1], sys.argv[2], curTranscript)

    if os.path.isfile(oldTranscript): # old transcript exists
        if not filecmp.cmp(curTranscript, oldTranscript): # new grades have been entered
            msg = "GRADES POSTED (but something went wrong in grade grabber)"
            with open(curTranscript, 'r') as curFile, open(oldTranscript, 'r') as oldFile:
                msg = "<html><body>" + diffTool.make_table(oldFile.readlines(), curFile.readlines(), fromdesc='Old transcript', todesc='New transcript', context='True', numlines=2) + "</body></html>"

                #Convert HTML tags to use inlined CSS
                msg = re.sub(r'("table class="diff")', r"\1 style='font-family: courier; border: medium;'", msg)
                msg = re.sub(r'("diff_header")', r"\1 style='background-color:#e0e0e0;'", msg)
                msg = re.sub(r'("diff_next")', r"\1 style='background-color:#c0c0c0;'", msg)
                msg = re.sub(r'("diff_add")', r"\1 style='background-color:#aaffaa;'", msg)
                msg = re.sub(r'("diff_chg")', r"\1 style='background-color:#ffff77;'", msg)
                msg = re.sub(r'("diff_sub")', r"\1 style='background-color:#ffaaaa;'", msg)
                oldFile.seek(0)
                curFile.seek(0)
                for line in difflib.context_diff(oldFile.readlines(), curFile.readlines()):
                    print line
            print "GRADES POSTED, SENDING EMAIL"
            emailSender = EmailSender(sys.argv[3], sys.argv[4], sys.argv[5])
            emailSender.sendNotification(msg)
            print "EMAIL SENT"
            #os.system('rm oldtranscript.txt; mv transcript.txt oldtranscript.txt')
            shutil.copyfile('transcript.txt', 'oldtranscript.txt')
    else: # old transcript does not exist, which means this is the first time running this script
            #os.system('mv transcript.txt oldtranscript.txt')
            shutil.copyfile('transcript.txt', 'oldtranscript.txt')

    time.sleep(10)

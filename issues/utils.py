from django.core.mail import send_mail
from issues.models import *

def issue_comment_email(username, issue, email, link, text):
    body = '''Hello, {0} An issue you are following has been replied to!

    {1}

Follow the link to view the discussion:
    {2}

Thank you!'''.format(username, text, link)
    subject = 'Update: {0}'.format(issue)
    send_mail(subject, body, 'mod@apalinode.com', [email], fail_silently=False)

def new_issue_email(username, issue, email, link):
    body = '''Hello {0},

A new issue was just created at MoD. Follow the link to view the issue:
    {1}

Thank you!'''.format(username, link)
    subject = 'MoD Issue Created'
    send_mail(subject, body, 'mod@apalinode.com', [email])

def get_editors():
    return SiteUser.objects.filter(role='editor')

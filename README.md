# Get O365 Meeting Alerts on Linux

## Overview

It's easy to get into the zone and miss meeting. Gnome notifications are not always in-your-face
enough to make sure you don't miss a meeting. This repo contains code and instructions that allow
you to make any changes to your desktop when a meeting is imminent.

This is intended for a highly technical person - a software developer or systems admin. You need to
be familiar with things like Python, CRON, environment variables.

Currently, only one behavior is built in - changing the Gnome desktop background color 5 minutes
before a meeting. But this can be easily customized.

## Create an AAD App Registration

First you (or your AAD administrator) will need to create an Azure Active Directory (AAD)
"App Registration". It's a limited-scope, safe registration that only allows internal
personnell to access their O365 calendar through Microsoft Graph.

The URL to create an App Registration: 
https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps

### Instructions

* Authentication blade:
    * Set Web Redirect URL to: https://login.microsoftonline.com/common/oauth2/nativeclient
    * Create Access and ID tokens
    * Who can use this application or access this API? Select single-tenant
    * Allow public client flows: No
* Certificates & secrets blade:
    * Create a secret and record the secret ID
* API permissions blade:
    * Add "Calendars.Read", "offline_access" and "User.Read" permissions
    * Click "Grant admin consent for ..."

If you're having difficulty the much more thorough instructions at https://github.com/O365/python-o365
might help you out.

## Setup local environment

Next you need to setup your local environment.

Clone the repo:
`git clone git@github.com:malcolmvr/o365_linux_meeting_alerts.git`

Create an .env file, for example:

```
export TENANT_ID=[the "Directory (tenant) ID" on the Overview blade]
export APPLICATION_ID=[the "Application (client) ID" on the Overview blade]
export CLIENT_SECRET=[to the client secret (not the Client ID)]
export IMMINENT_MINUTES=5
export IMMINENT_DESKTOP_BACKGROUND_COLOR=780e0e
export NORMAL_DESKTOP_BACKGROUND_COLOR=222222
```

Next setup some CRON jobs. First make some files executable.

```
$ chmod +x check_events.sh
$ chmod +x get_events.sh
```

* crontab -e
* Add:
    * `*/1 * * * * /usr/bin/bash -c 'cd /home/malcolm/Source/personal/ubuntu_meeting_notifications && source check_events.sh' > /dev/null 2>&1`
    * `*/15 * * * * /usr/bin/bash -c 'cd /home/malcolm/Source/personal/ubuntu_meeting_notifications && source env/bin/activate && python3 get_events.py' > /dev/null 2>&1`

## Customizing the alert behavior

Update the `update_ui.py` file to change what happens when a meeting is imminent. If you think of something cool here
send me a note and I'll add it to the repo as an option.
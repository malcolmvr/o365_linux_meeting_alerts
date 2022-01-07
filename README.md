# Ubuntu Meeting Notifications

## Create an AAD App Registration: https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps

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

## Setup local environment

Create a .env file and set:

* TENANT_ID to the "Directory (tenant) ID" on the Overview blade
* APPLICATION_ID to the "Application (client) ID" on the Overview blade
* CLIENT_SECRET to the client secret (not the Client ID)

CRON:

```
$ chmod +x check_events.sh
$ chmod +x get_events.sh
```

* crontab -e
* Add:
    * `*/1 * * * * /usr/bin/bash -c 'cd /home/malcolm/Source/personal/ubuntu_meeting_notifications && source check_events.sh' > /dev/null 2>&1`
    * `*/15 * * * * /usr/bin/bash -c 'cd /home/malcolm/Source/personal/ubuntu_meeting_notifications && source env/bin/activate && python3 get_events.py' > /dev/null 2>&1`


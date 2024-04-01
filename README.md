This project is for learning only, I take no responsibility for any issues that arise.

"SF Light Novel Automatic Check-in" script, an example for GitHub Action, can be used with just a single step of Forking.

## How to Use

1. Directly Fork this repository

2. Configure account (Mandatory)

Go to Settings > Actions > General > Workflow permissions, change to "Read and write permissions". This is to grant "Monthly Update Action" the permission to update the repository. "Monthly Update Action" runs once a month and adds a new commit to the repository to prevent GitHub from disabling Actions due to inactivity.

Go to Settings > Secrets > Actions > New repository secret, add "USERNAME", where the content is the mobile number of the account you want to sign in, add "PASSWORD", where the content is the password of the account you want to sign in, or add "SFCommunity" and "session_APP".

![](https://github.com/CarrotsPie/sfacg_checkin/blob/main/p1.png)

Configure schedule time (Optional)

Change the time in .github/workflows/health-report.yml:

yml

```
  on:
  workflow_dispatch:
  schedule:
     - cron: '0 23 * * *'
```

4. Configure DingTalk message notification (Optional)
- Mobile version DingTalk > add at the top right corner > create face-to-face group > after creating, you will have a group chat with only you.
- Computer version DingTalk > group setting > intelligent group assistant > add robot > customize, name it anything, choose "custom keywords" for security setting, fill in "check-in", then copy Webhook in the next step.
- Settings > Secrets > Actions > New repository secret, add "DINGTALK_TOKEN", the content is the content after "access_token=" in the copied Webhook.
6. Testing

Actions > I understand my workflows, go ahead and enable them.

Actions > @sfacg_checkin/action Demo > Enable workflow > Run workflow.

Actions > Monthly Update Action > Enable workflow > Run workflow.

7. Disable

Actions > @sfacg_checkin/action Demo > Disable workflow.

Actions > Monthly Update Action > Disable workflow.

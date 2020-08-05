# Linkiboost
*Wanna be nice and corporate? Endorse your teammates!*

This script leverages the power of automation by endorsing the highlighted skills on Linkedin of your teammates, family members, friends...

It will only endorse the skills that have not been endorsed yet. Those previously approved will remain still.

**NOTE**: you can hide people who endorsed you directly on Linkedin if you don't want them to support you.


## Requirements
- Internet connexion (increase delay in script if your connexion is slow)
- Linkedin account
- Chrome driver
  - MacOS:
  ```shell script
  brew cask install chromedriver
  ```
  - Other: *https://chromedriver.chromium.org/*
## Installation
- Fill your credentials in the json config template
    - Linkedin username and password
    - Path to the Chrome driver installed above (MacOS: */usr/local/bin/chromedriver*)
    - List of person(s) to endorse
- Venv
    ```shell script
    python3 -m venv myenv
    source myenv/bin/activate
    pip install -r requirements.txt
    ```

## Execution
``` shell script
python main.py config.json
```
## TODO
- Find a consistent way to load skills
- Send invitation when not connected
- Select level and origin of skills
- Upgrade to non developer users
- Add tests
---

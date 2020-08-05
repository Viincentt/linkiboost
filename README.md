# Linkiboost
*Wanna be nice and corporate? Endorse your teammates!*

This project is blablabla
- Endorse the highlighted skills of your teammates
- Won't undo previously endorsed skills
- Check the log
- **NOTE**: you can still hide people who endorsed you if you don't want them to support you.


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
- Send invitation when not connected to someone you want to endorse
---
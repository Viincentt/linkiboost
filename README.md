# Linkiboost
*Wanna be nice and corporate? Endorse your teammates!*

This project is blablabla


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
    - Username
    - Password
    - Path to Chrome driver (MacOS: */usr/local/bin/chromedriver*)
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
- Send invitation when not connected to someone
- add 2020 and 2022

---
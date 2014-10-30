# Erlenmeyer

Flask boilerplate

## Usage

1. Get `cookiecutter`
  ```bash
  $ pip install cookiecutter
  # You should be using pipsi though ;)
  $ pipsi install cookiecutter
  ```

2. Initialize your app
  ```bash
  $ cookiecutter git@github.com:SiliconValleyInsight/erlenmeyer.git
  ```

3. Up
  ```bash
  $ cd <app_name>
  $ ./up.sh
  ```

## Planned Features

* User accounts with basic information
  * Login
    * OAuth2
      * Google
      * Facebook
      * Coursera
    * OAuth
      * Twitter
    * Password login
  * Profile page
* Posts CMS
* API
* Database Migration
* Mailing

_Note: Features should be modular (exist as modules that can be swapped in/out)_

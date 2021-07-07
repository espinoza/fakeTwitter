# fakeTwitter

A simple Twitter clon.

[Visit here](http://52.15.51.235/)

## Requirements
* `Python3`
* `Postgresql`
* `Node.js` with `Node-Sass`

## How to install

1. Clone this repository: `git clone https://github.com/espinoza/fakeTwitter`
2. Enter the directory: `cd fakeTwitter`
3. Create virtual environment: `python3 -m venv .venv`
4. Activate virtual environment: `source .venv/bin/activate`
5. Install Python packages: `pip install -r requirements.txt`
6. Create Postgresql database: `NAME: fake_twitter`, `USER: postgres`, `PASSWORD: root`
7. Migrate database: `python manage.py migrate`
8. Compile CSS files: `node-sass assets/scss -o static/css`
9. Run server: `python manage runserver`
10. Open a browser and go to `http://localhost:8000`

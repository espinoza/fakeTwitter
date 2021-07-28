# fakeTwitter

A simple Twitter clone.
Responsive, without using CSS framework.

[Visit here](http://52.15.51.235/)

## Screenshots

![image](https://user-images.githubusercontent.com/42013600/127357324-e9e890b6-b52a-4f2a-a335-6480d015c468.png) &nbsp;&nbsp;&nbsp; ![image](https://user-images.githubusercontent.com/42013600/127358042-ba6d0add-a647-4a32-a8c1-097aade899d3.png)

![image](https://user-images.githubusercontent.com/42013600/127357449-4b2fa992-6f4c-4178-85bd-4bc0085db3b4.png)

## Installation

### Requirements
* `Python3`
* `Postgresql`
* `Node.js` with `Node-Sass`

### How to install

1. Clone this repository: `git clone https://github.com/espinoza/fakeTwitter`
2. Enter the directory: `cd fakeTwitter`
3. Create virtual environment: `python3 -m venv .venv`
4. Activate virtual environment: `source .venv/bin/activate`
5. Install Python packages: `pip install -r requirements.txt`
6. Create Postgresql database: `NAME: fake_twitter`, `USER: postgres`, `PASSWORD: root`
7. Migrate database: `python manage.py migrate`
8. Compile CSS files: `node-sass assets/scss -o main/static/css`
9. Run server: `python manage runserver`
10. Open a browser and go to `http://localhost:8000`

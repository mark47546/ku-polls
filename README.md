# Ku-Polls
[![Build Status](https://travis-ci.com/mark47546/ku-polls.svg?branch=master)](https://travis-ci.com/mark47546/ku-polls)

Django application for Kasetsart University online polls
## Documents
[Vision Statement](https://github.com/mark47546/ku-polls/wiki/Vision-Statement)

[Requirements](https://github.com/mark47546/ku-polls/wiki/Requirements)

## Installation

1. Access `ku-polls` directory.
2. Install required packages. <pre class=output>pip install -r requirements.txt</pre>
3. Create `.env` in the root directory for setting configurations (`SECRET_KEY` and `DEBUG`).
4. Create the database. <pre class=output>py manage.py migrate</pre>

## Running

1. Access `ku-polls` directory.
2. Run server. <pre class=output>py manage.py runserver</pre>
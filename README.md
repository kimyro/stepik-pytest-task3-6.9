## stepik-pytest-task3-6.9
A separate repository for task with peer-review in 3.6 lesson.

Contains 2 files:
* conftest.py
* test_items.py

#### Usage
It's simple, just run the script with language parameter:
`pytest --language=es test_items.py`

#### Extra
Chrome browser is used by default, but you can launch test script in Firefox if needed.
Make sure geckodriver is installed in your system (and added to PATH).
Just pass the browser name to --browser parameter as following:

`pytest --language=en --browser=firefox test_items.py`

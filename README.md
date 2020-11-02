<br />
<p align="center">
  <h3 align="center">FLASK REST API</h3>
</p>



## Table of Contents

* [About](#about)
  * [Built With](#built-with)
  * [Deployed With](#deployed-with)
* [Use](#use)
* [Contact](#contact)



## About

RESTful API built with Flask and deployed on Heroku. It contains information about me, Ezra Mizrahi.

### Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Python](https://www.python.org/)

### Deployed With

* [Heroku](https://heroku.com/)



## Use

This is a consumption only API. GET is the only method supported.

Try it out by copying this command into your terminal:

```bash
curl http://ezra-mizrahi-api.herokuapp.com/ezra
```

It should return data about me in `JSON` format:

```
[
  {"name": "Ezra Mizrahi",
   "title": "software engineer",
   "skills": [
   "javascript",
   ...
   ],
   ...
  }
]
```



## Contact

Ezra Mizrahi - ezra.mizrahi@hey.com

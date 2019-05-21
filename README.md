# heroku-rq-dashboard

A deploy-ready app using [Flask](http://flask.pocoo.org) + [rq_dashboard](https://github.com/eoranged/rq-dashboard) for monitoring RQ queues, jobs and workers.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


Uses [python-decouple](https://github.com/henriquebastos/python-decouple) for Heroku/Flynn env compatibility.

## How to use

#### Heroku/Flynn

Set `REDIS_URL` environment variable as normal via interface/api


#### Other

As specified in [python-decouple](https://github.com/henriquebastos/python-decouple), 
create an .env file in the root folder and use the following template

```
REDIS_URL=redis://name:password@host:port
```

## Security

rq_dashboard is able to modify the redis database so secure app as necessary

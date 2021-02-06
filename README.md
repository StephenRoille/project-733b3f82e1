# Introduction to Heroku (2014)

url: https://www.youtube.com/watch?v=QTOkqzCTGxw

Create the application
```bash

heroku create "introduction-to-heroku"
```
This line automatically deploy the application to heroku and add the `heroku` remote to
git (`https://git.heroku.com/introduction-to-heroku.git `)

Monitor the application with
```bash

heroku logs -t
```

Set environement variable in the current process (recreate a new release)
```bash

heroku config:set NAME=Stephen
```

View all releases
```bash

heroku releases
```

Rollback to previous release (by creating a new release)
```bash

heroku rollback v1
```

Monitor number of dynos used to run the application
```bash

heroku ps
```

Change the number of dynos to adapt application to traffic
```bash

heroku ps:scale web=4
```



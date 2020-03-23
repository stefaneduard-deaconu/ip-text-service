# ip-text-service
The service used for text recognition, translation, and work with a user's docs


# for testing purposes
### You need the mongo uri...
For running locally, you need a _mongo_uri.env_ file at the root of the project, that contains the "mongodb+srv://" URI
### Script for watching the files
I added a shell, heroku.sh, that you can run with _bash heroku.sh_.
It restarts heroku locally everytime the project changes (any .py and .html file modifications).

For it to work, you need to install heroku-cli, npm, then run _npm install -g nodemon_
Then run again _bash heroku.sh_.
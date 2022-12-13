# import the create app function
# that lives in src/__init__.py
from src import create_app

# create the app object
app = create_app()



# If this file is being run directly, then run the application
# via the app object.
# debug = True will provide helpful debugging information and
#   allow hot reloading of the source code as you make edits and
#   save the files.
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 4000)



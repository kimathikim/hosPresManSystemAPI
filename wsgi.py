from app.factory import create_app

app = create_app()

if __name__ != "__main__":
    # The WSGI server will run this when in production.
    application = app

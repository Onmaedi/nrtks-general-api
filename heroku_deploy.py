# this is just for heroku deploy

from src.app import create_app


if __name__ == "__main__":
    app = create_app()

    app.run()

from flask_script import Manager

from app import create_app, db
from app.home.models import New, Type

app = create_app()
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        New=New,
        Type=Type
    )


if __name__ == '__main__':
    manager.run()
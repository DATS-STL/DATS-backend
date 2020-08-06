#!/usr/bin/env python3

# To add a new revision to the db migration:
#
#        python sqlmigrate.py db revision --autogenerate -m "An explanatory message"
#
# HOW TO USE
#
# 1. Make the desired changes to the models in
#    src/familytoolswap_backend/models. Do not make changes to your heroku
#    database directly.
# 2. Any new/deleted models need to be updated in the "from ... import" lines
#    below.
# 3. Run this script as shown above.
# 4. Find the new migration in migrations/versions (should be named after your
#    explanatory message), and make sure the upgrade and downgrade commands do
#    what you expect.
# 5. run the "db upgrade" command below, then verify in psql/pgadmin that the
#    migration went as expected.


# To perform git-controlled database migrations:
#
#        python sqlmigrate.py db upgrade
#
# As part of the deploy process, run the "db upgrade" command above.
# This command is automatically run in the heroku deploy (See ./Procfile)

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.familytoolswap_backend import app, sa

# You must add models you want part of the migration here
from src.familytoolswap_backend.models.user import User
from src.familytoolswap_backend.models.messages import Messages

migrate = Migrate(app, sa)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def seed_db():
    try:
		# Any seeding SQL should be done here

        sa.session.commit()
    except:
        sa.session.rollback()
        raise

if __name__ == '__main__':
    manager.run()

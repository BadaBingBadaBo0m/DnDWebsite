## Env.py in Migrations 

The env.py that is part of the starter has been modified from the default, to include code to handle the SCHEMA in production. If you deleted your migrations and did a flask db init you now have the default env.py, not the custom one from the project starter. Make sure you env.py is the same as the code below, and if not replace the entire file with this code

```
from __future__ import with_statement

import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from flask import current_app
config.set_main_option(
    'sqlalchemy.url',
    str(current_app.extensions['migrate'].db.engine.url).replace('%', '%%'))
target_metadata = current_app.extensions['migrate'].db.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """

    # this callback is used to prevent an auto-migration from being generated
    # when there are no changes to the schema
    # reference: http://alembic.zzzcomputing.com/en/latest/cookbook.html
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
            **current_app.extensions['migrate'].configure_args
        )
        # Create a schema (only in production)
        if environment == "production":
            connection.execute(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA}")

        # Set search path to your schema (only in production)
        with context.begin_transaction():
            if environment == "production":
                context.execute(f"SET search_path TO {SCHEMA}")
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```


If you created a new migration file, the first thing you will need to do is import the environment and SCHEMA near the other import statements.

```
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")
```

Next, for each table you are creating in your migration there will be an op.create_table() method call. After each op.create_table() call (and remember the closing ) will be after all the column and constraint details), you will want to add the following conditional statement to handle prefixing the SCHEMA

```
 if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
```
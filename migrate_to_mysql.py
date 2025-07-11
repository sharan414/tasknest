from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models import User, Task  # Make sure User and Task are imported properly

# Connect to SQLite
sqlite_engine = create_engine('sqlite:///database.db')
sqlite_metadata = MetaData()
sqlite_metadata.reflect(bind=sqlite_engine)
SQLiteSession = sessionmaker(bind=sqlite_engine)
sqlite_session = SQLiteSession()

# Connect to MySQL
mysql_engine = create_engine('mysql+pymysql://root:yourpassword@localhost/tasknest_db')
MySQLSession = sessionmaker(bind=mysql_engine)
mysql_session = MySQLSession()

# Migrate users
sqlite_users = sqlite_session.query(User).all()
for user in sqlite_users:
    mysql_session.add(User(id=user.id, username=user.username, password=user.password))

# Migrate tasks
sqlite_tasks = sqlite_session.query(Task).all()
for task in sqlite_tasks:
    mysql_session.add(Task(
        id=task.id,
        title=task.title,
        description=task.description,
        deadline=task.deadline,
        priority=task.priority,
        status=task.status,
        user_id=task.user_id
    ))

mysql_session.commit()
print("✅ Migration completed successfully!")

from .. import app, sa

class User(sa.Model):
	__tablename__ = "user"
	user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
	username = sa.Column(sa.String(255), nullable=False)
	password = sa.Column(sa.String(255), nullable=False)

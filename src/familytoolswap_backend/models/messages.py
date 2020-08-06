from .. import app, sa

class Messages(sa.Model):
	__tablename__ = "messages"
	message_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
	name = sa.Column(sa.String(255), nullable=False)
	value = sa.Column(sa.String(255), nullable=False)

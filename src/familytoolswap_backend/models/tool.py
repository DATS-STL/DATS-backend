from .. import app, sa

class Tool(sa.Model):
	__tablename__ = "tool"
	tool_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
	user_id = sa.Column(sa.Integer, sa.ForeignKey('user.user_id'), nullable=False)
	type = sa.Column(sa.String(80), nullable=False)
	name = sa.Column(sa.String(80), nullable=False)
    description = sa.Column(sa.String(255), nullable=True)
    brand = sa.Column(sa.String(80), nullable=False)
   

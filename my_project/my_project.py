from datetime import datetime
from flask import Flask,render_template,url_for,request,redirect,flash

from logging import DEBUG
from forms import BookmarkForm
app=Flask(__name__)
app.logger.setLevel(DEBUG)
bookmarks=[]
app.config['SECRET_KEY']='X\x87\xda\x98\xcei\xf3\xf2\xee\x10[x\xd7"\xc7\x1b\xe9BY\xc8RF\xc1P'
def new_bookmark(num):
	return sorted(bookmarks,key=lambda bm:bm['date'],reverse=True)[:num]
def store_books(url,description):
	bookmarks.append(dict(
	url=url,
	description=description,
	user="Ani",
	date=datetime.utcnow()
	))
class worker:
	def __init__(self,firstname,lastname):
		self.firstname=firstname
		self.lastname=lastname	
	def __str__(self):
		return "{} {}".format(self.firstname,self.lastname)	
	def function(self):
		return "{}. {}.".format(self.firstname[0],self.lastname[0])

@app.route('/')
@app.route('/index')
def indeyx():
	return render_template('index.html',title="yoyooyo",tryouts=worker("Jon","Snow"),new_bookmark=new_bookmark(5))

@app.route('/pager',methods=['GET','POST'])
def lala():
	form=BookmarkForm()
	if form.validate_on_submit():
		url=form.url.data
		description=form.description.data
		store_books(url,description)
		flash('{} stored'.format(description))
		return redirect(url_for('indeyx'))
	return render_template('add.html',form=form)	
@app.errorhandler(404)
def pagenotfound(e):
	return render_template('404.html'),404
if __name__=='__main__':
	app.run("localhost",5001,debug=True)



from flask import Flask, render_template, request
from .models import DB, User, Tweet
from .twitter import add_or_update_user
from .predict import predict_user
from os import getenv


# factory
def create_app():
    app = Flask(__name__)

    # tell our app where to find our database
    # 'registering' our database with the app
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route("/")
    def home():
        # query the database for all users
        users = User.query.all()
        # print(users)
        return render_template('base.html', title='Home', users=users)

    @app.route("/reset")
    def reset():
        # drop our DB tables
        DB.drop_all()
        # create tables according to the classes in model.py
        DB.create_all()
        return render_template('base.html', title='Reset DB')

    # @app.route('/populate')
    # def populate():
        # add_or_update_user('nasa')
        # add_or_update_user('austen')
        # add_or_update_user('ryanallred')
        # ryan = User(id=1, username='Ryan')
        # DB.session.add(ryan)
        # julian = User(id=2, username='Julian')
        # DB.session.add(julian)
        # tweet1 = Tweet(id=1, text='Ryans tweet', user=ryan)
        # DB.session.add(tweet1)
        # tweet2 = Tweet(id=2, text='Julians tweet', user=julian)
        # DB.session.add(tweet2)
        # DB.session.commit()
        # return render_template('base.html', title='Populate')

    @app.route('/update')
    def update():
        usernames = [user.username for user in User.query.all()]
        for username in usernames:
            add_or_update_user(username)
        return render_template('base.html', title='Update')

    @app.route('/user', methods=['POST'])
    @app.route('/user/<username>', methods=['GET'])
    def user(username=None):
        if request.method == 'GET':
            tweets = User.query.filter(User.username == username).one().tweets

        if request.method == 'POST':
            tweets = []
            try:
                username = request.values['user_name']
                add_or_update_user(username)
                message = f'User "{username}" was succesfully added.'
            except Exception as e:
                message = f'Error adding {username} : {e}'

        return render_template('user.html',
                               title=username,
                               tweets=tweets,
                               message=message)

    @app.route('/compare', methods=['POST'])
    def compare():
        user0 = request.values['user0']
        user1 = request.values['user1']

        if user0 == user1:
            message = "Cannot comapre users to themselves"
        else:
            text = request.values['tweet_text']
            prediction = predict_user(user0, user1, text)
            message = '''"{}" is more likely to be said
                         by user "{}" than by user "{}".'''.format(
                        text,
                        user1 if prediction else user0,
                        user0 if prediction else user1)
        return render_template('prediction.html',
                               title='Prediction',
                               message=message)

    return app

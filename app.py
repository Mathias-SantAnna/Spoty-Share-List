import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_pymongo import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/") 
@app.route("/get_playlists")
def get_playlists():
    playlists = mongo.db.playlists.find()
    return render_template("/playlists/playlists.html", playlists=playlists)


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
          
    return render_template("/register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("/login.html")


# PROFILE PAGE
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    username = user["username"]
    user_playlist = list(mongo.db.playlist.find(
        {'created_by': ObjectId(user["_id"])}))
    for paylist in user_playlist:
        paylist['created_by'] = mongo.db.users.find_one(
            {"_id": paylist['created_by']})['username']
        paylist['genre'] =  mongo.db.music_genre.find_one(
            {"_id": paylist['genre']})['genre_name']
    if session["user"]:
        return render_template(
            "profile.html", username=username, user_playlist=user_playlist)

    return redirect(url_for("login"))


# LOGOUT
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


# ADD PLAYLIST
@ app.route("/add_playlist", methods=["GET", "POST"])
def add_playlist():
    if not session.get("user"):
        render_template("templates/error_handlers/404.html")

    if request.method == "POST":
        user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
        playlist = {
            "genre": ObjectId(request.form.get("genre_name")),
            "playlist_name": request.form.get("playlist_name"),
            "img_url": request.form.get("img_url"),
            "playlist_details": request.form.get("playlist_details"),
            "playlist_tracks": request.form.get("playlist_tracks"),
            "artist_name": request.form.get("artist_name"),
            "created_by": ObjectId(user_id),
            "playlist_url": request.form.get("playlist_url")
        }

        mongo.db.playlist.insert_one(playlist)
        flash("Playlist successfully added")
        return redirect(url_for("profile", username=session['user']))

    artist = mongo.db.artist.find()
    music_genre = list(mongo.db.music_genre.find().sort("genre_name", 1))
    return render_template(
        "playlists/add_playlist.html", artist=artist, music_genre=music_genre
        )


# THE APP
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
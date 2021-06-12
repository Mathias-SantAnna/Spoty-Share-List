# Import Python Modules
import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from flask_pymongo import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

# Flask Instance
app = Flask(__name__)

# MongoDB Config
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# MongoDB Global Variable
mongo = PyMongo(app)


# Index
@app.route("/") 
@app.route("/home")
def home():
    playlists = list(mongo.db.playlist.find())
    music_genre = list(mongo.db.music_genre.find().sort("genre_name", 1))

    return render_template(
        "/playlists/playlists.html",
        playlists=playlists,
        music_genre=music_genre)


# SEARCH PLAYLISTS
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    playlist = list(mongo.db.playlist.find({"$text": {"$search": query}}))
    if len(playlist) == 0:
        flash(f"Sorry no playlists with {query} were found!")
    else:
        flash(f"Your search for {query} returned {len(playlist)} result(s)!")
    return render_template("/playlists/playlists.html", playlist=playlist)  


# FILTER PLAYLISTS (GENRE & ARTISTS)
@app.route("/genre_filter/<id>")
def genre_filter(id):
    genre = list(mongo.db.music_genre.find({"genre_name": id}))
    return render_template("/playlists/playlists.html", genre=genre)


# FILTER PLAYLISTS (GENRE & ARTISTS)
@app.route("/artist_filter/<id>")
def artist_filter(id):
    artist = list(mongo.db.artist.find({"artist": id}))
    return render_template("playlists/playlists.html", artist=artist)


# MUSIC GENRE
@app.route("/music_genre/<_id>")
def music_genre(genre_id): 
    music_genre = list(mongo.db.music_genre.find().sort("_id", 1))
    return render_template("music_genre.html", music_genre=music_genre)


# MUSIC GENRE S
@app.route("/music_genres")
def music_genres(): 
    music_genres = list(mongo.db.music_genre.find().sort("_id", 1))
    return render_template("genre.html", music_genres=music_genres, )


# SINGLE PLAYLIST
@app.route("/playlist/<playlist_id>")
def playlist(playlist_id):
    playlist = mongo.db.playlist.find_one_or_404(
            {'_id': ObjectId(playlist_id)}
        )
    genre = mongo.db.music_genre.find_one_or_404(
            {'_id': ObjectId(playlist["genre"])}
        )
    playlist["genre_name"] = genre["genre_name"]
    user = mongo.db.users.find_one_or_404(
            {'_id': ObjectId(playlist["created_by"])}
        )
    return render_template(
        "playlists/playlist.html",
         playlist=playlist, user=user)


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
        flash("Welcome, {}".format(
            request.form.get("username")), "success")
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
                    existing_user["password"],
                     request.form.get("password")):
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
    for playlist in user_playlist:
        playlist['created_by'] = mongo.db.users.find_one(
            {"_id": playlist['created_by']})['username']
        playlist['genre'] = mongo.db.music_genre.find_one(
            {"_id": playlist['genre']})['genre_name']
    if session["user"]:
        return render_template(
            "profile.html", username=username, user_playlist=user_playlist)

    flash("Access denied. Create your own account and login", "error")
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


# EDIT PLAYLIST
@ app.route("/edit_playlist/<playlist_id>", methods=["GET", "POST"])
def edit_playlist(playlist_id):
    if not session.get("user"):
        render_template("templates/page_404.html")

    if request.method == "POST":
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        submit = {
            "genre": ObjectId(request.form.get("genre_name")),
            "playlist_name": request.form.get("playlist_name"),
            "img_url": request.form.get("img_url"),
            "playlist_details": request.form.get("playlist_details"),
            "playlist_tracks": request.form.get("playlist_tracks"),
            "artist_name": request.form.get("artist_name"),
            "created_by": ObjectId(user_id),
            "playlist_url": request.form.get("playlist_url")
        }
        
        mongo.db.playlist.update({"_id": ObjectId(playlist_id)}, submit)
        flash("Playlist successfully edited")
        return redirect(url_for("profile", username=session['user']))

    playlist = mongo.db.playlist.find_one({"_id": ObjectId(playlist_id)})
    artist = mongo.db.artist.find()
    music_genre = list(mongo.db.music_genre.find().sort("genre_name", 1))
    return render_template(
        "playlists/edit_playlist.html", 
        playlist=playlist, 
        artist=artist, 
        music_genre=music_genre)


# MANAGE MUSIC GENRE


# DELETE PLAYLIST
@app.route("/delete_playlist/<playlist_id>", methods=["GET", "POST"])
def delete_playlist(playlist_id):
    """Delete playlists function"""
    if "user" in session:
        playlist = mongo.db.playlists.find_one({"_id": ObjectId(playlist_id)})

        if session["user"].lower() == playlist["created_by"].lower():
            mongo.db.playlists.remove({"_id": ObjectId(playlist_id)})
            flash("playlist successfully deleted", "success")
            return redirect(url_for("profile", username=session["user"]))

        flash("Access denied. This is not your playlist", "error")
        return redirect(url_for("profile", username=session["user"]))

    flash("Access denied. This is not your playlist", "error")
    return redirect(url_for("register"))


# THE APP
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
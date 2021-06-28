# Spoty Share List 
<h2 align="center"><img src="https://i.postimg.cc/CLWV9npc/Big-Logo-Read-Me.gif"></h2>

It's a mobile-first &#38; responsive web application for sharing Playlists with it's users. The objective is to intensify and amplify the usage of music streaming services like Spotify® 🎶
Link to the website is available [HERE.](https://spoty-share-list.herokuapp.com/home)

<br>
<h2 align="center"><img src="https://i.postimg.cc/hjKHYfQf/Site-Mock-Up.png"></h2>
# Table of Contents

- [Spoty Share List](#Spoty-Share-List)
- [UX]()
  * [WHO'S THIS WEBSITE FOR](##WHO'S-THIS-WEBSITE-FOR)
  * [User Experience Planes](##User-Experience-Planes)
  * [Strategy Plane](###Strategy-Plane)
  * [Scope Plane](###Scope-Plane)
  * [Structure Plane](###Structure-Plane)
  * [Skeleton Plane](###Skeleton-Plane)
  * [Surface Plane](###Surface-Plane)
  * [Website Construction Plans](##Website-Construction-Plans)

- [Features](##Features)
   * [Existing Features](###Existing-Features)
   * [Features Left to Implement](###Features-left-to-implement)

- [Technologies Used](##Technologies-Used)

- [Resources](##Resources)
   * [General Resources](###General-Resources)
   * [Tools](###Tools)

- [Project Barriers & Solutions](##Project-Barriers-&-Solutions)
  * [Test Strategy](####Test-Strategy)
  * [Summary](####Summary)
  * [High Level Test Cases](###High-Level-Test-Cases)
  * [Access Requirements](####Access-Requirements)
  * [Regression Testing](####Regression-Testing)
  * [Assumptions and Dependencies](####Assumptions-and-Dependencies)
  * [Out of Scope](####Out-of-Scope)
  * [Test Results](###Test-Results)

- [Deployment](##Deployment)
  * [Project Creation](###Project-Creation)
  * [Deployment to Heroku](###Deployment-to-Heroku)
  * [Run Locally](###Run-Locally)
  * [Fork Project](###Fork-Project)

- [Credits](##Credits)
  * [Code](###Code)
  * [Contents](###Contents)
  * [Acknowledgements](###Acknowledgements)

## WHO'S THIS WEBSITE FOR
Since everyone loves music (and I even more 🤟), why not do something enjoyable and productive at the same time. As we all know, these days the consumption of the streaming services are only growing, and a great tool to have is to be part of a awesome group of people with great music taste (some may discord) where you can create, edit, share your Playlists and much more...(more features to be added in the future). 
The website is designed for the user that desires to share their playlists and find new ones in a very simple and easy way that the first time visitor can adapt fairly quickly.💚 🎧  

## User Experience Planes

### Strategy Plane
The website is designed for the people who would like to share and find different spotify playlists, add to their own catalog, share with friends, while working, excercing or just for the fun or it, it's a great tool of motivation, scientifically proofed to increased someone's performance up to 30%. Following simple steps users can Register to create an account, to create a new Playlist in a very easy way. 
To open a specific playlist the visitor don't need to register himself, going to Search field they can find any existing playlist that matches the input field. The Library with all playlists is hidden for visitor to make them sign up in order to add a playlist and browse for mode content such Genres.

Registered users see all the playlists shown (Library), or browse by music genre(All Genres), or even by details (Search). Also they can click in the embed iframe field that would send them to the existing playlist in Spotify. A search field is on these pages to help the user to find what they're looking for, using a specific keyword(s).  The website design is simple and user friendly for the first-time visitor easily start navigating. Also for creating a new playlist is a set of instructions for the "hardest parts" like to add a Url for the specific spotify. 

All the functions on the tables below are minimum requirements on the website to achieve the current user's and owner's goals. (On a scale of 1 &#91;least&#93; - 5 &#91;most&#93;).

| Opportunity                                   | Importance |         Viability       |
| :-------------------------------------------- | :--------: | :---------------------: |
| Register                                      |     5      |            5            |
| Login / Log out                               |     5      |            5            |
| Create / Edit / Delete Playlists              |     5      |            4            |
| Search Playlist By Keywords                   |     4      |            5            |
| Show Playlists By Genre                       |     4      |            5            |
| Responsiveness                                |     4      |            5            |
| Manage Playlist Genre (Admin only)            |     3      |            5            |
| Page 404                                      |     3      |            4            |

There is some other functions to implement in the website, however, these are not mandatory to achieve the current project goals. Because of lack of time or knowledge, most of these features will only implemented in the future.

| Opportunity                                    | Importance |        Viability        |
| :--------------------------------------------- | :--------: | :---------------------: |
| Upload Image For Each Playlist                 |     4      |            4            |
| Upload Spotify Url For Each Playlist           |     4      |            3            |
| Pagination                                     |     3      |            3            |
| Admin Edit and Delete buttons in Library page  |     3      |            3            |
| User profile favorite Genre & Artists          |     2      |            2            |
| Resetting Password When Users Forget It        |     3      |            2            |
| Review By Other Users                          |     2      |            2            |
| “Like” Button By Other Users                   |     2      |            2            |


  <div align="right"><a href="#top">🔝</a></div>

### Scope Plane

To achieve user my project goals, below are the minimum features to be included in this project. Also, **CRUD** (Create, Read, Update, and Delete) functions are required for this project so these are implemented as a part of essential features.

- Simple design Home page that first-time users can recognise the purpose of the website easily. All the playlists are shown on *Home* page (R)
- Music Genre (Metal, Dance & Electro, Rock) pages where users can see playlists by the Music Genre (R)
- Register page where users can create an account to create, post and edit playlists
- Login page where users can log in to the website
- Logout function that users can log out the website
- Profile page where users can see all their playlists and access to create, post, edit and delete playlists
- Create Playlist page where users can create and post their playlists (C)
- Edit Playlist page where users can edit their playlists (U)
- Delete Playlist function that users can delete their playlists (D)
- Manage playlist page and functions that only <ins>admin user</ins> (owner) can create, edit and delete Music Genre (C & U & D)
- Search by a keyword(s) function that users can search for specific playlists
- Subscribe to newsletter function to collect users e-mail addresses
- 404 page that appears for invalid URL and takes users back to *Home* page of the website safely

> **Note:**<br>
> Initially, only 3 fixed Music Genre are planned for playlists, however as the project is created, discover that a newly created playlist can be implemented on the website by using loop so Music Genre are not limited. (e.g. If the admin decides to create a new playlist called "Birthday", it can be implemented to the website automatically)

### Structure Plane

— **Front-end** —

The website consists of a **Home** page with **12 other core pages**.

- **Home** (`index.html`)<br>The main page of the website. There is a logo, navigation bar to *Music Genre*, *Register* & *Login* pages, a title and a hero image. All the summary of playlists are contained and users can access a full *Playlist* page. There is a footer with a form to subscribe to newsletter and some social icons

- **Library** (`playlists/library.html`)<br>The page where users can see all existing playlists and search and access a full *Playlist* page. The same navigation bar and footer are used as *Home*

- **Playlist** (`playlists/playlist.html`)<br>The page where a full Playlist is shown individually. The same navigation bar and footer are used as *Home*

- **Register** (`register.html`)<br>The page where users can create an account. Once users create an account successfully, they will be led to *Profile* page. The navigation bar is different to *Home* page, in which users can go back to *Home* page by clicking Uncle Jam's icon, and there is no footer

- **Login** (`login.html`)<br>The page where users who have an account can log in to the website. Once users log in successfully, they will be led to *Profile* page. The navigation bar is different to *Home* page, in which users can go back to *Home* page by clicking Uncle Jam's icon, and there is no footer

- **Profile** (`profile.html`)<br>The page where users will be led when they create an account or log in. Users see all of their playlists with an option to edit&#47;delete. Users can access to *Edit Playlist* page and *Delete Playlist* function by clicking a button on the Playlist. There is an option to create a new Playlist from this page by clicking a button and that leads to *Create Playlist* page. The same navigation bar and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a link to *Profile* page on the navigation bar

- **Create Playlist** (`playlists/add_playlist.html`)<br>The page where users can create and post playlists. There is no link on the navigation bar and it can only be accessed by clicking a Create Playlist button on *Profile* page. The page style is the same as *Register | Login*, and users can go back to *Profile* page by clicking Gingerbread man icon or cancel button

- **Edit Playlist** (`playlists/edit_playlist.html`)<br>The page where users can edit playlists. There is no link on the navigation bar and it can only be accessed by clicking an Edit button on *Profile* page. The page style is the same as *Register | Login*, and users can go back to *Profile* page by clicking Gingerbread man icon or cancel button

- **Single Genre** (`/single_genre/<_id>.html`)<br>The pages where users can see all playlists of the same genre (eg: Rock) and access the selected *Playlist* page. The same navigation bar and footer are used as *Home*

- **All Genres** (`all_genres.html`)<br>The pages where users can see the genres as card and access the selected *Sinle Genre* page. The same navigation bar and footer are used as *Home*
  1. The CRUD features is accessible for Admin only in this page in the bottom as two cards, One for create and another one for edit and a detele button in each Genre Card as well.

- **Page 404** (`page_404.html`)<br>The page that informs users the page not found and takes them back to *Home* page safely. The page style is the same as *Register | Login*.

Summary of playlists and full playlists are accessible by any users. Summary of playlists are available on *Profile* and full playlists are available from the cards in *Library*, *Home* and *Single Genre* page.

Below is the chart of the website to show the core relationships between the pages. (Most of the pages are linked to each other subject to permission)<br>

![image](https://github.com/Mathias-SantAnna/Spoty-Share-List/blob/master/static/images/SiteMap2.0.png)<br>
> **Note:**<br>
> Decided to change the tile of following pages for better understanding of it's purpose: Playlists => Library, Genre => All Genres;

— **Back-end** —<br>
Users must have an account to create playlists so there is a **users collection** that has <ins>username</ins> and <ins>password</ins> as keys of the data. <ins>username</ins> in **users collections** is linked with the <ins>username</ins> in **playlists collection** because users who have an account can only create a Playlist and they create a Playlist in their own account. Same principle as <ins>username</ins> in **users collection** that users can only create a Playlist for the Music Genre available in a **Music Genre collection** so it is liked with <ins>playlist_name</ins> in **playlists collection**. Music Genre in **Music Genre collection** are editable by admin so it is created as an independent collection. The data in all the collections are retrievable and can be identified by the key or unique id of the object.

Below is the chart of the database to show the collections and their relationships.

![image](https://github.com/Mathias-SantAnna/Spoty-Share-List/blob/master/static/images/Collections%20SCHEMA.png)

> **Note:**<br>
> Decided to not use Artist collection for simplicity , and didn't have time to add newsletter feature

### Skeleton Plane

It is a mobile-first website because people usually bake with a playlist so a good mobile-first design helps users whose main purpose is seeing playlists. For users whose main purpose is creating and posting playlists, the form is also well designed on both mobile and desktop sizes. There are wireframes of mobile and desktop sizes for all the core pages of the website.

- [Wireframes: Home (`index.html`)](/workspace/Spoty-Share-List/wireframes/Home.png)

- [Wireframes: Login / Register (`login.html`)](/workspace/Spoty-Share-List/wireframes/Register_Login.png)

- [Wireframes: Profile (`profile.html`)](/workspace/Spoty-Share-List/wireframes/.png)

- [Wireframes: Playlist (`playlist.html`)](/workspace/Spoty-Share-List/wireframes/SinglePlaylist.png)

- [Wireframes: Playlists Library (`playlists.html`)](/workspace/Spoty-Share-List/wireframes/PlaylistsLibrary.png)

- [Wireframes: Create a Playlist (`add_playlist.html`)](/workspace/Spoty-Share-List/wireframes/CreateYourPlaylist.png)

- [Wireframes: Edit a Playlist (`edit_playlist.html`)](/workspace/Spoty-Share-List/wireframes/EditPlaylist.png)

- [Wireframes: Manage Genre (`manage_genre.html`)](/workspace/Spoty-Share-List/wireframes/ManageGenre(Admin).png)

### Surface Plane

— **Colour** —

Inspired in the famous music streaming service, the base color is lime green (#21E666). It is used as it is on some headings, texts as well as the navigation bar, footer, and slightly transparent colour is used for some background. Regular Black and White are used for some text and background when it needs contrast. Also the same lime green is used when it needs an accent on the website such as See playlist button, flash messages and hover effect.

[![Color-Palette.png](https://i.postimg.cc/gc8hRqR3/Color-Palette.png)](https://postimg.cc/MXZXJB9G)

— **Typography** —

For the Logo was used **Monserrat Classic**, **Moontime**, and **Blibker Thin**.
For (h1) and headings of other pages (h2) was also used **Monserrat**.

**Raleway**, which is also another type of This is a powerful typeface, is used for menu and other headings (h3 - h6) as it matches the image of the website well.

[From Spotify Fonts](https://www.designyourway.net/blog/typography/spotify-font/)

<div align="right"><a href="#top">🔝</a></div>

## WEBSITE CONSTRUCTION PLANS

This project contains both front-end and back-end so well-structured planning is required to do the work efficiently. Below is a summary of the plans.

1. Creating Database in MongoDB
1. Installing necessary Python frameworks, creating a Python file for the app and testing functions
1. Deploying the website in Heroku
1. Connecting Database and App
1. Creating parent HTML template with common sections (e.g. header & footer)
1. Creating *Register*, *Login*, *Profile* pages
1. Creating *Create*, *Edit* Playlist pages
1. Creating an single *Playlist* page pages
1. Creating *Create*, *Edit* (Manage Genre) pages
1. Creating *Home* page with top playlists and filter
1. Creating *404* page

Updating README.md and some testing is also done during the above process

<div align="right"><a href="#top">🔝</a></div>

## FEATURES

### Existing Features

- Create with **HTML5**, **CSS3** (with Materialize ), **JavaScript**, **Python** (Flask), **MongoDB** (Atlas)
- It consists of 1 base html file and 13 other html files
- Modal for confirmation of "Delete" function
- Upload Image For Each Playlist: Image data cannot be stored in MongoDB, so having image for Playlists is achieved by using image URL.
- Spotify Embed iframe, for a sample view of the Playlist selected. 
- For Admin Only:
  1. Access to manage Genres (CRUD) in all_genres.html,
    ![All Genres CRUD - Admin Only](/images/Admin-Genre-CRUD.png)
  1. Access to Edit and Delete playlist buttons in library.html
    ![Library Buttons - Admin Only](/images/Admin_Edit_Delete_Playlist_Btns.png)

### Features Left To Implement

- **Resetting Password When Users Forget It:** To achieve this, an e-mail address is probably required for creating an account. The current primary purpose of the website is to provide easy access to the platform so do not ask e-mail address to create an account. In addition, do not know how to implement this with my current skills, decide to leave this out.

- **Share Button:** Do not know how to achieve this with my current skill and do not have time to learn so decide to leave this out.

- **“Like” Reaction By Other Users:** Do not know how to achieve this with my current skill and do not have time to learn so decide to leave this out.

- **Customise Pagination Page Display:** Manage to do pagination as it is essential to make the website neat, however, do not know how to customise pagination page display (e.g. When there are more Playlists, it will show page 1, 2, 3, 4, 5, 6, 7...) and do not have time to look into details so decide to leave as it is.

- **Error Pages:** Only one type of error page (404) is set up for the project. Ideally, users should be directed to a specific error page depending on the type of the error, however, do not have time to implement this so leave this out.

- **Hook Up a Spotify API** Where the user can connect to it's Spotify account and there bring data like their playlists, all with two clicks. I'm very exciting to be able to implement this feature in the future. 

<div align="right"><a href="#top">🔝</a></div>

## TECHNOLOGIES USED

- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Materialize](materializecss.com/) (A modern responsive front-end framework based on Material Design) for the mainframe of the website
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language
- [Flask](https://flask.palletsprojects.com/) (a micro web framework written in Python) as the main framework of Python
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/) as database
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment (IDE)
- [Git](https://git-scm.com/) for local version control, keeping the files & documents
- [GitHub](https://github.com/) for online version control and keeping the files & documents
- [Heroku](https://www.heroku.com/) for deploying the website

<div align="right"><a href="#top">🔝</a></div>

## RESOURCES

### General Resources

- Code Institute Course Materials
- [Stack Overflow](https://stackoverflow.com/)
- [YouTube](https://www.youtube.com/)
- [W3schools](https://www.w3schools.com/)
- [Google](https://www.google.com/)

### Tools

- [Spotify For Developers](https://developer.spotify.com/documentation/widgets/guides/adding-a-spotify-embed/) to add a embed iframe to webpage
- [Balsamiq](https://balsamiq.com/) for wireframes
- [ImageResizer](https://imageresizer.com/) for resizing images
- [PostImages](https://postimages.org/) for hosting images online
- [PNG to ICO](https://hnet.com/png-to-ico/) for converting png to ico for favicon
- [Online Palette](https://www.onlinepalette.com/spotify/) for generate a colour Palette
- [Canva](https://www.canva.com/) for creating logos and some images
- [Regex Tester](https://www.regextester.com/94502) to create a Regex validation code
- [Multi Device Website Mockup Generator](http://techsini.com/multi-mockup/index.php) for mockup
- [Autoprefixer](https://autoprefixer.github.io/) for parsing CSS and add vendor prefixes
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [Jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

<div align="right"><a href="#top">🔝</a></div>

## PROJECT BARRIERS & SOLUTIONS

— **Syntax Issues** —

These were defenitelly the most commom issues that I had during these project. These little issues caused by syntax very hard to find. Specially in the beggining confusing the id that needs to be matched with the variable, such as "@app.route("/playlist/<playlist_id>") - as playlist_id". 
I was getting every time more confused thinking that was the functions that I wasn't fully understanding when in fact beacuse of Naming the libraries, pages and also functions was too similar. 
In the beggiging I didn't get much feedback into this part in a way to correct myself as I got towards the end with Rimom, that clarified that great majority of the confusion and frustation resulting of that was only because it. 
I had to rename playlists.html into Library.html, music_genres.html into All_Genre.html, and also the playlists.html as home was changed into index.html. Not only that but also understanding deeply how for loops and if statments work, and when and how to use them.


— **Jinga2 For Loop Issue** —

For a prefix list, such as tracks and artists, I was using a regular foor loop but having a few problems, creating new lines in the beggining and end of the text area, when edit page was open.
To fix that it was suggested to add a "-" in the beggining of the for loop and in the end as well. Such as:" {%- for track in playlist.playlist_tracks.splitlines() %}
{{ track }}{% endfor -%} ".
Probably there's still room for improvement here.
Solution found in: [TTL255 - Przemek Rogala's Blog](https://ttl255.com/jinja2-tutorial-part-2-loops-and-conditionals/).

— **Delete Modal Overlapping** —

I notice when implementing profile.html the delete modal was been overlapped by the second playlist card. It was fixed using the following: 
- class: "modal-overlay fade" 
- style="height: 18%; width: 20%;" 
- tabindex="-1"

— **Defensive Programme** —

There is a certain restriction on accessing pages. For example, *create playlist* page can be accessed by logged-in users, *edit playlist* can be accessed by the playlist owner only, so a good defensive programme is required to prevent non-authorised users from accessing them. Defensive programme when users logged-in is achieved easily (e.g. User A tries to access user B's playlist) however when a user is not logged in and do a manual test, it gives me a **KeyError:  "user"**. I've got this suggestion of `if "user" in session:`  can be used for this. Also other restrictions only available to Admin for maintanance of the content such as management of Playlists in the Library page and also Music Genres in the All_genre page (CRUD functions).

In this subject I have used Regex (module re) validation for the spotify_url. Where it gets the Url, validate with Regex, grabs a part of the url, slipts and return an array for object Id to be stored. For avoid malicius code or string to be passed into the database. Found in [Regex Tester](https://www.regextester.com/94502).

— **MongoDB/Heroku Application Error** —
The problem was with config vars int the cluster, and after that fixed it was identified that in MongoDB I forgot to create a query for the search function. After suggested by a tutor, and following the Code Inst. video I created the query as instructed, and it worked as expected.


<div align="right"><a href="#top">🔝</a></div>


### Test Strategy
#### **Summary**
Testing is required on all features and user stories documented in this README. 
All clickable links must redirect to the correct pages. All forms linked to MongoDB
must be tested to ensure they insert all given fields into the correct collections.

HTML Code must pass through the [W3C HTML Validator](https://validator.w3.org/#validate_by_uri).

CSS Code must pass through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

JavaScript code must pass through the [JSHint Validator](https://jshint.com/).

Python Code must pass through [PEP8 Validator](http://pep8online.com/)
#### **High Level Test Cases**
[Test Cases](Testing.md)

#### **Access Requirements**
Tester must have access to MongoDB in order to manually verify the insertion 
of records to users and events collections.

#### **Regression Testing**
All features previous tested during development in a local environment must be regression 
tested in production on the live website.

#### **Assumptions and Dependencies**
Testing is dependent on the website being deployed live on Heroku.

#### **Out of Scope**
Only test cases listed under High Level Test Cases will be performed as part of this 
testing effort.

### Test Results

Full test results can be found [here](Testing.md)

****
## Deployment

### Project Creation
To create this project I used the CI Gitpod Full Template by navigating 
[here](https://github.com/Code-Institute-Org/gitpod-full-template) and clicking the 'Use this template' button.

I was then directed to the create new repository from template page and entered in my desired repo name, then 
clicked Create repository from template button.

Once created, I navigated to my new repository on GitHub and clicked the Gitpod button which built my workspace.

The following commands were used for version control throughout the project:

* git add *filename* - This command was used to add files to the staging area before committing.

* git commit -m "commit message explaining the updates" - This command was used to to commit changes to the local repository.

* git push - This command is used to push all committed changes to the GitHub repository.


### Deployment to Heroku

**Create application:**
1. Navigate to Heroku.com and login.
1. Click on the new button.
1. Select create new app.
1. Enter the app name.
1. Select region.

**Set up connection to Github Repository:**

1. Click the deploy tab and select GitHub - Connect to GitHub.
1. A prompt to find a github repository to connect to will then be displayed.
1. Enter the repository name for the project and click search.
1. Once the repo has been found, click the connect button.

**Set environment variables:**

Click the settings tab and then click the Reveal Config Vars button and add the following:

1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (database name you want to connect to)
4. key: MONGO_URI, value: (mongo uri - This can be found in MongoDB by going to clusters > connect > connect to your application and substituting the password and 
    dbname that you set up in the link).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).

**Enable automatic deployment:**
1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Run Locally

**Note: The project will not run locally with database connections unless the user sets up an [env.py](https://pypi.org/project/env.py/) file configuring IP, PORT, 
MONGO_URI, MONGO_DBNAME and SECRET_KEY. You must have the connection details in order to do this. These details are private and not disclosed in this repository 
for security purposes.**

1. Navigate to the GitHub [Repository](https://github.com/Daisy-McG/Motorbike-Event-Finder).
1. Click the Code drop down menu.
1. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
1. Open your developement editor of choice and open a terminal window in a directory of your choice.
1. Use the 'git clone' command in terminal followed by the copied git URL.
1. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages:
> pip install -r requirements.txt

### Fork Project 

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point 
for your own idea. - Definition from [Github Docs](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).

1. Navigate to the GitHub Repository you want to fork.
1. On the top right of the page under the header, click the fork button.

1. This will create a duplicate of the full project in your GitHub Repository.


## CREDITS

### Code

— **HTML5** —

- [Materialize](materializecss.com/) for navigation bar, input forms, card displays, modals and dropdown menus.


— **CSS3** —

- [Materialize Classes and colours](materializecss.com/) for styling.


— **JavaScript** —

- [Spotify Web Playback SDK](https://developer.spotify.com/documentation/web-playback-sdk/quick-start/) client-side JavaScript library which allows you to create a new player in Spotify Connect and play any audio track from Spotify in the browser via Encrypted Media Extensions.

— **Python** —

- [TTL255 - Przemek Rogala's Blog](https://ttl255.com/jinja2-tutorial-part-2-loops-and-conditionals/) Jinga2 for loops
- [Ed Bradley](https://github.com/Edb83/self-isolution/blob/master/app.py) for reference.



### Contents

— **Playlists** —
> Almost every image has been collected from spotify website

>Tracks titles, Artitst names, and Url also from the same playlist in spotify
- [Spotify web player](https://open.spotify.com/)


## ACKNOWLEDGEMENTS

I would like to thank:

- My deer friend and personal mentor, **Rimom Costa**, for going through the project with me and giving a lots of advice and taking so much time for teaching and helping me when I needed the most. (If it wasn't for him I wouldn't have finished it)

- For all Code Institute Tutors, **Michael**, **Stephen**, **Igor** and **Sheryl**, for giving me a guidance on how to solve different issues
- **Ed Bradley** for the meeting about MS3 and explainig very carefully each subject.
- **Antonio R.** for giving me advice on some subjects and helping with the project

<div align="right"><a href="#top">🔝</a></div>

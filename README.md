# Spoty Share List 
<h2 align="center"><img src="https://i.postimg.cc/CLWV9npc/Big-Logo-Read-Me.gif"></h2>

It's a mobile-first &#38; responsive web application for sharing Playlists with it's users. The objective is to intensify and amplify the usage of music streaming services like Spotify® 🎶
Link to the website is available [HERE.](https://spoty-share-list.herokuapp.com/home)

<br>

# Table of Contents

- [Spoty Share List](#Spoty-Share-List)
- [UX](#ux)
  * [General](##WHO'S-THIS-WEBSITE-FOR)
  * [User Stories](#user-stories)
  * [Wireframes](#wireframes)
- [Features](#features)
  * [Paylists Library](#playlists-library)
  * [Navigation](#navigation)
  * [Footer](#footer)
  * [Register](#register)
  * [Log In](#log-in)
  * [User Tools](#user-tools)
  * [User Profile](#user-profile)
  * [Create a Playlist](#create-a-Playlist)
  * [404 pages](#404-pages)
  * [Search](#search)
- [Features to implement in future updates](#features-to-implement-in-future-updates)
- [User Types and permissions](#user-types-and-permissions)
  * [Visitor](#visitor)
  * [User](#user)
  * [Admin](#admin)
## WHO'S THIS WEBSITE FOR
Since everyone loves music (and I even more 🤟), why not do something enjoyable  and productive in the same time. As we all know, these days the consumption of the streaming services are only growing, and a great tool to have is to be part of a awesome group of people with great music taste (some may discord) where you can create, edit, share your Playlists and much more...(more features to be added in the future). The website is designed for the user that desires to share their playlists and find new ones in a very simple and easy way that the first time visitor can adapt fairly quickly...CONTINUE 💚 🎧 🎸  🎼 🎵 

## User Experience Planes

### Strategy Plane
The website is designed for the people who would like to share and find different spotify playlists, add to their own catalog, share with friends, while working, excercing or just for the fun or it, it's a great tool of motivation, scientifically proofed to increased someone's performance up to 30%. Following simple steps users can Register to create an account, to create a new Playlist in a very easy way. 
To open a specific playlist the visitor don't need to register himself, going to Search field they can find any existing playlist that matches the input field. The Library with all playlists is hidden for visitor to make them sign up in order to add a playlist and browse for mode content such Genres.

Registered users see all the playlists shown (Library), or browse by music genre(All Genres), or even by details (Search). Also they can click in the embed iframe field that would send them to the existing playlist in Spotify. A search field is on these pages to help the user to find what they're looking for, using a specific keyword(s).  The website design is simple and user friendly for the first-time visitor easily start navigating. Also for creating a new playlist is a set of instructions for the "hardest parts" like to add a Url for the specific spotify. 

All the functions on the tables below are minimum requirements on the website to achieve the current user's and owner's goals. &#40;On a scale of 1 &#91;least&#93; - 5 &#91;most&#93;&#41;.

| Opportunity                                   | Importance |         Viability         |
| :-------------------------------------------- | :--------: | :---------------------: |
| Register                                      |     5      |            5            |
| Login / Log out                               |     5      |            5            |
| Create / Edit / Delete Playlists              |     5      |            4            |
| Search Playlist By Keywords                   |     4      |            5            |
| Show Playlists By Genre                       |     4      |            5            |
| Responsiveness                                |     4      |            5            |
| Manage Playlist Genre &#40;Admin only&#41;    |     3      |            5            |
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


  <div align="right"><a href="#top">🔝</a></div


## Scope Plane

To achieve user my project goals, below are the minimum features to be included in this project. Also, **CRUD** &#40;Create, Read, Update, and Delete&#41; functions are required for this project so these are implemented as a part of essential features.

- Simple design Home page that first-time users can recognise the purpose of the website easily. All the playlists are shown on *Home* page &#40;R&#41;
- Music Genre &#40;Metal, Dance & Electro, Rock&#41; pages where users can see playlists by the Music Genre &#40;R&#41;
- Register page where users can create an account to create, post and edit playlists
- Login page where users can log in to the website
- Logout function that users can log out the website
- Profile page where users can see all their playlists and access to create, post, edit and delete playlists
- Create Playlist page where users can create and post their playlists &#40;C&#41;
- Edit Playlist page where users can edit their playlists &#40;U&#41;
- Delete Playlist function that users can delete their playlists &#40;D&#41;
- Manage playlist page and functions that only <ins>admin user</ins> &#40;owner&#41; can create, edit and delete Music Genre &#40;C & U & D&#41;
- Search by a keyword&#40;s&#41; function that users can search for specific playlists
- Subscribe to newsletter function to collect users e-mail addresses
- 404 page that appears for invalid URL and takes users back to *Home* page of the website safely

> **Note:**<br>
> Initially, only 3 fixed Music Genre are planned for playlists, however as the project is created, discover that a newly created playlist can be implemented on the website by using loop so Music Genre are not limited. &#40;e.g. If the admin decides to create a new playlist called "Birthday", it can be implemented to the website automatically&#41;

### Structure Plane

— **Front-end** —

The website consists of a **Home** page with **13 other core pages**.

- **Home** &#40;`index.html`&#41;<br>The main page of the website. There is a logo, navigation bar to *Music Genre*, *Register* & *Login* pages, a title and a hero image. All the summary of playlists are contained and users can access a full *Playlist* page. There is a footer with a form to subscribe to newsletter and some social icons

- **Search Result** &#40;`search.html`&#41;<br>The page where users can see playlists by search and access a full *Playlist* page. The same navigation bar and footer are used as *Home* *Idea of having this page comes up during the project

- **Music Genre** &#40;`Music Genre_<genre_name>.html`&#41;<br>The pages where users can see playlists by playlist and access a full *Playlist* page. The same navigation bar and footer are used as *Home*

- **Playlist** &#40;`Playlist.html`&#41;<br>The page where a full Playlist is shown individually. The same navigation bar and footer are used as *Home*

- **Register** &#40;`register.html`&#41;<br>The page where users can create an account. Once users create an account successfully, they will be led to *Profile* page. The navigation bar is different to *Home* page, in which users can go back to *Home* page by clicking Uncle Jam's icon, and there is no footer

- **Login** &#40;`login.html`&#41;<br>The page where users who have an account can log in to the website. Once users log in successfully, they will be led to *Profile* page. The navigation bar is different to *Home* page, in which users can go back to *Home* page by clicking Uncle Jam's icon, and there is no footer

- **Profile** &#40;`profile.html`&#41;<br>The page where users will be led when they create an account or log in. Users see all of their playlists with an option to edit&#47;delete. Users can access to *Edit Playlist* page and *Delete Playlist* function by clicking a button on the Playlist. There is an option to create a new Playlist from this page by clicking a button and that leads to *Create Playlist* page. The same navigation bar and footer are used as *Home* but there is a *Logout* function instead of *Register* and *Login*. There is also a link to *Profile* page on the navigation bar

- **Create Playlist** &#40;`add_playlist.html`&#41;<br>The page where users can create and post playlists. There is no link on the navigation bar and it can only be accessed by clicking a Create Playlist button on *Profile* page. The page style is the same as *Register | Login*, and users can go back to *Profile* page by clicking Gingerbread man icon or cancel button

- **Edit Playlist** &#40;`edit_playlist.html`&#41;<br>The page where users can edit playlists. There is no link on the navigation bar and it can only be accessed by clicking an Edit button on *Profile* page. The page style is the same as *Register | Login*, and users can go back to *Profile* page by clicking Gingerbread man icon or cancel button

- **Edit Genre** &#40;`edit_genre.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can access to create and edit Music genre pages as well as to delete Music Genre. Only admin user can have an access to this page by a navigation link that appears on *Profile* page for admin. The page style is the same as *Home*

- **Create Genre** &#40;`add_genre.html`&#41;<br>The page where only <ins>admin user</ins> &#40;owner&#41; can create Music Genre. The page style is the same as *Register | Login*, and admin user can go back to *Manage playlist* page by clicking Tools icon or cancel button

- **Page 404** &#40;`page_404.html`&#41;<br>The page that informs users the page not found and takes them back to *Home* page safely. The page style is the same as *Register | Login*.

Summary of playlists and full playlists are accessible by any users. Summary of playlists are available on *Home* and *Music Genre* pages and full playlists are available on *Playlists* page.

Below is the chart of the website to show the core relationships between the pages. &#40;Most of the pages are linked to each other subject to permission&#41;<br>

![image](https://github.com/Mathias-SantAnna/Spoty-Share-List/blob/master/static/images/SiteMap2.0.png)<br>

— **Back-end** —<br>
Users must have an account to create playlists so there is a **users collection** that has <ins>username</ins> and <ins>password</ins> as keys of the data. <ins>username</ins> in **users collections** is linked with the <ins>username</ins> in **playlists collection** because users who have an account can only create a Playlist and they create a Playlist in their own account. Same principle as <ins>username</ins> in **users collection** that users can only create a Playlist for the Music Genre available in a **Music Genre collection** so it is liked with <ins>playlist_name</ins> in **playlists collection**. Music Genre in **Music Genre collection** are editable by admin so it is created as an independent collection. Data in **subscription collection** is independent data for newsletters because users who do not have an account can also subscribe to it if they wish to do. The data in all the collections are retrievable and can be identified by the key or unique id of the object.

Below is the chart of the database to show the collections and their relationships.

![image](https://github.com/Mathias-SantAnna/Spoty-Share-List/blob/master/static/images/Collections%20SCHEMA.png)

> **Note:**<br>
> On the subscription collection, subs_name is listed but the subscribe function collects e-mail address only

### Skeleton Plane

It is a mobile-first website because people usually bake with a playlist so a good mobile-first design helps users whose main purpose is seeing playlists. For users whose main purpose is creating and posting playlists, the form is also well designed on both mobile and desktop sizes. There are wireframes of mobile and desktop sizes for all the core pages of the website.

- [Wireframes: Home &#40;`index.html`&#41;](/workspace/Spoty-Share-List/wireframes/Home.png)

- [Wireframes: Login / Register &#40;`login.html`&#41;](/workspace/Spoty-Share-List/wireframes/Register_Login.png) UPDATE LATER!!

- [Wireframes: Profile &#40;`profile.html`&#41;](/workspace/Spoty-Share-List/wireframes/.png)

- [Wireframes: Playlist &#40;`playlist.html`&#41;](/workspace/Spoty-Share-List/wireframes/SinglePlaylist.png)

- [Wireframes: Playlists Library &#40;`playlists.html`&#41;](/workspace/Spoty-Share-List/wireframes/PlaylistsLibrary.png)

- [Wireframes: Create a Playlist &#40;`add_playlist.html`&#41;](/workspace/Spoty-Share-List/wireframes/CreateYourPlaylist.png)

- [Wireframes: Edit a Playlist &#40;`edit_playlist.html`&#41;](/workspace/Spoty-Share-List/wireframes/EditPlaylist.png)

- [Wireframes: Manage Genre &#40;`manage_genre.html`&#41;](/workspace/Spoty-Share-List/wireframes/ManageGenre(Admin).png) UPDATE LATER!

### Surface Plane

— **Colour** —

Inspired in the famous music streaming service, the base color is lime green &#40;#21E666&#41;. It is used as it is on some headings, texts as well as the navigation bar, footer, and slightly transparent colour is used for some background. Regular Black and White are used for some text and background when it needs contrast. Also the same lime green is used when it needs an accent on the website such as See playlist button, flash messages and hover effect.

[![Color-Palette.png](https://i.postimg.cc/gc8hRqR3/Color-Palette.png)](https://postimg.cc/MXZXJB9G)

— **Typography** —

For the Logo was used **Monserrat Classic**, **Moontime**, and **Blibker Thin**.
For &#40;h1&#41; and headings of other pages &#40;h2&#41; was also used **Monserrat**.

**Raleway**, which is also another type of This is a powerful typeface, is used for menu and other headings &#40;h3 - h6&#41; as it matches the image of the website well.

[From Spotify Fonts](https://www.designyourway.net/blog/typography/spotify-font/)

<div align="right"><a href="#top">🔝</a></div>

## WEBSITE CONSTRUCTION PLANS

This project contains both front-end and back-end so well-structured planning is required to do the work efficiently. Below is a summary of the plans.

1. Creating Database in MongoDB
1. Installing necessary Python frameworks, creating a Python file for the app and testing functions
1. Deploying the website in Heroku
1. Connecting Database and App
1. Creating parent HTML template with common sections &#40;e.g. header & footer&#41;
1. Creating *Register*, *Login*, *Profile* pages
1. Creating *Create*, *Edit* Playlist pages
1. Creating an single *Playlist* page pages
1. Creating *Create*, *Edit* &#40;Manage Genre&#41; pages
1. Creating *Home* page with top playlists and filter
1. Creating *404* page

Updating README.md and some testing is also done during the above process

<div align="right"><a href="#top">🔝</a></div>

## FEATURES

### Existing Features

- Create with **HTML5**, **CSS3** &#40;with Materialize &#41;, **JavaScript**, **Python** &#40;Flask&#41;, **MongoDB** &#40;Atlas&#41;
- It consists of 1 base html file and 13 other html files
- Modal for "Create Playlist" instructions and confirmation for "Delete" function
- Upload Image For Each Playlist: Image data cannot be stored in MongoDB, so having image for Playlists is achieved by using image URL.
- Spotify Embed iframe, for a sample view of the Playlist selected. 
- CONTINUE... ???

### Features Left To Implement

- **Resetting Password When Users Forget It:** To achieve this, an e-mail address is probably required for creating an account. The current primary purpose of the website is to provide easy access to the platform so do not ask e-mail address to create an account. In addition, do not know how to implement this with my current skills, decide to leave this out.

- **Share Button:** Do not know how to achieve this with my current skill and do not have time to learn so decide to leave this out.

- **“Like” Reaction By Other Users:** Do not know how to achieve this with my current skill and do not have time to learn so decide to leave this out.

- **Customise Pagination Page Display:** Manage to do pagination as it is essential to make the website neat, however, do not know how to customise pagination page display &#40;e.g. When there are more Playlists, it will show page 1, 2, 3, 4, 5, 6, 7...&#41; and do not have time to look into details so decide to leave as it is.

- **Error Pages:** Only one type of error page &#40;404&#41; is set up for the project. Ideally, users should be directed to a specific error page depending on the type of the error, however, do not have time to implement this so leave this out.

- **Hook Up a Spotify API** Where the user can connect to it's Spotify account and there bring data like their playlists, all with two clicks. I'm very exciting to be able to implement this feature in the future. 

<div align="right"><a href="#top">🔝</a></div>

## TECHNOLOGIES USED

- [HTML5](https://en.wikipedia.org/wiki/HTML) for markup
- [CSS3](https://en.wikipedia.org/wiki/CSS) for style
- [Materialize](materializecss.com/) &#40;A modern responsive front-end framework based on Material Design&#41; for the mainframe of the website
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for interaction
- [Python3](https://www.python.org/) as a backend programming language
- [Flask](https://flask.palletsprojects.com/) &#40;a micro web framework written in Python&#41; as the main framework of Python
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/) as database
- [Google Fonts](https://fonts.google.com/) for fonts
- [Font Awesome](https://fontawesome.com/) for icons
- [Gitpod](https://www.gitpod.io/) as Integrated Development Environment &#40;IDE&#41;
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
- [Multi Device Website Mockup Generator](http://techsini.com/multi-mockup/index.php) for mockup
- [Autoprefixer](https://autoprefixer.github.io/) for parsing CSS and add vendor prefixes
- [W3C Markup Validation Service](https://validator.w3.org/) for testing HTML code
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) for testing CSS code
- [Jshint](https://jshint.com/) for testing JavaScript code
- [PEP8 Online](http://pep8online.com/) for checking Python code compliance
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) for testing, style checking and debugging

<div align="right"><a href="#top">🔝</a></div>
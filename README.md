# Spoty Share List 
<h2 align="center"><img src="https://i.postimg.cc/CLWV9npc/Big-Logo-Read-Me.gif"></h2>

It's a mobile-first &#38; responsive web application for sharing Playlists with it's users. The objective is to intensify and amplify the usage of music streaming services like Spotify® 🎶
Link to the website is available [HERE.](https://spoty-share-list.herokuapp.com/home)

<br>

# Table of Contents

- [Spoty Share List](#Spoty-Share-List)
- [UX](#ux)
  * [General](#WHO'S THIS WEBSITE FOR)
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
The website is designed for the people who would like to share and find different spotify playlists, add to their own catalog, share with friends, while working, excercing or just for the fun or it, it's a great tool of motivation, scientofically proofed to increased someone's performance up to 30%.Following simple steps users can Register to create an account, to create a new Playlist in a very easy way. Users which are just visiting can see all the playlists shown by post date, or browse by music genre(Music Genre), or even by artists. Also they can click in the playlist url field that would send them to the existing playlist in Spotify. A search field is on these pages to help the user to find what they're looking for, using a specific keyword(s). To open a specific playlist the visitor don't need to register himself, only for adding new ones, editing or deleting your playlists. The website design is simple and user friendly for the first-time visitor easily start navigating. Also for creating a new playlist is a set of instructions for the "hardest parts" like to add a Url for the specific spotify. 

All the functions on the tables below are minimum requirements on the website to achieve the current user's and owner's goals. &#40;On a scale of 1 &#91;least&#93; - 5 &#91;most&#93;&#41;.

| Opportunity                                   | Importance |         Viability         |
| :-------------------------------------------- | :--------: | :---------------------: |
| Register                                      |     5      |            5            |
| Login / Log out                               |     5      |            5            |
| Create / Edit / Delete Playlists              |     5      |            4            |
| Search Playlist By Keywords                   |     4      |            5            |
| Show Playlists By Genre                       |     4      |            5            |
| Responsiveness                                |     4      |            5            |
| Subscribe To Newsletter                       |     4      |            4            |
| Manage Playlist Genre &#40;Admin only&#41;    |     3      |            5            |
| Page 404                                      |     3      |            4            |

There is some other functions to implement in the website, however, these are not mandatory to achieve the current project goals. Because of lack of time or knowledge, most of these features will only implemented in the future.

| Opportunity                             | Importance |        Viability        |
| :-------------------------------------- | :--------: | :---------------------: |
| Upload Image For Each Playlist          |     4      |            4            |
| Upload Spotify Url For Each Playlist    |     4      |            3            |
| Pagination                              |     3      |            3            |
| User profile favorite Genre & Artists   |     3      |            2            |
| Resetting Password When Users Forget It |     3      |            2            |
| Review By Other Users                   |     3      |            2            |
| “Like” Button By Other Users            |     3      |            2            |


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

![image](https://github.com/Mathias-SantAnna/Spoty-Share-List/blob/master/static/images/Collections%20SCHEMA.png

> **Note:**<br>
> On the subscription collection, subs_name is listed but the subscribe function collects e-mail address only

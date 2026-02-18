Django Blog Project Documentation
Project Overview

The Django Blog Project is a full-featured blogging platform where users can register, log in, create posts, comment on posts, assign tags to posts, and search for content. The project is designed to demonstrate Django's capabilities in user authentication, CRUD operations, comment handling, tagging, and search functionality.

1. User Authentication & Profile Management
   Features Implemented

User Registration (RegisterForm)

User Login and Logout (LoginView, LogoutView)

Profile Update (ProfileUpdateForm)

Views

home(request) – displays the homepage.

register(request) – allows new users to sign up.

profile(request) – lets authenticated users update their username and email.

Forms

RegisterForm – extends UserCreationForm, adding an email field.

ProfileUpdateForm – updates username and email for existing users.

URLs
/ -> home
/login/ -> login page
/logout/ -> logout and redirect to home
/register/ -> registration page
/profile/ -> profile management

2. Blog Post CRUD Operations
   Models

Post – fields: title, content, author, published_date.

Posts are related to User via a foreign key (author).

Views

PostListView – lists all posts (latest first).

PostDetailView – shows details of a single post.

PostCreateView – allows logged-in users to create posts.

PostUpdateView – allows authors to update their posts.

PostDeleteView – allows authors to delete their posts.

Forms

PostForm – handles post creation and editing.

URLs
/post/ -> post list
/post/new/ -> create post
/post/<int:pk>/ -> view post details
/post/<int:pk>/update/ -> edit post
/post/<int:pk>/delete/ -> delete post

3. Comment Functionality
   Models

Comment – fields: post, author, content, created_at, updated_at.

Each comment is linked to a Post and a User.

Views

CommentCreateView – allows logged-in users to add a comment to a post.

CommentUpdateView – allows comment authors to update their comment.

CommentDeleteView – allows comment authors to delete their comment.

Forms

CommentForm – handles creating and updating comments.

URLs
/post/<int:pk>/comments/new/ -> create comment for post
/comment/<int:pk>/update/ -> edit comment
/comment/<int:pk>/delete/ -> delete comment

Templates

comment_form.html – used for both creating and editing comments.

comment_confirm_delete.html – confirms deletion.

4. Tagging and Search Functionality
   Models

Tag – stores tag names, linked to Post via a many-to-many field.

Updated Post model:

tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

Forms

PostForm updated to handle tags using a custom widget TagWidget.

Tags are entered as comma-separated values.

Views

PostByTagListView – lists all posts associated with a specific tag (class-based view).

search_posts(request) – handles search queries for title, content, or tags.

URLs
/tags/<slug:tag_slug>/ -> show posts with a specific tag
/search/ -> search posts by keyword

Templates

Updated post_list.html and post_detail.html to display associated tags.

Each tag is a clickable link that filters posts by that tag.

Search bar added in template to query posts.

Key Features Summary
Feature Implementation
User Registration & Login RegisterForm, LoginView, LogoutView
Profile Update ProfileUpdateForm
CRUD for Posts PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
CRUD for Comments CommentCreateView, CommentUpdateView, CommentDeleteView
Tagging System Tag model, many-to-many in Post, PostForm with TagWidget
Search Functionality search_posts view using Q objects
URL Routing Clean, intuitive URLs for posts, comments, tags, and search
Templates Custom templates for posts, comments, tags, and search
How to Use the Features

Authentication

Register a new account using /register/.

Log in via /login/.

Update your username/email on /profile/.

Posts

Create a new post on /post/new/.

Edit/delete your posts using links on the post detail page.

View all posts on /post/.

Comments

Add a comment on a post detail page.

Edit/delete your comments using links next to your comment.

Tags

Add tags while creating or editing posts.

Click on a tag to view all posts with that tag: /tags/<tag_slug>/.

Search

Use the search bar to find posts by title, content, or tag: /search/?q=keyword.

Conclusion

This Django Blog Project demonstrates:

Full CRUD operations for posts and comments

User authentication and profile management

Tagging system with many-to-many relationships

Search functionality for posts

Clean URL patterns and reusable templates

All components are designed to work seamlessly together, with proper permission checks ensuring only authorized users can modify posts and comments.

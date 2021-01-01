# Lab: Django Models

## Overview

Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

Today you'll build out a project with one model and wire up that model using Django Views.


## Feature Tasks and Requirements

- create `blog_project` project
- create `blog` app
- migrate data
- create `Post` model
    - add `title` as a CharField with maximum length of 64 characters.
    - add `author` ForeignKey related to Django's built in user model with CASCADE delete option.
    - add `body` TextField
- add model to admin
- modify `Post` model have user friendly display in admin
- create migrations and migrate data
- create a super user
- Add a few posts via Admin panel
- Add`templates` folder in root of project
  - register `templates` folder in project settings
- create `HomePageView`
  - extend `ListView`
  - give a template of `home.html`
  - associate `Post` model
- create `home.html` template
  - use `Django Templating Language` to display each post's title
- create `base.html` ancestor template
  - add main html document
  - use `Django Templating Language` to allow child templates to insert content
- update url patterns for app and project
- view home page and confirm posts showing properly
- add detail view
  - link `post_detail.html` template
  - associate `Post` model
- create `post_detail.html` template
  - template should extend base
  - content should display post title and body
- update app urlpatterns to handle detail view
  - account for primary key in url
- add link in home page template to related post detail page

## Implementation Notes

- The instructions are becoming more conceptual. 
- All the concepts listed relate to key Django steps covered in the demo.
- If there is confusion about what, exactly, is required then ask the client (aka the instructors.)
- **TLDR** - make your lab project like the demo project.

### User Acceptance Tests

- Test `HomePageViewTest`
  - verify status code
  - verify correct template use
  - use url *name* instead of hard coded path

- We can't test `PostDetailView` until next class.
	- Can you figure out why?  

## Configuration

- Create `django-models` GitHub repository.
- Use `poetry` to manage virtual environment and dependencies.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

## Stretch Goals

- add styling
  - create static folder at root of project
  - update STATICFILES_DIRS
  - create base.css file which styles base.html elements
  - load static css in base.html file
- Test PostDetailView
- Test Post model
- add multiple models
- use an alternate test runner
- add more advanced fields to models, e.g. created time stamp


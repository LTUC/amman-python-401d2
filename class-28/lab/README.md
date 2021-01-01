# Lab: Django CRUD and Forms

## Overview

Add full CRUD functionality to your bag of tricks by building a Django project that allows Creating, Reading, Updating and Deleting.

## Feature Tasks and Requirements

**NOTE**: replace `blog` and `Post` with your own names.

- Create `blog_project` Django project
- Create `blog` app
- Create `Post` model
  - title field
  - author field
  - body field
  - Register model with admin
- Create `BlogListView` that extends appropriate generic view
  - associated url path is an empty string
- Create `BlogDetailView` that extends appropriate generic view
  - associated url path is `post/<int:pk>/`
- Create `BlogCreateView` that extends appropriate generic view
  - associated url path is `post/new/`
- Create `BlogUpdateView` that extends appropriate generic view
  - associated url path is `post/<int:pk>/edit/`
- Create `BlogDeleteView` that extends appropriate generic view
  - associated url path is `post/<int:pk>/delete/`
- Add urls to support all views, with appropriate names
- Add templates to support all views
- Add navigation links in appropriate locations to access all pages
- Make all necessary changes to project level files for project to run
  - In other words, make it work

## Implementation Notes

A lot of functionality is being added here. But it should still follow the "Django way." So when in doubt refer back to demo.

## Stretch Goals

- add multiple models
- use an alternate test runner
- add more advanced fields to models, e.g. created time stamp
- add styling

### User Acceptance Tests

- Test all Views
- Test Model
  - string representation
  - all fields
- When in doubt on what to test refer to demo

## Configuration

Use `poetry` to create `django-crud` project.

```console
> $ mkdir django-crud
> $ cd django-crud
> $ poetry init -n
> $ poetry add [required libraries]
> $ poetry shell
```

Use `django-crud` folder as the root of your project's git repository.

Refer to [Lab Submission Instructions](../../../reference/submission-instructions/labs/){:target="_blank"} for detailed instructions.

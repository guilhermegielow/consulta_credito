# Category Tree App
[![Build Status](https://travis-ci.org/lamenezes/olist-categories.svg?branch=master)](https://travis-ci.org/lamenezes/olist-categories)
[![Coverage Status](https://coveralls.io/repos/github/lamenezes/olist-categories/badge.svg?branch=master)](https://coveralls.io/github/lamenezes/olist-categories?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/dd99157ada1b43c1817d10df294c26bb)](https://www.codacy.com/app/luiz-menezesf/olist-categories)

## Working Example

[http://olist-lm.herokuapp.com/api/](http://olist-lm.herokuapp.com/api/)

## Specification

This project provides an API to browse channels and categories to allow sellers
to publish products in channels. It is possible to import categories to a channel
using the `python manage.py importcategories` command.


All published products need to be categorized in one of channels' categories.


All channels group the products published in categories that are arranged as a
tree of *varying depths* (from 1 to infinite levels of hierarchy). See version
an small example below:

- Books
  - National Literature
    - Science fiction
    - Fantastic Fiction
  - Foreign literature
  - Computers
    - Applications
    - Database
    - Programming
- Games
  - XBOX 360
    - Console
    - Games
    - Accessories
  - XBOX One
    - Console
    - Games
    - Accessories
  - Playstation 4
- Computing
  - Notebooks
  - Tablets
  - Desktop


Each channel sends us a CSV file where one of the columns (`Category`) is
contains the full category's path:

```
Category
Books
Books / National Literature
Books / National Literature / Science Fiction
Books / National Literature / Fiction Fantastic
Books / Foreign Literature
Books / Computers
Books / Computers / Applications
Books / Computers / Database
Books / Computers / Programming
Games
Games / XBOX 360
Games / XBOX 360 / Console
Games / XBOX 360 / Games
Games / XBOX 360 / Accessories
Games / XBOX One
Games / XBOX One / Console
Games / XBOX One / Games
Games / XBOX One / Accessories
Games / Playstation 4
Computers
Computers / Notebooks
Computers / Tablets
Computers / Desktop
```


## Project Requirements

The project requires:

- Python >= 3.5
- Django >= 1.9
- Relational database
- django-MPTT (optmizes read operations on the categories trees)
- rest_framework
- django-filter
- prettyconf

## Project Funcionalities:

- A *Django Management Command* to import the channels' categories from a CSV.
  - Import command operates in "full update" mode, ie it overwrites
    all categories of a channel with the categories in CSV.
  - The command receives 2 arguments: channel name (create the channel if
    it doesn't exists in database) and the name of `.csv` file:
  - The CSV file must be organized in a way that no parent category appears
    *after* its children.

```
$ python manage.py importcategories walmart categories.csv
```

- Each channel has its own set of categories.
- Each channel has a unique identifier and a field with the channel's name.
- Each category has a unique identifier and a field with the category's name.
- A HTTP REST API that provides the following functionalities:
  - List existing channels and all their categories.
  - List details of a channel containing all its categories and subcategories.
  - Return a single category with their parent categories and subcategories, i.e.
    their family.

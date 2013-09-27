# url2markdown

This is a very simple web service that will take a given URL, and return
a Markdown representation of that page.

Powered by [Readability](http://readability.com/), [Requests](http://python-guide.org/), [html2text](http://www.aaronsw.com/2002/html2text/) and [Flask](http://flask.pocoo.org/).

## Usage


    $ curl http://url2markdown.herokuapp.com/url=http://kennethreitz.

    My name is Kenneth Reitz.

    I am a wandering street photographer, musician, and moral fallibilist.

    I'm the product owner of Python at Heroku and a member of the Python Software
    Foundation. I believe that simplicity is always better than functionality.
    ...

Enjoy!

## Configuration

This application requires a [Readability Parser Token](http://www.readability.com/developers/api/parser).

    $ export READABILITY_TOKEN=xxxxxx

You can use [autoenv](https://github.com/kennethreitz/autoenv) to do this easily.

## License

Unfortunately, this code is released under [GPLv3](http://www.gnu.org/copyleft/gpl.html).
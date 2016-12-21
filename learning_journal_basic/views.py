"""The views module is the logic behind rendering the templates."""
# from pyramid.response import Response
from pyramid.view import view_config
import io
import os


THIS_DIR = os.path.dirname(__file__)

ENTRIES = {
    1: {"id": 1,
    "title": "Jinja2 Templates and Binary Heap",
    "creation_date": "December 20, 2016",
    "body": """Pyramid, jinja2, binary heap, prepping for my lightning talk. Kudos to those who can get everything to work, and can complete every assignment on-time. Well, that's not me. Struggled with the jinja2 and passing the id correctly to bring up the correct article. And that was with Rachael, Ben, and Will's help. Working with Ted on the Binary Heap was great, but I wasn't able to finish doing all of the tests. Excited to learn with my project team how to scrape and then assemble info off 3rd party sites. Coming from the SEO world, I know of black hats who use scraping to aggregate content, change it slightly, and then re-publish it as their own content. At this hour, I guess the question is sleep or work."""},
    2: {"id": 2,
    "title": "Pyramid Framework",
    "creation_date": "December 19, 2016",
    "body": """TIL, Git is a still an issue for me at times. (Go, go Patrick's Git idea). I also learned if you make a mistake early in the setup of a long process in class, there's no way to catch up, and you're better off just watching what Nick does and take good notes (see Pyramid/Heroku setups). I re-learned about checking for which python version you use. I learned I still hate CSS ("there's no CSS in Python", once said by one sage instructor). The pyramid framework was more rote learning, and probably the easiest part of the 2nd assignment. The complication about how you setup your files and repo, that caused all the pain."""},
    3: {"id": 3,
    "title": "HTTP Server",
    "creation_date": "December 16, 2016",
    "body": """os.path to determine absolute path, listdir, mimetype detection, detect whether a file or a directory... I learned a lot in lab today on the http server project, despite the rabbit holes and complete refactoring needing to be done halfway through, and still way behind. It's tough with missing team members, who then come back and aren't as up to speed - especially when you're scrambling and under the gun to accomplish so much in a day, and not get even further behind. This weekend is gonna be a doozy. We also learned concurrency and asynchronous connections in class - I think we get to use that today."""},
}


@view_config(route_name="list", renderer="templates/list.jinja2")
def list(request):
    """View for the home page."""
    return {"entries": ENTRIES.values()}



@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail(request):
    """View for the detail page."""
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[id]
    return {"entry": entry, "id": the_id}


@view_config(route_name="create", renderer="templates/create.jinja2")
def create(request):
    """View for the create page."""
    return {"entries": ENTRIES.values()}

@view_config(route_name="edit", renderer="templates/edit.jinja2")
def edit(request):
    """View for the edit page."""
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[id]
    return {"entry": entry, "id": the_id}

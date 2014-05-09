
from boogs import BugBuilder

if __name__ == "__main__":

    #
    # The Builders return a request, which is a named tuple containing
    # url, method, params, headers, body that you can use in your http
    # client
    #

    #request = boogs.BugBuilder("https://bugzilla.mozilla.org").build_your_query_here.build()
    #r = request.get(request.url, params=request.params, headers=request.headers)
    #r.raise_for_status()
    #bugs = r.json()

    #
    # Getting a single bug
    #

    # Get a single bug without logging in
    request = BugBuilder().id(36).build()
    print request

    # Get a single bug without logging in, limit the number of fields
    request = BugBuilder("https://bugzilla.mozilla.org").id(36).fields("cc","assigned_to","summary").build()
    print request

    # Get a single bug with a token
    request = BugBuilder("https://bugzilla.mozilla.org", token="t0k3n").id(36).build()
    print request

    # Get a single bug with login and password
    request = BugBuilder("https://bugzilla.mozilla.org", credentials=("stefan","secret")).id(36).build()
    print request

    # #
    # # Searching for bugs. And retrieving many bugs at a time.
    # #

    # # Get many bugs at once
    bug_ids = (36, 37, 38)
    request = BugBuilder("https://bugzilla.mozilla.org").ids(bug_ids).fields("summary").build()
    print request

    # # Search for bugs
    bb = BugBuilder("https://bugzilla.mozilla.org")
    bb.product("Firefox")
    bb.component("Developer Tools: 3D View")
    bb.status("NEW")
    request = bb.build()
    print request

    # # Actual examples

    bb = BugBuilder("https://bugzilla.mozilla.org")
    bb.product("Websites")
    bb.component("developer.mozilla.org")
    bb.open()
    bb.advanced("bug_group", "equals", "websites-security")
    request = bb.build()
    print request

    bb = BugBuilder("https://bugzilla.mozilla.org")
    bb.product("Websites").open()
    bb.advanced("bug_group", "equals", "websites-security").advanced("status_whiteboard", "substring", "[site:www.mozilla.org]")
    request = bb.build()
    print request

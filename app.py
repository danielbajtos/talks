from bottle import default_app, delete, get, post, put, request, response, run, get, view 

#################################

@get("/")
@view("index")
def _():
    return "x"

#################################

#################################

#################################

#################################

#################################

#################################








try:
    # Production
    import production
    application = default_app()
except:
    # Development
    run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")
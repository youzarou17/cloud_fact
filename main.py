def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using `make_response`.
    """
    request_json = request.get_json(silent=True)
    if request_json and 'name' in request_json:
        name = request_json['name']
    else:
        name = 'World'
    return f'Hello {name}!'
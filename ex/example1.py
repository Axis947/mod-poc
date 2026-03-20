HANDLER = None

def set_handler(handler):
    global HANDLER
    HANDLER = handler

def modify(apparatus):
    HANDLER.comment("Example 1 worked")
    return f"example1({apparatus})"

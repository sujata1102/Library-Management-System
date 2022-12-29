def Library_middleware(get_response):
    print("Code executed only once for any initialization")

    def library_function(request):
        print("Code executed before view function is called....")

        res=get_response(request)
        print("code executed after view function is called....")

        return res
    return library_function
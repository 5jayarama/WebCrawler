from html.parser import HTMLParser

# class to parse links and more
class Parser(HTMLParser):
    def __init__(self, parse_type):
        super().__init__()
        self.parse_type = parse_type # the thing that we are parsing for
        self.results = {} # store parsing results
        self.save_flag_data = False # if flag, save data (so we can print it)

    # handle start tags
    def handle_starttag(self, tag, attrs):
        if self.parse_type == "csrf" and tag == "input":
            attr_dict = dict(attrs)
            # extract csrf token if available
            if "name" in attr_dict and attr_dict["name"] == "csrfmiddlewaretoken":
                self.results["csrfmiddlewaretoken"] = attr_dict["value"]
            # extract next if available
            if "name" in attr_dict and attr_dict["name"] == "next":
                self.results["next"] = attr_dict["value"]

        # format: <h3 class='secret_flag' style="color:red">FLAG: 64-characters-of-random-alphanumerics</h3>
        if self.parse_type == "flag" and tag == "h3":
            attr_dict = dict(attrs)
            # save the flag
            if "class" in attr_dict and attr_dict["class"] == "secret_flag":
                self.save_flag_data = True

        # extract urls if available
        if self.parse_type == "url" and tag == "a":
            attr_dict = dict(attrs)
            if "href" not in attr_dict:
                return
            if "href" in self.results:
                # print("dictionary: ", attr_dict)
                self.results["href"].append(attr_dict["href"])
            else:
                self.results["href"] = [attr_dict["href"]]

    # save the next data as flag
    def handle_data(self, data):
        if self.save_flag_data:
            self.results["flag"] = data
            self.save_flag_data = False

    # gets the crsf token if available
    def get_csrf_token(self):
        if "csrfmiddlewaretoken" not in self.results:
            return "Error"
        else:
            return self.results["csrfmiddlewaretoken"]

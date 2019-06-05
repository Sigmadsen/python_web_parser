from html_parser import HtmlParser

# TODO: Uncomment it for checking speed by using API
# from api_parser import ApiParser

if __name__ == '__main__':
    html_parser_instance = HtmlParser()
    html_parser_instance.print_final_result(100)

    # --- 1.3550786972045898 seconds --- and no connection aborted
    # html_parser_instance.print_final_result(5)

    # TODO: Uncomment it for checking speed by using API
    # api_parser = ApiParser()
    # --- 6.7943620681762695 seconds --- and 1 connection aborted
    # api_parser.print_final_result(5)

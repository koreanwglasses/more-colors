from pyquery import PyQuery
import re
import json
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))

COLOR_DICT_URL = "https://people.csail.mit.edu/jaffer/Color/M.htm"
OUT_FILE = os.path.join(__dir__, "dict.json")

def main():
    pq = PyQuery(url=COLOR_DICT_URL)

    parsed_color_dict = {}
    for tr in pq('tr'):
        cells = pq(tr).children('td')

        if len(cells) < 2:
            # Not a color mapping row
            continue

        color_name = pq(cells[0]).text()

        # Remove anything in/past brackets
        color_name = re.match(r'[^\[\]]*', color_name)[0].strip()

        outer_html = pq(cells[1]).outer_html()
        match = re.search('background-color:(#[0-9A-Fa-f]{6});', outer_html)

        if not match:
          # Couldn't find hex
          continue

        hex_code = match[1]
        
        parsed_color_dict[color_name] = hex_code

    json.dump(parsed_color_dict, open(OUT_FILE, "w"))

if __name__ == "__main__":
    main()

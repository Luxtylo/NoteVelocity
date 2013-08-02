"""File for storing markup. Changing this file should change the whole project's markup."""

# HTML page header and footer
pageHeader = "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Page</title>\n\t\t<link rel='stylesheet' type='text/css' href='../style.css'>\n\t</head>\n\t<body>\n"
pageFooter = "\n\t</body>\n</html>"

# HTML markup
italicMarker = ["<i>","</i>"]
boldMarker = ["<b>","</b>"]
underlineMarker = ["<ins>","</ins>"]
strikethroughMarker = ["<del>","</del>"]
equationMarker = ["<b><i>","</i></b>"]
superscriptMarker = ["<sup>","</sup>"]
subscriptMarker = ["<sub>","</sub> "]
tabMarker = "&nbsp;&nbsp;&nbsp;&nbsp;"
bulletMarker = chr(149)
lineBreak = "\t\t<br/>\n"
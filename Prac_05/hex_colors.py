"""
CP1404 Practical
"""

color_codes = {"DarkOrange1": "#ff7f00", "DarkOrange2": "#ee7600", "DarkOrange3": "#cd6600", "DarkOrange4":	"#8b4500",
               "DarkOrchid": "#9932cc", "DarkOrchid1": "#bf3eff", "DarkOrchid2": "#b23aee",
               "DarkOrchid3": "#9a32cd", "DarkOrchid4":	"#68228b", "DarkSalmon": "#e9967a"}
color_name = input("Enter the name of a color: ")
while color_name !="":
    print("The code for \"{}\" is {}".format(color_name, color_codes.get(color_name)))
    color_name = input("Enter the name of a color: ")

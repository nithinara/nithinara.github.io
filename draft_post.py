import argparse
import datetime

def generate_draft_post(date):
	path = "_posts/{}-nyt-crossword-{}.md".format(date, date)

	parts = date.split("-")

	year = parts[0]
	month = parts[1]
	day = parts[2]

	if day.startswith("0"):
		day = day[1:]

	dummy_date = datetime.datetime.strptime(month, "%m")
	full_month_name = dummy_date.strftime("%B")

	title = "title: NYT Crossword | {} {}, {}".format(full_month_name, day, year)
	embed_url = "{% include embed/youtube.html id='X' %}"

	with open(path, "w") as file:
		file.write("---\n")
		file.write(title + "\n")
		file.write("date: " + date + "\n")
		file.write("categories: [NYT Crossword]\n")
		file.write("description: Solved The Crossword in X\n")
		file.write("tags: [crossword]\n")
		file.write("---\n\n")
		file.write(embed_url)
		file.write("\n")

parser = argparse.ArgumentParser(description="Generate a draft post")
parser.add_argument("-d","--date", help="the date of the post", required=True)
args = vars(parser.parse_args())

date = args["date"]

generate_draft_post(date)
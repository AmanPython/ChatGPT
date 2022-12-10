# Import the required modules
import glob
import os
from markdown import markdown
from ebooklib import epub

# Set the input and output directories
input_dir = "./markdown_files"
output_dir = "./epub_files"

# Create the ePub book object
book = epub.EpubBook()

# Set the book metadata
book.set_identifier("MultipleMarkdownFiles")
book.set_title("Multiple Markdown Files")
book.set_language("en")

# Create a new empty chapter
def create_new_chapter():
    chapter = epub.EpubHtml(title="", file_name="")
    chapter.content=u'<h1>Chapter</h1>'
    return chapter

# Loop through the Markdown files in the input directory
for file in glob.glob(input_dir + "/*.md"):
    # Read the Markdown file and convert it to HTML
    with open(file, "r") as f:
        markdown_text = f.read()
    html_text = markdown(markdown_text)

    # Create a new chapter and set its content to the HTML text
    chapter = create_new_chapter()
    chapter.content = html_text

    # Add the chapter to the book
    book.add_item(chapter)

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the ePub file
output_file = output_dir + "/MultipleMarkdownFiles.epub"
epub.write_epub(output_file, book, {})

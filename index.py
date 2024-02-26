import os
import glob

# Directory containing the "strips*" subdirectories
parent_dir = "."
# HTML file to generate
output_html = "index.html"

# Start of the HTML file
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Gallery</title>
    <style>
        body { display: flex; flex-wrap: wrap; }
        .image { margin: 10px; }
        img { max-width: 100px; max-height: 100px; }
    </style>
</head>
<body>
"""

# Find all "strips*" directories
for strips_dir in sorted(glob.glob(os.path.join(parent_dir, "strips*"))):
    # Find all files in the current "strips*" directory
    for filename in sorted(glob.glob(os.path.join(strips_dir, "*"))):
        # Add image to HTML content
        html_content += f'<div class="image"><img src="{filename}" alt=""></div>\n'

# End of the HTML file
html_content += """
</body>
</html>
"""

# Write the HTML content to the file
with open(output_html, "w") as file:
    file.write(html_content)

print(f"Gallery HTML has been generated: {output_html}")

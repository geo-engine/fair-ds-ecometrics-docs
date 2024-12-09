from bs4 import BeautifulSoup

# Load the HTML content
with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Create the new script tag
new_script = soup.new_tag('script', type='module')
new_script.string = '''
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
for (const element of document.getElementsByClassName("language-mermaid")) {
    element.classList.add("mermaid");
}
mermaid.initialize({ startOnLoad: true });
'''

# Append the script tag to the end of the body
soup.body.append(new_script)

# Save the modified HTML back to the file
with open('index.html', 'w') as file:
    file.write(str(soup))

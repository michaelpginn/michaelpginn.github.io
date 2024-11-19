"""Uses a citations.yaml file to create HTML for citations. You should copy the generated code into the appropriate part of publications.html."""
import yaml
from datetime import datetime
from collections import defaultdict


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def create_html_content(publications_by_year):
    html_content = ""

    for year in sorted(publications_by_year.keys(), reverse=True):
        html_content += f"\n<h2>{year}</h2>\n<section class=\"publications\">\n"
        for pub in publications_by_year[year]:
            authors = [f'<u>{author}</u>' if author == "Michael Ginn" else author for author in pub['authors']]
            html_content += f"""<div class="publication">
        <a href="{pub.get('link', '#')}">{pub['title']}</a>
        <div class="publication-authors">{', '.join(authors)}</div>
        <div class="publication-venue"><span class="publication-date">{pub['datestring']}</span>. {pub['publisher']}</div>
        """
            if "note" in pub:
                html_content += f"""<div class="special-note">🏆&nbsp;&nbsp;{pub['note']}</div>"""
            html_content += "</div>"
        html_content += "</section>\n"
    return html_content

def main():
    input_file = 'citations.yaml'
    output_file = 'publications.html'

    publications = read_yaml(input_file)

    # Group publications by year
    publications_by_year = defaultdict(list)
    for pub in publications:
        d = datetime.strptime(pub['date'], '%Y-%m-%d')
        pub['datestring'] = d.strftime("%B %Y")
        publications_by_year[d.year].append(pub)

    # Sort publications within each year
    for year in publications_by_year:
        publications_by_year[year].sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)

    html_content = create_html_content(publications_by_year)

    with open(output_file, 'w') as file:
        file.write(html_content)

    print(f"HTML file '{output_file}' has been created successfully.")

if __name__ == "__main__":
    main()

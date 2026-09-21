# === Stage 32: Add pagination helpers for long console output ===
# Project: MealPrepBox
def paginate(text, page_width=80):
    """Split long console text into fixed-width pages."""
    lines = text.split('\n')
    pages = []
    current = ''
    for line in lines:
        if len(current) + len(line) + 1 > page_width:
            pages.append(current.strip())
            current = line
        else:
            if current:
                current += '\n' + line
            else:
                current = line
    if current:
        pages.append(current.strip())
    return pages

def print_paginated(text, page_width=80):
    """Print text in pages with a separator between each."""
    pages = paginate(text, page_width)
    for i, page in enumerate(pages):
        print(f'--- Page {i+1} ---')
        print(page)
        print()

def print_paginated_to_file(text, filename='output.txt', page_width=80):
    """Write paginated text to a file."""
    pages = paginate(text, page_width)
    with open(filename, 'w') as f:
        for i, page in enumerate(pages):
            f.write(f'--- Page {i+1} ---\n')
            f.write(page + '\n')
            f.write('\n')

def merge_pages(*texts, page_width=80):
    """Merge multiple texts and paginate the combined result."""
    combined = '\n\n'.join(texts)
    return paginate(combined, page_width)

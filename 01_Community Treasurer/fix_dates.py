import re

def fix_dates(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    def replace_func(match):
        date_str = match.group(0)
        if '-' in date_str:
            parts = date_str.split('-')
            if len(parts) == 3:
                # parts[0] is YYYY, parts[1] is MM, parts[2] is DD
                return f"{parts[2]}/{parts[1]}/{parts[0]}"
        return date_str

    # Match YYYY-MM-DD
    new_content = re.sub(r'\d{4}-\d{2}-\d{2}', replace_func, content)
    
    with open(file_path, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    fix_dates('02_Reconcile/transactions-2026.md')

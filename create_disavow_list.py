import pandas as pd
import re
import os
from datetime import datetime

def create_disavow_list(excel_path, output_dir=None):
    """
    Creates a disavow list from an Excel file with backlinks,
    filtering out PBN links matching the wix.com/marketplace/wix-partner pattern.
    
    Args:
        excel_path: Path to the Excel file with backlinks
        output_dir: Directory to save the disavow file (defaults to same directory as script)
    """
    print(f"Reading backlinks from: {excel_path}")
    
    # Try to determine which column has the URLs
    try:
        # Read first few rows to inspect
        df_sample = pd.read_excel(excel_path, nrows=5)
        
        # Look for likely column names or types
        url_column = None
        for col in df_sample.columns:
            col_lower = str(col).lower()
            if 'url' in col_lower or 'link' in col_lower or 'source' in col_lower or 'target' in col_lower:
                url_column = col
                break
        
        # If we couldn't find by name, try to find by content
        if not url_column:
            for col in df_sample.columns:
                sample_values = df_sample[col].astype(str)
                if any(['http' in val.lower() for val in sample_values]):
                    url_column = col
                    break
        
        # If still no column found, use first column
        if not url_column:
            url_column = df_sample.columns[0]
            
        print(f"Using column: {url_column}")
        
        # Read the full Excel file
        df = pd.read_excel(excel_path)
        
        # Filter for PBN links matching wix.com/marketplace/wix-partner pattern
        pattern = r'wix\.com/marketplace/wix-partner'
        
        # Convert column to string to ensure regex works
        df[url_column] = df[url_column].astype(str)
        
        # Filter rows matching the pattern
        filtered_df = df[df[url_column].str.contains(pattern, regex=True, na=False)]
        
        # Get the list of domains to disavow
        disavow_links = filtered_df[url_column].tolist()
        
        # Create output file path
        if output_dir is None:
            output_dir = os.path.dirname(os.path.abspath(__file__))
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"bluecap_disavow_{timestamp}.txt")
        
        # Write to disavow file
        with open(output_file, 'w') as f:
            f.write("# Disavow file for BlueCap Advisors\n")
            f.write("# Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            f.write("# Filtered for PBN links matching wix.com/marketplace/wix-partner pattern\n\n")
            
            for link in disavow_links:
                try:
                    # Try to extract domain from URL
                    domain_match = re.search(r'https?://([^/]+)', link)
                    if domain_match:
                        domain = domain_match.group(1)
                        f.write(f"domain:{domain}\n")
                    else:
                        # If we can't extract domain, use the full URL
                        f.write(f"url:{link}\n")
                except:
                    # Fallback for any parsing issues
                    f.write(f"url:{link}\n")
        
        print(f"Found {len(disavow_links)} links matching the pattern.")
        print(f"Disavow file created at: {output_file}")
        return output_file, len(disavow_links)
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None, 0

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        excel_path = sys.argv[1]
    else:
        excel_path = r"C:\Users\gunja\OneDrive\Desktop\bluecapeconomicadvisors.com-backlinks-2025-04-18.xls"
    
    create_disavow_list(excel_path)

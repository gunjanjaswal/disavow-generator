# BlueCap Disavow Generator

A specialized Python tool that automatically generates Google disavow files by filtering Excel spreadsheets of backlinks for potentially harmful PBN (Private Blog Network) links.

## Purpose

This tool was created specifically for BlueCap Advisors to identify and disavow suspicious backlinks that match patterns associated with PBNs, particularly those with the Wix partner marketplace pattern.

## Features

- Automatically processes Excel files containing backlink data
- Intelligently identifies the URL column in various backlink export formats
- Filters links matching the `wix.com/marketplace/wix-partner` pattern (common in certain PBNs)
- Extracts domains from matched URLs
- Generates properly formatted disavow files ready for Google Search Console
- Includes timestamps and documentation in the disavow file
- Easy to use with a simple batch file interface

## Requirements

- Python 3.6 or higher
- pandas library (automatically installed by the batch file if missing)

## How to Use

1. Place your backlink Excel file in an accessible location
2. Edit the `run_disavow_generator.bat` file to point to your Excel file (or use the default path)
3. Double-click the `run_disavow_generator.bat` file
4. The tool will generate a disavow file in the same directory with a timestamp

## Output Format

The tool generates a properly formatted disavow file according to Google's specifications:

```
# Disavow file for BlueCap Advisors
# Generated on: 2025-07-03 18:26:32
# Filtered for PBN links matching wix.com/marketplace/wix-partner pattern

domain:example-pbn-site.com
domain:another-suspicious-domain.com
```

## How It Works

The tool:
1. Reads the Excel file containing backlinks
2. Automatically identifies which column contains URLs
3. Filters for links matching the Wix partner marketplace pattern
4. Extracts the domain from each matched URL
5. Writes a properly formatted disavow file with appropriate headers

## Customization

To modify the filtering pattern or other behaviors:

1. Open `create_disavow_list.py` in a text editor
2. Change the `pattern` variable to match different PBN patterns
3. Adjust other parameters as needed

## Author

Gunjan Jaswaal  
Website: [www.gunjanjaswal.me](https://www.gunjanjaswal.me)  
Email: [hello@gunjanjaswal.me](mailto:hello@gunjanjaswal.me)

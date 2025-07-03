# Google Disavow File Generator

A lightweight, browser-based tool that helps SEO professionals generate properly formatted disavow files for Google Search Console.

## Features

- Convert lists of URLs and domains into the exact format required by Google
- Validate input to ensure proper formatting
- Automatically detect and fix common formatting errors
- Add comments to document your disavow decisions
- Batch process multiple URLs or domains at once
- No server-side processing - everything happens in your browser
- Export properly formatted .txt files ready for upload to Google Search Console

## How to Use

1. Enter URLs or domains you want to disavow (one per line)
2. Select whether each entry is a URL or domain
3. Add optional comments to document your decisions
4. Generate the properly formatted disavow file
5. Download the .txt file
6. Upload to Google Search Console

## Input Format

The tool accepts the following formats:

### For URLs:
```
https://example.com/bad-page
http://spam-site.com/page
www.suspicious-site.com/page.html
```

### For Domains:
```
example.com
spam-site.com
www.suspicious-site.com
```

## Output Format

The tool generates a properly formatted disavow file according to Google's specifications:

```
# Disavow file generated on 2025-07-03
# The following URLs were flagged for suspicious backlinks
domain:example.com
domain:spam-site.com
url:https://legitimate-site.com/specific-bad-page.html
```

## Why Use a Disavow File?

Disavow files tell Google to ignore specific backlinks when assessing your site. This can be helpful if your site has received unnatural or spammy backlinks that might negatively impact your search rankings.

## When to Use

- After receiving a manual penalty from Google
- When you've identified spammy or low-quality backlinks pointing to your site
- After being the target of a negative SEO attack
- When cleaning up an old backlink profile with questionable links

## Important Notes

- Use the disavow tool with caution - only disavow links you're confident are harmful
- Google recommends trying to remove bad links before disavowing them
- Changes may take time to be processed by Google after uploading

## License

MIT License

## Author

Gunjan Jaswaal  
Website: [www.gunjanjaswal.me](https://www.gunjanjaswal.me)  
Email: [hello@gunjanjaswal.me](mailto:hello@gunjanjaswal.me)

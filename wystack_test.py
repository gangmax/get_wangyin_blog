import sys
import wystack

SAMPLE_URL = 'https://yinwang1.substack.com/p/321'

if __name__ == '__main__':
    given_url = sys.argv[1] if len(sys.argv) > 1 else SAMPLE_URL
    raw_content = wystack.parse_page_to_post(given_url)
    print(raw_content + '\n\n\n')
    result_content = wystack.optimize_content(raw_content, 'test', given_url)
    print(result_content)

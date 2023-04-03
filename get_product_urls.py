from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse

def get_product_urls(shop_name: str)-> list[str]:
    with sync_playwright() as p:
        cookies = [
            {"name": "language", "value": "en", "domain": "shopee.co.th", "path": "/"},
        ]
        base_url = "https://shopee.co.th"
        shop_url = f"{base_url}/{shop_name}#product_list"
        product_links = []

        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.add_cookies(cookies)
        # Navigate to the All Product page
        page = context.new_page()
        print(f"Crawling shop {shop_url}")
        page.goto(shop_url, wait_until='networkidle')
        while True:
            page_number = int(page.locator(".shopee-button-solid--primary").text_content())
            print(f"Extracting product URLs from page {page_number}")
            product_objects = page.query_selector_all('[data-sqe="link"]')
            for link in product_objects:
                relative_url = link.get_attribute("href")
                abusolute_url = f"{base_url}{relative_url}"
                product_links.append(urljoin(abusolute_url, urlparse(abusolute_url).path))
            # go to the next page
            if next_page_button := page.query_selector(".shopee-icon-button--right"):
                next_page_button.click()
                page.wait_for_load_state("networkidle")
                if int(page.locator(".shopee-button-solid--primary").text_content()) > page_number:
                    continue
            break
        context.close()
        browser.close()
    return product_links

if __name__ == "__main__":
    shop_name = "ethan1177"
    product_links = get_product_urls(shop_name)
    with open('product_urls.txt', 'w') as file:
        file.write('\n'.join(product_links) + '\n')
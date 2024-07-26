import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# 링크 스크래핑 할 웹 페이지의 URL
target_url = "your_target_url"

def scrape_links(url):
    try:
        # 웹 페이지 요청, 타임아웃 5초 설정
        response = requests.get(url, timeout=5)
        
        # 요청이 성공적이지 않은 경우 예외 발생
        response.raise_for_status()
        
        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # img 태그 내 src 속성의 링크 수집 # base_url + relative_path를 통해 절대 경로로 링크 저장
        img_links = [urljoin(target_url, img['src']) for img in soup.find_all('img', src=True)]
        
        # a 태그 내 href 속성의 링크 수집
        a_links = [urljoin(target_url, a['href']) for a in soup.find_all('a', href=True)]
        
        # set 사용하여 중복 링크 제거
        all_links = set(img_links + a_links)
        
        # 결과 출력
        print(f"[+] 결과 | 타겟: {target_url}") 
        for link in all_links:
            print(link)
    except requests.exceptions.Timeout:
        print(f"[-] Error: 연결에 문제가 없는지 확인하세요. | URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Error: 요청에 실패했습니다. | Error Message: {e}")

scrape_links(target_url)

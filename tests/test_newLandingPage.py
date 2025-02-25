import pytest
import asyncio
from pathlib import Path
import random
from playwright.async_api import async_playwright, expect
from utils.loggers import function_logging, module_logging

#####
### 구현 완료
### 전송(submit) 버튼은 주석처리로 비활성화 상태
#####




# type A
@function_logging
async def wrapsody_contactUs_KR_Main(settings, test_logger):
    
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                   
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Warpsody로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="생성형 AI 학습 콘텐츠 관리 | Wrapsody")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/wrapsody")

                # 영업담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot(
                    "- heading \"Wrapsody\" [level=2]\n"
                    "- heading \"Wrapsody 영업 담당자\" [level=2]\n"
                    "- heading \"만나러 가기\" [level=2]"
                )
                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-a?type=wrapsody")
            
               
                # 양식 작성하기
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hqtest5")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                #await page11.once("dialog", lambda dialog: dialog.dismiss())

                ###await page11.get_by_role("button", name="상담 신청하기").click()
            
                return True
   
# type ??
@function_logging
async def wrapsody_contactUs_EN_Main(settings, test_logger):
    
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
    
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # 'AI-Ready Data' 탭이 나타날 때까지 기다림
                ai_ready_data_tab = page.get_by_role("tab", name="AI-Ready Data")
                await expect(ai_ready_data_tab).to_be_visible()  

                # 'AI-Ready Data' 탭 클릭
                await ai_ready_data_tab.click()
                # await page.wait_for_url("https://en.fasoo.com/products/ai-ready-data/")  # 페이지가 해당 URL로 변경될 때까지 기다림

                # 'Wrapsody' 링크에 hover
                wrapsody_link = page.get_by_role("link", name="Wrapsody Enterprise Content")
                await wrapsody_link.hover()
                
                # 'Wrapsody' 링크 클릭
                await wrapsody_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/wrapsody/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Wrapsody is available in the").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=wrapsody")  # URL이 일치할 때까지 대기
                

                # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                ###await page12.get_by_role("button", name="Book Now").click()

                return True
   
# type C
@function_logging
async def wrapsodyECO_contactUs_KR_Main(settings, test_logger):
    
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                   
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)      
                # 상단 배너에서 제품 > Warpsody로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="Wrapsody eCo", exact=True)
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/wrapsody-eco")
                
                # 영업담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot(
                    "- heading \"Wrapsody\" [level=2]\n"
                    "- heading \"Wrapsody eCo 영업 담당자\" [level=2]\n"
                    "- heading \"만나러 가기\" [level=2]"
                )
                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                page11 = await page11_info.value
                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-c?type=wrapsody-eco")
                
                # 양식 작성하기
                await page11.get_by_label("성명").click()
                await page11.get_by_label("성명").fill("hqtest1")
                await page11.get_by_label("성명").press("Tab")
                await page11.get_by_label("회사").fill("hqtest2")
                await page11.get_by_label("회사").press("Tab")
                await page11.get_by_label("부서").fill("hqtest3")
                await page11.get_by_label("부서").press("Tab")
                await page11.get_by_label("직급").fill("hqtest4")
                await page11.get_by_label("직급").press("Tab")
                await page11.get_by_label("연락처").fill("01011111111")
                await page11.get_by_label("연락처").press("Tab")
                await page11.get_by_label("이메일").fill("hqtest@fasoo.com")
                await page11.get_by_label("이메일").press("Tab")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_placeholder("유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다").fill("hqtest")
                #await page11.once("dialog", lambda dialog: dialog.dismiss())
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                ###await page11.get_by_role("button", name="상담 신청하기").click()

                return True

 
# type ??
@function_logging
async def wrapsodyECO_contactUs_EN_Main(settings, test_logger):
    
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                   
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)    
                await page.wait_for_load_state("networkidle") 
                # 'Products' 링크에 hover
                await expect(page.get_by_role("banner").get_by_role("link", name="Products")).to_be_visible()
                await page.get_by_role("banner").get_by_role("link", name="Products").hover()
                # 'Secure Collaboration' 탭이 나타날 때까지 기다린 후 호버링
                await expect(page.get_by_role("tab", name="Secure Collaboration")).to_be_visible()
                await page.get_by_role("tab", name="Secure Collaboration").hover()
                await expect(page.get_by_role("link", name="Wrapsody eCo Secure")).to_be_visible()
                await page.get_by_role("link", name="Wrapsody eCo Secure").click()
                await page.wait_for_url("https://en.fasoo.com/products/wrapsody-eco/")
                await page.wait_for_load_state("networkidle") 
                await expect(page.get_by_role("heading", name="Why Wrapsody eCo?")).to_be_visible()
                await expect(page.get_by_role("heading", name="Meet with a Wrapsody eCo")).to_be_visible()
                async with page.expect_popup() as page1_info:
                    await page.get_by_role("heading", name="Meet with a Wrapsody eCo").click()
                page1 = await page1_info.value
                # 양식 작성하기
                await page1.get_by_placeholder("Name*").click()
                await page1.get_by_placeholder("Name*").fill("hqtest")
                await page1.get_by_placeholder("Name*").press("Tab")
                await page1.get_by_placeholder("Company*").fill("hqtest")
                await page1.get_by_placeholder("Company*").press("Tab")
                await page1.get_by_placeholder("Department*").fill("hqtest")
                await page1.get_by_placeholder("Department*").press("Tab")
                await page1.get_by_placeholder("Job Title*").fill("hqtest")
                await page1.get_by_placeholder("Job Title*").press("Tab")
                await page1.get_by_placeholder("Phone*").fill("01022222222")
                await page1.get_by_placeholder("Work Email*").click()
                await page1.get_by_placeholder("Work Email*").fill("hqtest@fasoo.com")
                await page1.get_by_placeholder("Work Email*").press("Tab")
                await page1.get_by_placeholder("Inquiry Details*  (For a").fill("hqtest")
                await page1.get_by_label("Search Engine (Google, Bing,").check()
                await page1.get_by_label("I agree to the collection and").check()
                ###await page1.get_by_role("button", name="Book Now").click()
                # await expect(page1.get_by_text("Your submission was")).to_be_visible()
                # test_logger.info("[메인] Wrapsody eCo 문의하기[EN] - 이상 없음")
                await browser.close()
                return True
   
# type A
@function_logging
async def wrapsodySE_contactUs_KR_Main(settings, test_logger):
    
        url = "https://www.fasoo.com/?lang=kr"
        browser_config = {
            "type": "chromium",
            "headless": True,
            "viewport": {"width": 1920, "height": 1080},
            "accept_downloads": True,
            "timeout": 20000
        }

        async with async_playwright() as p:
            # Browser setup
            browser = await p.chromium.launch(headless=browser_config["headless"])
            context = await browser.new_context(
                viewport=browser_config["viewport"],
                accept_downloads=browser_config["accept_downloads"]
            )
            context.set_default_timeout(browser_config["timeout"])
            page = await context.new_page()

            # Navigate to main page
            await page.goto(url)
            await page.wait_for_load_state("networkidle")

            # Click Wrapsody Drive link
            drive_link = page.get_by_role("link", name="문서 관리 x 보안 강화 | Wrapsody SE")
            await expect(drive_link).to_be_visible()
            await drive_link.click()

            # Handle popup for contact form
            async with page.expect_popup() as page1_info:
                await page.get_by_role("heading", name="Wrapsody SE 영업 담당자").click()
            contact_page = page1_info.value
            await contact_page.wait_for_load_state("networkidle")

            # Form field data
            form_data = {
                "성명*": "hqtest",
                "회사*": "hqtest",
                "부서*": "hqtest",
                "직급*": "hqtest",
                "연락처*": "01090283044",
                "이메일*": "hqtest@fasoo.com",
                "문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)": "hqtest"
            }

            # Fill form fields
            for placeholder, value in form_data.items():
                field = contact_page.get_by_placeholder(placeholder)
                await expect(field).to_be_visible()
                await field.click()
                await field.fill(value)

            # Check required checkboxes
            checkboxes = [
                "온/오프라인 행사",
                "개인정보 수집 및 이용에 대해서 동의합니다"
            ]
            for checkbox in checkboxes:
                await contact_page.get_by_label(checkbox).check()
            # Submit button is commented out for testing
            # submit_button = contact_page.get_by_role("button", name="상담 신청하기")
            # await expect(submit_button).to_be_visible()
            # await submit_button.click()
            # Close browser
            await browser.close()
            return True

# type A
@function_logging
async def wrapsodyDrive_contactUs_KR_Main(settings, test_logger):
    
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                   
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)    
                await page.wait_for_load_state("networkidle")

                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="차세대 문서중앙화 | Wrapsody Drive")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/wrapsody-drive")
                async with page.expect_popup() as page1_info:
                    await page.get_by_role("heading", name="Wrapsody Drive 영업 담당자").click()
                page1 = await page1_info.value
                await page1.get_by_placeholder("성명*").click()
                await page1.get_by_placeholder("성명*").fill("hqtest")
                await page1.get_by_placeholder("회사*").click()
                await page1.get_by_placeholder("회사*").fill("hqtest")
                await page1.get_by_placeholder("부서*").click()
                await page1.get_by_placeholder("부서*").fill("hqtest")
                await page1.get_by_placeholder("직급*").click()
                await page1.get_by_placeholder("직급*").fill("hqtest")
                await page1.get_by_placeholder("연락처*").click()
                await page1.get_by_placeholder("연락처*").fill("01090283044")
                await page1.get_by_placeholder("연락처*").press("Tab")
                await page1.get_by_placeholder("이메일*").fill("hqtest")
                await page1.get_by_placeholder("이메일*").click()
                await page1.get_by_placeholder("이메일*").fill("hqtest@fasoo.com")
                await page1.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").click()
                await page1.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hqtest")
                await page1.get_by_label("온/오프라인 행사").check()
                await page1.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                ### page1.get_by_role("button", name="상담 신청하기").click()
        
                
# type ??
@function_logging
async def wrapsodyDrive_contactUs_EN_Main(settings, test_logger):
    
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                   
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)    
                await page.wait_for_load_state("networkidle")

                # Get the navigation bar 
                nav_menu = page.get_by_role("navigation")
                products_link = nav_menu.get_by_role("link", name="Products")

                # Verify Products link is visible
                await expect(products_link).to_be_visible()
                await products_link.hover()

                # Go to wrapsody link
                wrapsody_link = page.get_by_role("link", name="Wrapsody Drive Virtual")
                await expect(wrapsody_link).to_be_visible()
                await wrapsody_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/wrapsody-drive/")
                
                async with page.expect_popup() as page1_info:
                    await page.get_by_role("heading", name="Meet with a Wrapsody Sales").click()
                page1 = await page1_info.value
                await page1.get_by_placeholder("Name*").click()
                await page1.get_by_placeholder("Name*").fill("hqtest")
                await page1.get_by_placeholder("Name*").press("Tab")
                await page1.get_by_placeholder("Company*").fill("hqtest")
                await page1.get_by_placeholder("Company*").press("Tab")
                await page1.get_by_placeholder("Department*").fill("hqtest")
                await page1.get_by_placeholder("Department*").press("Tab")
                await page1.get_by_placeholder("Job Title*").fill("hqtest")
                await page1.get_by_placeholder("Job Title*").press("Tab")
                await page1.get_by_placeholder("Phone*").fill("01022222222")
                await page1.get_by_placeholder("Work Email*").click()
                await page1.get_by_placeholder("Work Email*").fill("hqtest@fasoo.com")
                await page1.get_by_placeholder("Work Email*").press("Tab")
                await page1.get_by_placeholder("Inquiry Details*  (For a").fill("hqtest")
                await page1.get_by_label("Search Engine (Google, Bing,").check()
                await page1.get_by_label("I agree to the collection and").check()
                ### await page1.get_by_role("button", name="Book Now").click()
                # await expect(page1.get_by_text("Your submission was")).to_be_visible()
                return True

#type A
@function_logging
async def AIRPrivacy_contactUs_KR_Main(settings, test_logger):
    
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                   
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)    
                await page.wait_for_load_state("networkidle")

                # Get the navigation bar 
                nav_menu = page.get_by_role("navigation")
                products_link = nav_menu.get_by_role("link", name="제품")
                # Verify Products link is visible
                await expect(products_link).to_be_visible()
                await products_link.hover()
                
                await page.get_by_role("link", name="AI 기반 개인정보보호 및 검출 | AI-R").click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-ai-r-privacy")
                await page.wait_for_load_state("networkidle")

                # Go to contact us link
                async with page.expect_popup() as page1_info:
                    await page.get_by_role("heading", name="AI-R Privacy 영업 담당자").click()
                page1 = await page1_info.value
                await page1.get_by_placeholder("성명*").click()
                await page1.get_by_placeholder("성명*").fill("hqtest")
                await page1.get_by_placeholder("회사*").click()
                await page1.get_by_placeholder("회사*").fill("hqtest")
                await page1.get_by_placeholder("부서*").click()
                await page1.get_by_placeholder("부서*").fill("hqtest")
                await page1.get_by_placeholder("직급*").click()
                await page1.get_by_placeholder("직급*").fill("hqtest")
                await page1.get_by_placeholder("연락처*").click()
                await page1.get_by_placeholder("연락처*").fill("01090283044")
                await page1.get_by_placeholder("이메일*").click()
                await page1.get_by_placeholder("이메일*").fill("hqtest@fasoo.com")
                await page1.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").click()
                await page1.get_by_label("온/오프라인 행사").check()
                await page1.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                ### await page1.get_by_role("button", name="상담 신청하기").click()
                return True
            
# type B
@function_logging
async def fss_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Smart Screen으로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="화면 보안 | FSS")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-smart-screen")

                # FSS 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FSS\" [level=2]\n- heading \"FSS 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-b?type=fss")
                #(f"[메인] Fasoo FSS[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                #(f"[메인] Fasoo FSS[KR] - 이상 없음")
                return True
   
# ??
@function_logging
async def fss_contactUs_EN( settings, test_logger):
     
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # EDRM 탭이 나타날 때까지 기다림
                E_tab = page.get_by_role("tab", name="EDRM")
                await expect(E_tab).to_be_visible()  

                # EDRM 탭 클릭
                await E_tab.click()

                # FSS 링크에 hover
                FSS_link = page.get_by_role("link", name="FSS Screen Security")
                await FSS_link.hover()
                
                # FSS 링크 클릭
                await FSS_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/fasoo-smart-screen/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Empower your screen security").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=fss")  # URL이 일치할 때까지 대기
                

               # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                #await page12.get_by_role("button", name="Book Now").click()

                 #(f"[메인] FSS 문의하기[EN] - 이상 없음")
                return True


# type B
@function_logging
async def fsp_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Smart Print로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="인쇄 보안 | FSP")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-smart-print")

                # FSP 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FSP\" [level=2]\n- heading \"FSP 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-b?type=fsp")
                 #(f"[메인] Fasoo FSP[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FSP[KR] - 이상 없음")
                return True


# tyep B
@function_logging
async def fsp_contactUs_EN( settings, test_logger):
     
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # EDRM 탭이 나타날 때까지 기다림
                E_tab = page.get_by_role("tab", name="EDRM")
                await expect(E_tab).to_be_visible()  

                # EDRM 탭 클릭
                await E_tab.click()

                # FSP 링크에 hover
                FSP_link = page.get_by_role("link", name="FSP Print Security")
                await FSP_link.hover()
                
                # FSP 링크 클릭
                await FSP_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/fasoo-smart-print/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Empower your print security").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=fsp")  # URL이 일치할 때까지 대기
                 #(f"[메인] FSP 문의하기[EN] - 팝업 페이지 로딩 완료")

               # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                #await page12.get_by_role("button", name="Book Now").click()

                 #(f"[메인] FSP 문의하기[EN] - 이상 없음")
                return True


# type B
@function_logging
async def fed_m_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Intergreatred Log Manager로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="모바일 보안 | FED-M")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-enterprise-drm-for-mobile")

                # FED-M 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FED-M\" [level=2]\n- heading \"FED-M 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-b?type=fed-m")
                 #(f"[메인] Fasoo FED-M[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FED-M[KR] - 이상 없음")
                return True


# type ???
@function_logging
async def fed_m_contactUs_EN( settings, test_logger):


     
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # EDRM 탭이 나타날 때까지 기다림
                E_tab = page.get_by_role("tab", name="EDRM")
                await expect(E_tab).to_be_visible()  

                # EDRM 탭 클릭
                await E_tab.click()

                # FC-BR 링크에 hover
                FC_BR_link = page.get_by_role("link", name="FED-M Mobile Document Security")
                await FC_BR_link.hover()
                
                # FC-BR 링크 클릭
                await FC_BR_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/fasoo-enterprise-drm-for-mobile/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Empower your data security on").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=fed-m")  # URL이 일치할 때까지 대기
                 #(f"[메인] FED-M 문의하기[EN] - 팝업 페이지 로딩 완료")

               # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                #await page12.get_by_role("button", name="Book Now").click()

                 #(f"[메인] FED-M 문의하기[EN] - 이상 없음")
                return True


# type B
@function_logging
async def fsw_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Intergreatred Log Manager로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="웹 콘텐츠 보안 | FSW")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-secure-web")

                # FSW 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FSW\" [level=2]\n- heading \"FSW 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-b?type=fsw")
                 #(f"[메인] Fasoo FSW[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FSW[KR] - 이상 없음")
                return True



# type B
@function_logging
async def fcb_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Intergreatred Log Manager로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="클라우드 보안 | FCB")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-cloud-bridge")

                # FCB 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FCB\" [level=2]\n- heading \"FCB 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-b?type=fcb")
                 #(f"[메인] Fasoo FCB[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FCB[KR] - 이상 없음")
                return True


# type B
@function_logging
async def fc_br_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Intergreatred Log Manager로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="문서 백업 | FC-BR")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-content-backup-and-recovery")

                # FC-BR 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FC-BR\" [level=2]\n- heading \"FC-BR 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-b?type=fc-br")
                 #(f"[메인] Fasoo FR-BR[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FR-BR[KR] - 이상 없음")
                return True


# type ??
@function_logging
async def fc_br_contactUs_EN( settings, test_logger):
     
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # EBR 탭이 나타날 때까지 기다림
                E_tab = page.get_by_role("tab", name="EBR")
                await expect(E_tab).to_be_visible()  

                # EBR 탭 클릭
                await E_tab.click()

                # FC-BR 링크에 hover
                FC_BR_link = page.get_by_role("link", name="Fasoo Content Backup and")
                await FC_BR_link.hover()
                
                # FC-BR 링크 클릭
                await FC_BR_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/fasoo-content-backup-and-recovery/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Be ransomware-ready Contact Us").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=fc-br")  # URL이 일치할 때까지 대기
                 #(f"[메인] FC-BR 문의하기[EN] - 팝업 페이지 로딩 완료")

               # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                #await page12.get_by_role("button", name="Book Now").click()

                 #(f"[메인] FC-BR 문의하기[EN] - 이상 없음")
                return True


# type B
@function_logging
async def film_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Intergreatred Log Manager로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="문서 추적/통합 로그 관리 | FILM")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-integrated-log-manager")

                # FILM 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FILM\" [level=2]\n- heading \"FILM 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-b?type=film")
                 #(f"[메인] Fasoo FILM[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FILM[KR] - 이상 없음")
                return True


# type ??
@function_logging
async def film_contactUs_EN( settings, test_logger):
     
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # 'DSPM 탭이 나타날 때까지 기다림
                dspm_tab = page.get_by_role("tab", name="DSPM")
                await expect(dspm_tab).to_be_visible()  

                # 'DSPM' 탭 클릭
                await dspm_tab.click()

                # 'FILM' 링크에 hover
                FDR_link = page.get_by_role("link", name="Fasoo Integrated Log Manager")
                await FDR_link.hover()
                
                # 'FILM' 링크 클릭
                await FDR_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/fasoo-integrated-log-manager/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Track all files, no matter").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=film")  # URL이 일치할 때까지 대기
                 #(f"[메인] DSPM-FILM 문의하기[EN] - 팝업 페이지 로딩 완료")

               # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                #await page12.get_by_role("button", name="Book Now").click()

                 #(f"[메인] DSPM-FILM 문의하기[EN] - 이상 없음")
                return True


# type ??
@function_logging
async def frv_contactUs_EN( settings, test_logger):
     
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
         #(f"[메인] Wrapsody 문의하기[EN] - 이상 없음")
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # Analytics 탭이 나타날 때까지 기다림
                A_tab = page.get_by_role("tab", name="Analytics")
                await expect(A_tab).to_be_visible()  

                # Analytics 탭 클릭
                await A_tab.click()

                # FRV 링크에 hover
                FDR_link = page.get_by_role("link", name="Fasoo RiskView UEBA")
                await FDR_link.hover()
                
                # FRV 링크 클릭
                await FDR_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/fasoo-riskview/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Take a proactive approach").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=frv")  # URL이 일치할 때까지 대기
                 #(f"[메인] FRV 문의하기[EN] - 팝업 페이지 로딩 완료")

               # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                #await page12.get_by_role("button", name="Book Now").click()

                 #(f"[메인] FRV 문의하기[EN] - 이상 없음")
                return True


# type C
@function_logging
async def frv_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=True,    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Data Radar로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="사용자 행동 기반 위험 관리 | FRV")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-riskview")

                # FRV 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FRV\" [level=2]\n- heading \"FRV 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-c?type=frv")
                 #(f"[메인] Fasoo FRV[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성하기
                await page11.get_by_label("성명").click()
                await page11.get_by_label("성명").fill("hqtest1")
                await page11.get_by_label("성명").press("Tab")
                await page11.get_by_label("회사").fill("hqtest2")
                await page11.get_by_label("회사").press("Tab")
                await page11.get_by_label("부서").fill("hqtest3")
                await page11.get_by_label("부서").press("Tab")
                await page11.get_by_label("직급").fill("hqtest4")
                await page11.get_by_label("직급").press("Tab")
                await page11.get_by_label("연락처").fill("01011111111")
                await page11.get_by_label("연락처").press("Tab")
                await page11.get_by_label("이메일").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다").click()
                await page11.get_by_placeholder("유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FRV[KR] - 이상 없음")
                return True



# type A
@function_logging
async def fdr_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=True,    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Data Radar로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="Fasoo Data Radar")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-data-radar")

                # FDR 영업 담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"FDR\" [level=2]\n- heading \"FDR 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-a?type=fdr")
                 #(f"[메인] Fasoo FDR[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성하기
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo FDR[KR] - 이상 없음")
                return True


# type A 
@function_logging
async def dspm_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=True,    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Crypto로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="Fasoo DSPM").first
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-dspm")

                # DSPM 전문 컨설턴트 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"Fasoo DSPM\" [level=2]\n- heading \"DSPM 전문 컨설턴트\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-a?type=fasoo-dspm")
                 #(f"[메인] Fasoo DSPM[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성하기
                await page11.get_by_placeholder("성명*").click()
                await page11.get_by_placeholder("성명*").fill("hqtest1")
                await page11.get_by_placeholder("성명*").press("Tab")
                await page11.get_by_placeholder("회사*").fill("hqtest2")
                await page11.get_by_placeholder("회사*").press("Tab")
                await page11.get_by_placeholder("부서*").fill("hqtest3")
                await page11.get_by_placeholder("부서*").press("Tab")
                await page11.get_by_placeholder("직급*").fill("hqtest4")
                await page11.get_by_placeholder("직급*").press("Tab")
                await page11.get_by_placeholder("연락처*").fill("01011111111")
                await page11.get_by_placeholder("연락처*").press("Tab")
                await page11.get_by_placeholder("이메일*").fill("hqtest5@fasoo.com")
                await page11.get_by_placeholder("이메일*").press("Tab")
                await page11.get_by_placeholder("문의 내용* (유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다.)").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo DSPM[KR] - 이상 없음")
                return True


# type ??
@function_logging
async def dspm_fdr_contactUs_EN( settings, test_logger):
     
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 'Products' 링크에 hover
                link = page.get_by_role("banner").get_by_role("link", name="Products")
                await link.hover()  
                
                # 'DSPM 탭이 나타날 때까지 기다림
                dspm_tab = page.get_by_role("tab", name="DSPM")
                await expect(dspm_tab).to_be_visible()  

                # 'DSPM' 탭 클릭
                await dspm_tab.click()

                # 'FDR' 링크에 hover
                FDR_link = page.get_by_role("link", name="Fasoo Data Radar Discovery")
                await FDR_link.hover()
                
                # 'FDR' 링크 클릭
                await FDR_link.click()
                await page.wait_for_url("https://en.fasoo.com/products/fasoo-data-radar/")

                # contact us 버튼 클릭 후 팝업 대기
                async with page.expect_popup() as page12_info:  # 팝업을 기다리고 -> page12_info에 저장
                    await page.locator("section").filter(has_text="Data Security Posture").get_by_role("link").click()

                # 팝업 페이지를 page12로 받아옴
                page12 = await page12_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page12.wait_for_load_state("load")  # 팝업 페이지가 로드될 때까지 대기
                await page12.wait_for_url("https://en.fasoo.com/contact-us/product?type=fdr")  # URL이 일치할 때까지 대기
                 #(f"[메인] DSPM-FDR 문의하기[EN] - 팝업 페이지 로딩 완료")

               # 양식 작성하기
                await page12.get_by_placeholder("Name*").click()
                await page12.get_by_placeholder("Name*").fill("hqtest1")
                await page12.get_by_placeholder("Name*").press("Tab")
                await page12.get_by_placeholder("Company*").fill("hqtest2")
                await page12.get_by_placeholder("Company*").press("Tab")
                await page12.get_by_placeholder("Department*").fill("hqtest3")
                await page12.get_by_placeholder("Department*").press("Tab")
                await page12.get_by_placeholder("Job Title*").fill("hqtest4")
                await page12.get_by_placeholder("Job Title*").press("Tab")
                await page12.get_by_placeholder("Phone*").fill("01011111111")
                await page12.get_by_placeholder("Phone*").press("Tab")
                await page12.get_by_placeholder("Work Email*").fill("hqtest5@fasoo.com")
                await page12.get_by_placeholder("Work Email*").press("Tab")
                await page12.get_by_placeholder("Inquiry Details*  (For a").fill("hello")
                await page12.get_by_label("Search Engine (Google, Bing,").check()
                await page12.get_by_label("I agree to the collection and").check()

                # 상담 신청하기 버튼 클릭
                #await page12.get_by_role("button", name="Book Now").click()

                 #(f"[메인] DSPM-FDR 문의하기[EN] - 이상 없음")
                return True


# type C
@function_logging
async def crypto_contactUs_KR( settings, test_logger):
     
        url = "https://www.fasoo.com/?lang=kr"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    # 헤드리스 해제
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)

                # 상단 배너에서 제품 > Fasoo Crypto로 문의 페이지 접근
                link = page.get_by_label("제품").get_by_role("link", name="제품")
                await link.hover()
                support = page.get_by_role("link", name="Fasoo Crypto")
                await expect(support).to_be_visible()
                await support.click()
                await page.wait_for_url("https://www.fasoo.com/products/fasoo-crypto")

                # 영업담당자 만나러가기 찾아서 클릭
                # Playwright ARIA 스냅샷을 사용하여 요소를 확인한 후 클릭
                await expect(page.locator("body")).to_match_aria_snapshot("- heading \"Fasoo Crypto\" [level=2]\n- heading \"Fasoo Crypto 영업 담당자\" [level=2]\n- heading \"만나러 가기\" [level=2]")

                meeting_button = page.locator('text=만나러 가기')
                await expect(meeting_button).to_be_visible()  # 요소가 보일 때까지 대기
                async with page.expect_popup() as page11_info:  # 새 창 팝업 대기
                    await meeting_button.click()
                
                page11 = await page11_info.value

                # 팝업 페이지에서 필요한 작업을 진행
                await page11.wait_for_load_state("load")
                await page11.wait_for_url("https://www.fasoo.com/contact-us/solutions-c?type=crypto-module")
                 #(f"[메인] Fasoo Crypto[KR] - 팝업 페이지 로딩 완료")
               
                # 양식 작성하기
                await page11.get_by_label("성명").click()
                await page11.get_by_label("성명").fill("hqtest1")
                await page11.get_by_label("성명").press("Tab")
                await page11.get_by_label("회사").fill("hqtest2")
                await page11.get_by_label("회사").press("Tab")
                await page11.get_by_label("부서").fill("hqtest3")
                await page11.get_by_label("부서").press("Tab")
                await page11.get_by_label("직급").fill("hqtest4")
                await page11.get_by_label("직급").press("Tab")
                await page11.get_by_label("연락처").fill("01011111111")
                await page11.get_by_label("연락처").press("Tab")
                await page11.get_by_label("이메일").fill("hqtest5@fasoo.com")
                await page11.get_by_label("이메일").press("Tab")
                await page11.get_by_placeholder("유저 수, 미팅 일정 등을 구체적으로 남겨 주시면 더욱 신속하게 상담이 진행됩니다").fill("hello")
                await page11.get_by_label("온/오프라인 행사").check()
                await page11.get_by_label("개인정보 수집 및 이용에 대해서 동의합니다").check()
                
                #await page11.get_by_role("button", name="상담 신청하기").click()
                 #(f"[메인] Fasoo Crypto[KR] - 이상 없음")
                return True


            
    
"""@function_logging
async def AIRPrivacy_contactUs_EN_Main(settings, test_logger):
    
        url = "https://en.fasoo.com/"
        current_module = Path(__file__).name  # 현재 모듈 이름 가져오기
        browser_type = "chromium"
        width = 1920
        height = 1080
        accept_download = True
        async with async_playwright() as p:
            if browser_type == "chromium":
                browser = await p.chromium.launch(
                    headless=settings.get_module_options(current_module)['headless'],    
                )
                context = await browser.new_context(
                    viewport={'width': width, 'height': height},
                    accept_downloads=accept_download,
                )
                context.set_default_timeout(20000)
                page = await context.new_page()
                await page.goto(url)    
                await page.wait_for_load_state("networkidle")

                # Get the navigation bar 
                nav_menu = page.get_by_role("navigation")
                products_link = nav_menu.get_by_role("link", name="Products")

                # Verify Products link is visible
                await expect(products_link).to_be_visible()
                await products_link.hover()

                # Go to wrapsody link
                link = page.get_by_role("link", name="")
                await expect(link).to_be_visible()
                await link.click()
                await page.wait_for_url("")

                await page.get_by_placeholder("Name*").click()
                await page.get_by_placeholder("Name*").fill("hqtest")
                await page.get_by_placeholder("Name*").press("Tab")
                await page.get_by_placeholder("Company*").fill("hqtest")
                await page.get_by_placeholder("Company*").press("Tab")
                await page.get_by_placeholder("Department*").fill("hqtest")
                await page.get_by_placeholder("Department*").press("Tab")
                await page.get_by_placeholder("Job Title*").fill("hqtest")
                await page.get_by_placeholder("Job Title*").press("Tab")
                await page.get_by_placeholder("Phone*").fill("0000000000")
                await page.get_by_placeholder("Phone*").press("Tab")
                await page.get_by_placeholder("Work Email*").fill("hqtest@fasoo.com")
                await page.get_by_placeholder("Work Email*").press("Tab")
                await page.get_by_placeholder("Inquiry Details*  (For a").fill("hqtest")
                await page.get_by_text("Search Engine (Google, Bing,").click()
                await page.locator("span").filter(has_text="I'd like Fasoo to use my").click()
                await page.once("dialog", lambda dialog: dialog.dismiss())"""
                # await page.get_by_role("button", name="Book Now").click()

@module_logging
@pytest.mark.asyncio
async def test_newLandingPage(settings, test_logger):

    type_a_functions = [wrapsody_contactUs_KR_Main, wrapsodySE_contactUs_KR_Main, wrapsodyDrive_contactUs_KR_Main, AIRPrivacy_contactUs_KR_Main, fdr_contactUs_KR, dspm_contactUs_KR]
    type_b_functions = [fss_contactUs_KR, fsp_contactUs_KR, fsp_contactUs_EN, fed_m_contactUs_KR, fsw_contactUs_KR, fcb_contactUs_KR, fc_br_contactUs_KR, film_contactUs_KR]
    type_c_functions = [wrapsodyECO_contactUs_KR_Main, frv_contactUs_KR, crypto_contactUs_KR]

    # 각 type에서 무작위로 하나의 함수 선택
    selected_functions = [
        random.choice(type_a_functions),
        random.choice(type_b_functions),
        random.choice(type_c_functions)
        ]

    # 선택된 함수들 실행
    for func in selected_functions:
        await func(settings, test_logger)

"""
@module_logging
@pytest.mark.asyncio
async def test_newLandingPage(settings, test_logger):
    

    await wrapsody_contactUs_KR_Main(settings, test_logger)
    await wrapsody_contactUs_EN_Main(settings, test_logger)

    await wrapsodyECO_contactUs_KR_Main(settings, test_logger)
    await wrapsodyECO_contactUs_EN_Main(settings, test_logger)

    await wrapsodySE_contactUs_KR_Main(settings, test_logger)
        
    await wrapsodyDrive_contactUs_KR_Main(settings, test_logger)
    await wrapsodyDrive_contactUs_EN_Main(settings, test_logger)
        
    await AIRPrivacy_contactUs_KR_Main(settings, test_logger)

    await fss_contactUs_KR( settings, test_logger)
    await fss_contactUs_EN( settings, test_logger)

    await fsp_contactUs_KR( settings, test_logger)
    await fsp_contactUs_EN( settings, test_logger)

    await fed_m_contactUs_KR( settings, test_logger)
    await fed_m_contactUs_EN( settings, test_logger)

    await fsw_contactUs_KR( settings, test_logger)

    await fcb_contactUs_KR( settings, test_logger)
        
    await fc_br_contactUs_KR( settings, test_logger)
    await fc_br_contactUs_EN( settings, test_logger)
        
    await film_contactUs_KR( settings, test_logger)
    await film_contactUs_EN( settings, test_logger)

    await frv_contactUs_KR( settings, test_logger)
    await frv_contactUs_EN( settings, test_logger)

    await fdr_contactUs_KR( settings, test_logger)
    await dspm_contactUs_KR( settings, test_logger)
    await dspm_fdr_contactUs_EN( settings, test_logger)

    await crypto_contactUs_KR( settings, test_logger)
"""
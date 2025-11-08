import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options

class LinkedInScraper:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None
        self.profile_data = []
        
    def setup_driver(self):
        """Configure Chrome driver with appropriate options"""
        chrome_options = Options()
        
        # Rotate user agents to avoid detection
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        
        chrome_options.add_argument(f'user-agent={random.choice(user_agents)}')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
    def login_via_google(self):
        """Login to LinkedIn by searching through Google"""
        try:
            # Go to Google first
            self.driver.get('https://www.google.com')
            time.sleep(2)
            
            # Search for LinkedIn login
            search_box = self.driver.find_element(By.NAME, 'q')
            search_box.send_keys('linkedin login')
            search_box.submit()
            time.sleep(3)
            
            # Click on the first LinkedIn link
            links = self.driver.find_elements(By.CSS_SELECTOR, 'a[href*="linkedin.com"]')
            if links:
                links[0].click()
                time.sleep(3)
            
            # Now perform login
            return self.perform_login()
            
        except Exception as e:
            print(f"Error during Google navigation: {str(e)}")
            # Fallback to direct login
            return self.direct_login()
    
    def direct_login(self):
        """Direct login to LinkedIn"""
        try:
            self.driver.get('https://www.linkedin.com/login')
            time.sleep(2)
            
            return self.perform_login()
            
        except Exception as e:
            print(f"Error during direct login: {str(e)}")
            return False
    
    def perform_login(self):
        """Actually perform the login operation"""
        try:
            # Wait for login form
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'username'))
            )
            
            password_field = self.driver.find_element(By.ID, 'password')
            
            # Enter credentials
            email_field.clear()
            email_field.send_keys(self.email)
            time.sleep(1)
            
            password_field.clear()
            password_field.send_keys(self.password)
            time.sleep(1)
            
            # Click login button
            login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            login_button.click()
            
            # Wait for redirect to feed
            time.sleep(5)
            
            # Check if login was successful
            if 'feed' in self.driver.current_url or 'checkpoint' in self.driver.current_url:
                print("Login successful!")
                return True
            else:
                print("Login may have failed. Please check manually.")
                return False
                
        except Exception as e:
            print(f"Error during login: {str(e)}")
            return False
    
    def scrape_profile(self, profile_url):
        """Scrape data from a single LinkedIn profile"""
        try:
            self.driver.get(profile_url)
            time.sleep(random.uniform(3, 6))  # Random delay to avoid detection
            
            profile_info = {
                'url': profile_url,
                'name': '',
                'headline': '',
                'location': '',
                'about': '',
                'connections': '',
                'experience': '',
                'education': ''
            }
            
            # Extract name
            try:
                name_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.text-heading-xlarge'))
                )
                profile_info['name'] = name_element.text.strip()
            except:
                print(f"Could not extract name from {profile_url}")
            
            # Extract headline
            try:
                headline = self.driver.find_element(By.CSS_SELECTOR, 'div.text-body-medium')
                profile_info['headline'] = headline.text.strip()
            except:
                pass
            
            # Extract location
            try:
                location = self.driver.find_element(By.CSS_SELECTOR, 'span.text-body-small.inline')
                profile_info['location'] = location.text.strip()
            except:
                pass
            
            # Extract connection count
            try:
                connections = self.driver.find_element(By.CSS_SELECTOR, 'span.t-bold')
                profile_info['connections'] = connections.text.strip()
            except:
                pass
            
            # Scroll to load more content
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(2)
            
            # Extract about section
            try:
                about_section = self.driver.find_element(By.CSS_SELECTOR, 'div.display-flex.ph5.pv3')
                profile_info['about'] = about_section.text.strip()[:200]  # First 200 chars
            except:
                pass
            
            # Extract first experience
            try:
                experience = self.driver.find_element(By.CSS_SELECTOR, 'div.pvs-entity')
                profile_info['experience'] = experience.text.strip()[:200]
            except:
                pass
            
            # Extract education
            try:
                # Scroll to education section
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                education = self.driver.find_element(By.XPATH, "//section[contains(@id, 'education')]//div[@class='pvs-entity']")
                profile_info['education'] = education.text.strip()[:200]
            except:
                pass
            
            print(f"Successfully scraped: {profile_info['name']}")
            return profile_info
            
        except Exception as e:
            print(f"Error scraping {profile_url}: {str(e)}")
            return None
    
    def scrape_multiple_profiles(self, profile_urls):
        """Scrape multiple LinkedIn profiles"""
        for idx, url in enumerate(profile_urls, 1):
            print(f"\nScraping profile {idx}/{len(profile_urls)}: {url}")
            
            profile_data = self.scrape_profile(url)
            if profile_data:
                self.profile_data.append(profile_data)
            
            # Random delay between profiles
            if idx < len(profile_urls):
                delay = random.uniform(5, 10)
                print(f"Waiting {delay:.1f} seconds before next profile...")
                time.sleep(delay)
    
    def save_to_csv(self, filename='linkedin_profiles.csv'):
        """Save scraped data to CSV file"""
        if not self.profile_data:
            print("No data to save!")
            return
        
        keys = self.profile_data[0].keys()
        
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.profile_data)
        
        print(f"\nData saved to {filename}")
        print(f"Total profiles scraped: {len(self.profile_data)}")
    
    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()


def main():
    # LinkedIn credentials (you need to provide these)
    LINKEDIN_EMAIL = 'your-test-email@gmail.com'
    LINKEDIN_PASSWORD = 'your-test-password'
    
    # Sample LinkedIn profile URLs
    profile_urls = [
        'https://www.linkedin.com/in/satyanadella/',
        'https://www.linkedin.com/in/williamhgates/',
        'https://www.linkedin.com/in/jeffweiner08/',
        'https://www.linkedin.com/in/sundarpichai/',
        'https://www.linkedin.com/in/timcook/',
        'https://www.linkedin.com/in/marissarosemayer/',
        'https://www.linkedin.com/in/reidhoffman/',
        'https://www.linkedin.com/in/sherylsandberg/',
        'https://www.linkedin.com/in/ginni-rometty/',
        'https://www.linkedin.com/in/melinda-gates-0716/',
        'https://www.linkedin.com/in/brianacton/',
        'https://www.linkedin.com/in/jankum/',
        'https://www.linkedin.com/in/markzuckerberg/',
        'https://www.linkedin.com/in/larrypage/',
        'https://www.linkedin.com/in/sergeybrinn/',
        'https://www.linkedin.com/in/jackdorsey/',
        'https://www.linkedin.com/in/evanwilliams/',
        'https://www.linkedin.com/in/benioff/',
        'https://www.linkedin.com/in/arianaahuffington/',
        'https://www.linkedin.com/in/leomessi/'
    ]
    
    scraper = LinkedInScraper(LINKEDIN_EMAIL, LINKEDIN_PASSWORD)
    
    try:
        print("Setting up Chrome driver...")
        scraper.setup_driver()
        
        print("\nAttempting login via Google...")
        if scraper.login_via_google():
            print("\nStarting profile scraping...")
            scraper.scrape_multiple_profiles(profile_urls)
            scraper.save_to_csv('linkedin_profiles.csv')
        else:
            print("Login failed. Please check credentials and try again.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        print("\nClosing browser...")
        scraper.close()


if __name__ == "__main__":
    main()

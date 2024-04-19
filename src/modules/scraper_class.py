from selenium import webdriver
from selenium.webdriver.common.by import By
import re

class Scraper:
    def __init__(self):
        self.service = webdriver.ChromeService()
        self.driver = webdriver.Chrome(service=self.service)
        self.course_list = []

    def strip_name(self, course: str) -> str:

        pattern = r'\s+(LEC|TUT|TST|LAB)(,\s*(LEC|TUT|TST|LAB))*\s*\d*\.?\d*'
        cleaned_course_name = re.sub(pattern, '', course)

        final_name = cleaned_course_name.replace(" ", "")

        return final_name
    
    def get_courses_with_description(self, url: str) -> list[dict]:

        self.driver.get(url)

        courses = self.driver.find_elements(By.CSS_SELECTOR, 'div.divTable')

        for course in courses:
            course_name = course.find_element(By.CSS_SELECTOR, 'strong').text
            try:
                course_description = course.find_elements(By.CSS_SELECTOR, 'div.divTableCell.colspan-2')[1].text
            except IndexError:
                course_description = "No detailed description available."

            self.course_list.append({"course_name": self.strip_name(course_name), "course_description": course_description, "course_diff": 0})

            print("Course Name:", self.strip_name(course_name))
            print("Course Description:", course_description)
            print("---------------------------")
        
        self.driver.quit()

        return course_list

    def get_course_difficulties(self, url)

scraper = Scraper()
scraper.get_courses_with_description(url="https://ucalendar.uwaterloo.ca/2324/COURSE/course-MATH.html")

        
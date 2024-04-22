from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import xlsxwriter

class Scraper:
    def __init__(self, ):
        self.service = webdriver.ChromeService()
        self.driver = webdriver.Chrome(service=self.service)

        self.course_list = []

    def strip_name(self, course: str) -> str:
        """ 
        Removes session type labels from the course name
        
        Args:
            course: A string containing the course name and possibly additional 
                labels and numeric information.

        Returns:
            A string with session type labels and spaces removed from the original
            course name.

        """
        pattern = r'\s+(LEC|TUT|TST|LAB)(,\s*(LEC|TUT|TST|LAB))*\s*\d*\.?\d*'
        cleaned_course_name = re.sub(pattern, '', course)

        final_name = cleaned_course_name.replace(" ", "")

        return final_name
    
    def get_courses_with_description(self, url: str):
        """
        Function that takes in a url to the math courses section of the
        uwaterloo undergrad calendar and adds courses, along with their description
        to the self.course_list

        Args:
            url: string: the url of the uw ug calendar containing the courses

        Returns: 
            None
        """
        self.driver.get(url)

        courses = self.driver.find_elements(By.CSS_SELECTOR, 'div.divTable')

        for course in courses:
            course_name = course.find_element(By.CSS_SELECTOR, 'strong').text
            try:
                course_description = course.find_elements(By.CSS_SELECTOR, 'div.divTableCell.colspan-2')[1].text
            except IndexError:
                course_description = "No detailed description available."

            self.course_list.append({"course_name": self.strip_name(course_name), "course_description": course_description, "course_difficulty": 0})

            print("Course Name:", self.strip_name(course_name))
            print("Course Description:", course_description)
            print("---------------------------")
        
        self.driver.quit()

    def get_course_difficulties(self, url: str):
        ...

    
    def write_to_file(self, file_name: str):
        """Writes course data to an Excel file.This method takes course 
        information stored within the instance's `course_list` attribute 
        and writes it to an Excel file using `xlsxwriter`. 
    
    Args:
        file_name: A string representing the name of the file to which the Excel data will be written

    Returns:
        None

    """
        workbook = xlsxwriter.Workbook(f"{file_name}.xslx")
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})

        worksheet.write("A1", "course_name", bold)
        worksheet.write("B1", "course_description", bold)
        worksheet.write("C1", "course_difficulty", bold)

        row = 1
        col = 0

        for course in self.course_list:
            worksheet.write(row, col, course["course_name"])
            worksheet.write(row, col + 1, course["course_description"])
            worksheet.write(row, col + 2, course["course_difficulty"])
            row += 1
        
        workbook.close()


scraper = Scraper()
scraper.get_courses_with_description(url="https://ucalendar.uwaterloo.ca/2324/COURSE/course-MATH.html")

        
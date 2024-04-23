from modules import Scraper

def main():
    
    url_list = [
        "https://ucalendar.uwaterloo.ca/2223/COURSE/course-AMATH.html",
        "https://ucalendar.uwaterloo.ca/2223/COURSE/course-CO.html",
        "https://ucalendar.uwaterloo.ca/2324/COURSE/course-STAT.html",
        "https://ucalendar.uwaterloo.ca/2324/COURSE/course-ACTSC.html",
        "https://ucalendar.uwaterloo.ca/2324/COURSE/course-CS.html",
        "https://ucalendar.uwaterloo.ca/2324/COURSE/course-PHYS.html",
        "https://ucalendar.uwaterloo.ca/2223/COURSE/course-PMATH.html",
        "https://ucalendar.uwaterloo.ca/2324/COURSE/course-MATH.html",
        "https://ucalendar.uwaterloo.ca/2324/COURSE/course-MTHEL.html"

        # TODO: Add course decriptions manually for the following courses: BIOL 239, HLTH 101, ENGL 378, AFM 424 
        # TODO: go through the rest of the majors and find courses that don't fit

    ]

    scraper = Scraper()

    scraper.get_courses_with_description(url_list[8])
    
    scraper.write_to_file("mthel")

    # Not tested yet


if __name__ == "__main__":
    main()
"""Functions to parse a file containing student data."""

def unique_houses(filename):
    """TODO: Return a set of student houses.

    Iterate over the cohort_data.txt file to look for all of the included house names
    and create a set called "houses" that holds those names.

    For example:

    >>> sorted(unique_houses("cohort_data.txt"))
    ["Dumbledore's Army", 'Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    """

    houses = set()

    #open the file and set it to a variable
    data_file = open(filename)

    #loop over each line
    for line in data_file:
        #strip the whitespace
        line = line.rstrip()
        #tokenize the line data
        house_name = line.split("|")[2]
        # check to make sure the person has a house name listed
        if house_name:
            #add the housename to the set of houses
            houses.add(house_name)

    return houses


def sort_by_cohort(filename):
    """TODO: Return a list of all cohort lists, including ghosts but not instructors.

    Sort students by cohort, skipping instructors.

    Iterate over the data to create a list for each cohort. Puts ghosts into a
    separate list called "ghosts".

    For example:

    >>> sort_by_cohort("cohort_data.txt")
    [['Harry Potter', 'Mandy Brocklehurst', 'Ron Weasley', 'Oliver Wood', 'Colin Creevey', 'Cho Chang', 'Michael Corner', 'Draco Malfoy', 'Seamus Finnigan', 'Eddie Carmichael', 'Theodore Nott', 'Terence Higgs', 'Hermione Granger', 'Penelope Clearwater', 'Angelina Johnson', 'Dennis Creevey'], ['Neville Longbottom', 'Cedric Diggory', 'Pansy Parkinson', 'Anthony Goldstein', 'Padma Patil', 'Luna Lovegood', 'Eleanor Branstone', 'Lee Jordan', 'Marietta Edgecombe', 'Andrew Kirke', 'Ginny Weasley', 'Mary Macdonald', 'Blaise Zabini', 'Natalie McDonald', 'Adrian Pucey', 'Hannah Abbott', 'Graham Pritchard', 'Susan Bones', 'Roger Davies', 'Owen Cauldwell'], ['Laura Madley', 'Orla Quirke', 'Parvati Patil', 'Eloise Midgeon', 'Zacharias Smith', 'Cormac McLaggen', 'Lisa Turpin', 'Demelza Robins', 'Ernie Macmillan', 'Millicent Bullstrode', 'Percy Weasley', 'Jimmy Peakes', 'Justin Finch-Fletchley', 'Miles Bletchley', 'Malcolm Baddock'], ['Marcus Belby', 'Euan Abercrombie', 'Vincent Crabbe', 'Ritchie Coote', 'Katie Bell', 'Terry Boot', 'Lavender Brown', 'Gregory Goyle', 'Marcus Flint', 'Dean Thomas', 'Jack Sloper', 'Rose Zeller', 'Stewart Ackerley', 'Fred Weasley', 'George Weasley', 'Romilda Vane', 'Alicia Spinnet', 'Kevin Whitby'], ['Friendly Friar', 'Grey Lady', 'Nearly Headless Nick', 'Bloody Baron']]
    """

    # all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    #open the file and set it to a variable
    data_file = open(filename)

    #loop over each line
    for line in data_file:
        #strip the whitespace
        line = line.rstrip()
        #tokenize the line data and index into cohort
        personal_info = line.split("|")
        #if the person is an instructor, move on
        if personal_info[-1] == "I":
            continue
        #otherwise, add their name to their cohort list or ghost list
        else:
            full_name = personal_info[0] + " " + personal_info[1]
            if personal_info[-1] == "G":
                ghosts.append(full_name)
            elif personal_info[-1] == "Fall 2015":
                fall_15.append(full_name)
            elif personal_info[-1] == "Summer 2016":
                summer_16.append(full_name)
            elif personal_info[-1] == "Spring 2016":
                spring_16.append(full_name)
            elif personal_info[-1] == "Winter 2016":
                winter_16.append(full_name)
    #set the all_students list equal to the contents of all the cohort lists
    # all_students.append(fall_15)
    # all_students.append(winter_16)
    # all_students.append(spring_16)
    # all_students.append(summer_16)
    # all_students.append(ghosts)
    
    
    return [fall_15, winter_16, spring_16, summer_16, ghosts]


def hogwarts_by_house(filename):
    """TODO: Sort students into lists by house and return all lists in one list.


    Iterate over the data to create a list for each house, and sorts students
    into their appropriate houses by last name. Sorts ghosts into a list called
    "ghosts" and instructors into a list called "instructors".

    For example:
    >>> hogwarts_by_house("cohort_data.txt")
    [['Abercrombie', 'Bell', 'Brown', 'Coote', 'Finnigan', 'Granger', 'Johnson', 'Jordan', 'Kirke', 'Longbottom', 'Macdonald', 'McDonald', 'McLaggen', 'Patil', 'Peakes', 'Potter', 'Robins', 'Sloper', 'Thomas', 'Vane', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Wood'], ['Baddock', 'Bletchley', 'Bullstrode', 'Crabbe', 'Flint', 'Goyle', 'Higgs', 'Malfoy', 'Parkinson', 'Pritchard', 'Pucey', 'Zabini'], ['Bones', 'Branstone', 'Cauldwell', 'Diggory', 'Finch-Fletchley', 'Macmillan', 'Madley', 'Midgeon', 'Smith', 'Whitby', 'Zeller'], ['Ackerley', 'Belby', 'Boot', 'Brocklehurst', 'Carmichael', 'Clearwater', 'Corner', 'Davies', 'Goldstein', 'Lovegood', 'Patil', 'Quirke', 'Turpin'], ['Abbott', 'Chang', 'Creevey', 'Creevey', 'Edgecombe', 'Nott', 'Spinnet'], ['Baron', 'Friar', 'Lady', 'Nick'], ['Flitwick', 'McGonagall', 'Snape', 'Sprout']]

    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    data_file = open(filename)

    #loop over each line
    for line in data_file:
        #strip the whitespace
        line = line.rstrip()
        #tokenize the line data
        personal_info = line.split("|")
        
        if personal_info[2] == "Gryffindor":
            gryffindor.append(personal_info[1])
        elif personal_info[2] == "Hufflepuff":
            hufflepuff.append(personal_info[1])
        elif personal_info[2] == "Slytherin":
            slytherin.append(personal_info[1])
        elif personal_info[2] == "Dumbledore's Army":
            dumbledores_army.append(personal_info[1])
        elif personal_info[2] == "Ravenclaw":
            ravenclaw.append(personal_info[1])
        elif personal_info[-1] == "G":
            ghosts.append(personal_info[1])
        elif personal_info[-1] == "I":
            instructors.append(personal_info[1])

    all_students = [sorted(gryffindor), sorted(slytherin), sorted(hufflepuff), sorted(ravenclaw), sorted(dumbledores_army), sorted(ghosts), sorted(instructors)]

    return all_students


def all_students_tuple_list(filename):
    """TODO: Return a list of tuples of student data.

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:

    >>> all_students_data = all_students_tuple_list("cohort_data.txt")
    >>> print all_students_data
    [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Laura Madley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Orla Quirke', 'Ravenclaw', '', 'Spring 2016'), ('Marcus Belby', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Euan Abercrombie', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Neville Longbottom', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Vincent Crabbe', 'Slytherin', 'Snape', 'Summer 2016'), ('Parvati Patil', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Mandy Brocklehurst', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Ritchie Coote', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Eloise Midgeon', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Zacharias Smith', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Katie Bell', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Cedric Diggory', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Ron Weasley', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Cormac McLaggen', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Lisa Turpin', 'Ravenclaw', 'Flitwick', 'Spring 2016'), ('Oliver Wood', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Pansy Parkinson', 'Slytherin', 'Snape', 'Winter 2016'), ('Demelza Robins', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Terry Boot', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Lavender Brown', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Anthony Goldstein', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Ernie Macmillan', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Colin Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Padma Patil', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Cho Chang', "Dumbledore's Army", 'Flitwick', 'Fall 2015'), ('Gregory Goyle', 'Slytherin', 'Snape', 'Summer 2016'), ('Michael Corner', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Luna Lovegood', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Eleanor Branstone', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Draco Malfoy', 'Slytherin', 'Snape', 'Fall 2015'), ('Marcus Flint', 'Slytherin', 'Snape', 'Summer 2016'), ('Lee Jordan', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Marietta Edgecombe', "Dumbledore's Army", 'Flitwick', 'Winter 2016'), ('Andrew Kirke', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Ginny Weasley', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Mary Macdonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Blaise Zabini', 'Slytherin', 'Snape', 'Winter 2016'), ('Millicent Bullstrode', 'Slytherin', 'Snape', 'Spring 2016'), ('Seamus Finnigan', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Eddie Carmichael', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Dean Thomas', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Percy Weasley', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Jack Sloper', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Theodore Nott', "Dumbledore's Army", 'Snape', 'Fall 2015'), ('Terence Higgs', 'Slytherin', 'Snape', 'Fall 2015'), ('Jimmy Peakes', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Natalie McDonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Justin Finch-Fletchley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Rose Zeller', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Miles Bletchley', 'Slytherin', 'Snape', 'Spring 2016'), ('Stewart Ackerley', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Adrian Pucey', 'Slytherin', 'Snape', 'Winter 2016'), ('Fred Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Hannah Abbott', "Dumbledore's Army", 'Sprout', 'Winter 2016'), ('Graham Pritchard', 'Slytherin', 'Snape', 'Winter 2016'), ('George Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Hermione Granger', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Penelope Clearwater', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Malcolm Baddock', 'Slytherin', 'Snape', 'Spring 2016'), ('Angelina Johnson', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Susan Bones', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Dennis Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Roger Davies', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Romilda Vane', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Alicia Spinnet', "Dumbledore's Army", 'McGonagall', 'Summer 2016'), ('Kevin Whitby', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Owen Cauldwell', 'Hufflepuff', 'Sprout', 'Winter 2016')]
    """

    data_file = open(filename)

    student_list = []

    #loop over each line
    for line in data_file:
        #strip the whitespace
        line = line.rstrip()
        #tokenize the line data
        personal_info = line.split("|")

        if personal_info[-1] in ["G", "I"]:
            continue
        else:
            full_name = personal_info[0] + " " + personal_info[1]
            student_profile = (full_name, personal_info[2], personal_info[3], personal_info[4])
            student_list.append(student_profile)

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use list of tuples generated by all_students_tuple_list() to make a small
    function that, given a first and last name from the command line, return
    that student's cohort, or returns "Student not found." when appropriate.

    NOTE: This function isn't included in doctests. Test it by uncommenting the
    function call at the bottom of the file.

    For example:

    Who are you looking for? Harry Potter
    'Harry Potter was in the Fall 2015 cohort.'

    Who are you looking for? Tom Riddle
    'Student not found.'

    """

    student_name_list = [student_profile[0] for student_profile in student_list]
    student_name = raw_input("Who are you looking for? ")
    
    if student_name in student_name_list:
        print "{} was in the {} cohort.".format(student_name, student_profile[-1])
    else:
        print "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Return a set of student last names that have duplicates.

    Iterate over the data to find any last names that exist across all cohorts.
    Use set operations (set math) to create and return a set of these names.

    For example:
    >>> find_name_duplicates("cohort_data.txt")
    set(['Weasley'])

    """

    winter_16 = set()
    spring_16 = set()
    summer_16 = set()
    fall_15 = set()

    #open the file and set it to a variable
    data_file = open(filename)

    #loop over each line
    for line in data_file:
        #strip the whitespace
        line = line.rstrip()
        #tokenize the line data and index into cohort
        personal_info = line.split("|")
        #if the person is an instructor, move on
        if personal_info[-1] in ["G","I"]:
            continue
        #otherwise, add their name to their cohort list or ghost list
        else:
            if personal_info[-1] == "Fall 2015":
                fall_15.add(personal_info[1])
            elif personal_info[-1] == "Summer 2016":
                summer_16.add(personal_info[1])
            elif personal_info[-1] == "Spring 2016":
                spring_16.add(personal_info[1])
            elif personal_info[-1] == "Winter 2016":
                winter_16.add(personal_info[1])


    duplicate_names = fall_15 & summer_16 & spring_16 & winter_16

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Prompt user for a student. Display everyone in their house and cohort.

     Prompt the user for the name via the command line and when given a name,
     print a statement of everyone in their house in their cohort.

     Use the list of tuples generated by all_students_tuple_list() to make a
     small function that, when given a student's first and last name, prints
     students that are in both that student's cohort and that student's house.

     NOTE: This function isn't included in doctests. Test it by uncommenting the
     function call at the bottom of the file.

     For example:

     Choose a student: Hermione Granger
     Hermione Granger was in house Gryffindor in the Fall 2015 cohort.
     The following students are also in their house:
     Seamus Finnigan
     Angelina Johnson
     Harry Potter
     Ron Weasley
     Oliver Wood

     """

    student_name = raw_input("Choose a student: ")

    for student_profile in student_list:
        if student_profile[0] == student_name:
            selected_student_profile = student_profile

    
    print "{} was in house {} in the {} cohort.".format(selected_student_profile[0], selected_student_profile[1], selected_student_profile[3])
    print "The following students are also in their house:"
    for student_profile in student_list:
        if student_profile[1] == selected_student_profile[1] and student_profile[3] == selected_student_profile[3] and student_profile[0] != student_name:
            print student_profile[0] 


#############################################################################
# Here is some useful code to run these functions without doctests!

all_students_data = all_students_tuple_list("cohort_data.txt")
# find_cohort_by_student_name(all_students_data)
# find_house_members_by_student_name(all_students_data)


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#



if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")

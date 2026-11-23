from pyscript import display, document

def add_member(e):
    # clear any previous content in the output container
    document.getElementById('scm_output').innerHTML = ""
    
    # predefine at least four sets representing student grades
    grade_7 = {'Carlisle Miller', 'Shanny Tolentino', 'Cameron Bufford'}
    grade_8 = {'Georgina Banal', 'Carlos David'}
    grade_9 = {'Alexander Floro', 'Gavin Taguiga'}
    grade_10 = {'Neo Macaraig', 'Angelo Gloria'}

    # retrieve first name and last name inputs from text boxes and used .lower for the lower case letters of the code and used .strip
    first_name = document.getElementById('scm_first_name').value.lower().strip()
    last_name = document.getElementById('scm_last_name').value.lower().strip()
    
    # format and create a set containing the new member
    new_student = first_name + " " + last_name
    new_member_set = {new_student}

    # use set union operator (|) to combine all grade sets and the new member set into a master set
    all_members = grade_7 | grade_8 | grade_9 | grade_10 | new_member_set

    # calculate total number of members by using the code len()
    total_members = len(all_members)

    # format the member list into HTML line breaks using sorted()
    member_list_html = "<br>".join(sorted(all_members))

    # display total member count using display() function with an f-string
    display(f"Total Members: {total_members}", target="scm_output")

    # append full member list to the HTML output using innerHTML
    document.getElementById('scm_output').innerHTML += f"<hr><p><strong>Full List of Members:</strong><br>{member_list_html}</p>"

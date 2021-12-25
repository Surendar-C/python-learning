contacts = {
    "count" : 4,
    "students" : [        
            {"name" : "Surendar" , "email" : "surendar@example.com"},
            {"name" : "Pavithra" , "email" : "pavithra@example.com"},
            {"name" : "Shristii" , "email" : "shristii@example.com"},
            {"name" : "JLakshmi" , "email" : "jlakshmi@example.com"}        
    ]     
}

for student in contacts["students"]:
    print(student["email"])
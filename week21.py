import json
students = {'people': [{'name': 'Mohan', 'university': 'klh', 'from': 'Manikonda'}
                   ]}
students = {'people': [{'name': 'shiva', 'university': 'klh', 'from': 'vijayawada'}
                   ]}
students = {'people': [{'name': 'karthik', 'university': 'klh', 'from': 'lb nagar'}
                   ]}
students = {'people': [{'name': 'santosh', 'university': 'klh', 'from': 'kukatpally'}
                   ]}
def generateFile(students):
    with open('file.json', 'w') as outfile:
        outfile.write(json.dumps(students, indent=4, sort_keys=True))
generateFile(students)
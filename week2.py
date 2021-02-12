import json
students = {}
students['people'] = []
students['people'].append({
    'name': 'Mohan',
    'university': 'klh',
    'from': 'Manikonda'
})
students['people'].append({
    'name': 'Anitha',
    'university': 'klh',
    'from': 'kukatpally'
})
students['people'].append({
    'name': 'Geeta',
    'university': 'klu',
    'from': 'jntu'
})
students['people'].append({
    'name': 'Babu',
    'university': 'klu',
    'from': 'jbs'
})
students['people'].append({
    'name': 'ABC',
    'university': 'klh',
    'from': 'xyz'
})
with open('data.txt', 'w') as outfile:
    json.dump(students, outfile)



"""
Exercise: Selection Sort
Implement a Multi-Level Sort of a given list of dictionaries based on a given sorting order. If user wants to sort dictionary based on First Key 'A', Then Key 'B', they shall pass list of keys in the order of preference as a list ['A','B']. Your code should be able to sort list of dictionaries for any number of keys in sorting order list.

Using this multi-level sort, you should be able to sort any list of dictionaries based on sorting order preference

Example: A single dictionary entry contains two keys 'First Name' and 'Last Name'. the list should be sorted first based on 'First Name', then based on 'Last Name', w.r.t. common/same 'First Name' entries.

for this, one shall past sorting order of preference list [ 'First Name' , 'Last Name' ]

For this, Given the following sequence List:

[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
Your algorithm should generate sorted list:

[
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
    {'First Name': 'Armaan', 'Last Name': 'Dadra'}
    {'First Name': 'Armaan', 'Last Name': 'Kumar'}
    {'First Name': 'Ingrid', 'Last Name': 'Galore'}
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'}
    {'First Name': 'Jade', 'Last Name': 'Canary'}
    {'First Name': 'Jaya', 'Last Name': 'Seth'}
    {'First Name': 'Jaya', 'Last Name': 'Sharma'}
    {'First Name': 'Karan', 'Last Name': 'Kumar'}
    {'First Name': 'Kiran', 'Last Name': 'Kamla'}
    {'First Name': 'Raj', 'Last Name': 'Nayyar'}
    {'First Name': 'Raj', 'Last Name': 'Sharma'}
    {'First Name': 'Raj', 'Last Name': 'Thakur'}
    {'First Name': 'Suraj', 'Last Name': 'Sharma'}
]

"""
def selectionSort(data, search_by):
    for key in search_by[-1::-1]:
        for i in range(len(data)):
            min_idx = i
            for j in range(i+1, len(data)):
                if data[j][key] < data[min_idx][key]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
    return data

if __name__ == "__main__":
    data = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar', 'age': 22},
    {'First Name': 'Suraj', 'Last Name': 'Sharma', 'age': 49},
    {'First Name': 'Karan', 'Last Name': 'Kumar', 'age': 52},
    {'First Name': 'Jade', 'Last Name': 'Canary', 'age': 43},
    {'First Name': 'Raj', 'Last Name': 'Thakur', 'age': 36},
    {'First Name': 'Raj', 'Last Name': 'Sharma', 'age': 33},
    {'First Name': 'Kiran', 'Last Name': 'Kamla', 'age': 26},
    {'First Name': 'Armaan', 'Last Name': 'Kumar', 'age': 20},
    {'First Name': 'Jaya', 'Last Name': 'Sharma', 'age': 25},
    {'First Name': 'Ingrid', 'Last Name': 'Galore', 'age': 43},
    {'First Name': 'Jaya', 'Last Name': 'Seth', 'age': 42},
    {'First Name': 'Armaan', 'Last Name': 'Dadra', 'age': 28},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick', 'age': 32},
    {'First Name': 'Aahana', 'Last Name': 'Arora', 'age': 27}
]
    search_by = [ 'First Name' , 'Last Name' ]
    sorted_data = selectionSort(data, search_by)
    import pprint
    pprint.pprint(sorted_data)
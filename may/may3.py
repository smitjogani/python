'''
    pickle
    use rwquest modual the download the irix    
'''
try:
    import requests
    import pickle

    data = requests.get(
        "may\iris.data")
    # print(data)

    l1 = data.split("\n")
    # print(l1)

    l2 = [items.split(",") for item in l1 if len(item) != 0]
    print(l2)

    with open("myiris.pkl", 'wb') as f:
        pickle.dump(l2, f)

except Exception as e:
    print(e)

'''
To read this pickle file use this code
'''

# import pickle

# with open("myiris.pkl" , 'rb') as f:
#     print(pickle.load(f))
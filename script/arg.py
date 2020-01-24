import argparse
#instantiate the object as ap
ap=argparse.ArgumentParser()
#adding the argument (here only one),specifying both shorthand version(-n) and long hand version('name')

ap.add_argument("-n","--name",required=True,help="name of the user")
args=vars(ap.parse_args())
#here the vars package is used on object argparse to turn command line arguments into python dict
#here the key is  name and value is the name we type
print(args)
'''
this is a required argument which is noted by parameter 'required=True'
'''
print("hi there {},it's nice to meet you".format(args["name"]))
                                                     

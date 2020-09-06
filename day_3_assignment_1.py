altitude=int(input("enter altitude of plane"))
if(altitude<=1000):
    print("safe to land")
elif((altitude>1000)&(altitude<=4500)):
    print("comedown the altitude to 1000")
else:
    if(altitude>=5000):
        print("go around and try again")

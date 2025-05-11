Weight = (input ("Weight:"))
unit =  input ("(K)g or (L)bs:")
if unit.upper()=="K":
    converted = Weight / 2
    print ("Weight in Lbs:" + str (converted))
else:
    Converted = Weight * 2
    print("Weight in Kgs:" + str(Converted))    

print ("A Program to calculate the Area of a Triangle");

input("Press any button to continue...");

angleBase = input("Enter Angle Base\n");

angleHeight = input("Enter Angle Height\n");
isHeightANumber = angleHeight.isdigit();
isBaseANumber = angleBase.isdigit();

if  angleBase!="" and angleHeight!="":

     if isBaseANumber and isHeightANumber:
        
                areaOfATriangle = int(int(angleBase) * int(angleHeight) / int(2));

                print("Area of a triangle whose base = ", angleBase, " and height = ", angleHeight, " is = ", areaOfATriangle);
     else:
                 print("Angle Base and Height must be a number");
else:
                print("Height and Base can't be empty.");


# part - 2
# This script is in continuation with ther script_1
skin_data = data[data[ : , 3] == 1]
print("min of skin colors: " + str(skin_data[ : , 2].min()))
print("max of skin colors: " + str(skin_data[ : , 2].max()))

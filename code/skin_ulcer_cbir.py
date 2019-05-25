#start############################################################################
# Main Function responsible for capturing the following input parameters:
# color_in: CSV file path containing the image color vectors
# texture_in: CSV file path containing the image texture vectors
# f_sim: distance function
def main():
    color_in = str(input()).rstrip()
    texture_in = str(input()).rstrip()
    f_sim = str(input()).rstrip()

    arq1 = open(color_in, 'r')
    arq2 = open(texture_in, 'r')

    arq1.close()
    arq2.close()
#end##############################################################################

# Execution of Program
main()

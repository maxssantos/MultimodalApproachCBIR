import feature_extractor_bib as feb

#start############################################################################
# Main Function responsible for capturing input parameters following:
# dir_in: directory path containing the original images
# dir_out: directory path that will contain the rendered feature vectors of the 
# original images
# desc_color: color descriptor type, BIC by default
# desc_texture: texture descriptor type, LBP by default
def main():

    dir_in = str(input()).rstrip()
    dir_out = str(input()).rstrip()
    desc_color = str(input()).rstrip()
    desc_texture = str(input()).rstrip()
    total_images = int(input())

    feb.fe(dir_in, dir_out, desc_color, desc_texture, total_images)
#end##############################################################################

#Execution of program
main()
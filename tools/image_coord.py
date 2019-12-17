def div():
    from get_missing import run
    coords = run()
    im_nums = list()
    for i in coords:
        print((i[0] - 0)/292,(i[1] - 0)/292)
        im_nums.append((i[0]//292,i[1]//292))
    return(im_nums)    

def isLandscape(width, height):
    if width > height:
        return "LandScape"
    else:
        return "Portrait"
    
print(isLandscape(20, 12))
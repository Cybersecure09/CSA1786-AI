def generateColorMap():
    '''
    This function generates a 256 jet colormap of HTML-like
    hex string colors (e.g. FF88AA)
    '''
    Map = cm.jet(np.arange(256))
    stringColors = []
    for i in range(Map.shape[0]):
        rgb = (int(255*Map[i][0]), int(255*Map[i][1]), int(255*Map[i][2]))
        if (sys.version_info > (3, 0)):
            stringColors.append((struct.pack('BBB', *rgb).hex())) # python 3
        else:
            stringColors.append(
                struct.pack('BBB', *rgb).encode('hex'))  # python2

    return stringColors 

def BlendFormat(ImageSet : list, Dimensions : str):
    __options = []
    __attachments = []

    try:
        for __ImgObj in ImageSet:
            if __ImgObj:
                {"type":11,"name":"image1","value":0},{"type":11,"name":"image2","value":1}
                __options.append({"type":11,"name":"image{}".format(len(__options)+1),"value":len(__options)})

                __attachments.append({"id":str(len(__options)-1),"filename":__ImgObj.filename,"uploaded_filename":str(__ImgObj.url)})
        
        if Dimensions != "--ar 1:1":
            __options.insert(2,{"type":3,"name":"dimensions","value":Dimensions})

        return (True, [__options, __attachments])
    except Exception as e:
        print("Error in BlendFormat:{}".format(e))
        return (False, "Error in BlendFormat:{}".format(e))
def main():

    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import numpy as np
    import sys
    
    fileName = sys.argv[1]
    name = sys.argv[2]

    try:
        img = mpimg.imread(fileName)
    except:
        print('Failed loading file.')

    img_l = np.copy(img)
    img_l[:,:img.shape[1]//2] = np.fliplr(img[:,img.shape[1]//2:])

    img_r = np.copy(img)
    img_r[:,img.shape[1]//2:] = np.fliplr(img[:,:img.shape[1]//2])
    
    img_tot = np.reshape([img_l,img_r],(img_l.shape[0]+img_r.shape[0],img_l.shape[1],3))

    plt.figure(figsize=(4,4))
    plt.imshow(img_tot)
    plt.xlim([0, img_l.shape[1]*2])
    plt.ylim([img_l.shape[0]+img_r.shape[0]+100,0])
    plt.text(x=img_r.shape[0]//2,y=img_l.shape[0]+img_r.shape[0]+80,s='Who would you rather fight?')#name[:len(name)]+name[:len(name):-1])
    plt.text(x=img_r.shape[1]*1.25,y=img_l.shape[0]+img_r.shape[0]//2,s=name[:len(name)//2]+(name[::-1])[len(name)//2:])
    plt.text(x=img_r.shape[1]*1.25,y=img_r.shape[0]//2,s=(name[::-1])[:len(name)//2]+name[len(name)//2:])
    plt.axis('off')
    plt.savefig('mod_'+sys.argv[1].split('.')[0]+'.png',dpi=1200)
    #plt.show()

if __name__ == '__main__':
    main()

import glob

if __name__ == '__main__':
    for name in glob.glob('tmp/*'):
        print( name )

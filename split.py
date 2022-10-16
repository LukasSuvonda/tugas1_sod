import sys #
import os
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)                  


def splitFile(fromfile, dirfile, chunksize=chunksize):
    if not os.path.exists(dirfile):                  
        os.mkdir(dirfile)                           
    else:
        for fname in os.listdir(dirfile):            
            os.remove(os.path.join(dirfile, fname))
    partnum = 0
    input = open(fromfile, 'rb')                   
    while 1:                                       
        chunk = input.read(chunksize)              
        if not chunk:
            break
        partnum = partnum+1
        filename = os.path.join(dirfile, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()                           
    input.close()
    assert partnum <= 9999                         
    return partnum


if len(sys.argv) == 2 and sys.argv[1] == '-help':
    print 'Use: split.py [file-to-split target-dir [chunksize]]'
else:
    if len(sys.argv) < 3:
        interactive = 1
        fromfile = raw_input('File yang akan displit? ')       
        dirfile = raw_input('Direktori untuk memasukan part file? ')
    else:
        interactive = 0
        fromfile, dirfile = sys.argv[1:3]                 
        if len(sys.argv) == 4:
            chunksize = int(sys.argv[3])
    absfrom, absto = map(os.path.abspath, [fromfile, dirfile])
    print 'Splitting', absfrom, 'ke', absto, 'dari', chunksize

    try:
        parts = splitFile(fromfile, dirfile, chunksize)
    except:
        print 'Error saat memasukan split:'
        print sys.exc_type, sys.exc_value
    else:
        print 'Split selesai:', parts, 'parts berada di', absto
    if interactive:
        raw_input('Masukan kunci')  # pause if clicked

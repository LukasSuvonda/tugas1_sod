import os #
import sys
readsize = 1024


def joinFile(fromdir, tofile):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj = open(filepath, 'rb')
        while 1:
            filebytes = fileobj.read(readsize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()


if len(sys.argv) == 2 and sys.argv[1] == '-help':
    print 'Use: join.py [from-dir-name to-file-name]'
else:
    if len(sys.argv) != 3:
        interactive = 1
        fromdir = raw_input('Directory berisi part files? ')
        tofile = raw_input('Nama file dibuat ulang? ')
    else:
        interactive = 0
        fromdir, tofile = sys.argv[1:]
    absfrom, absto = map(os.path.abspath, [fromdir, tofile])
    print 'Joining', absfrom, 'ke', absto

    try:
        joinFile(fromdir, tofile)
    except:
        print 'Error saat menggabungkan file:'
        print sys.exc_type, sys.exc_value
    else:
        print 'Penggabungan selesai: lihat', absto
    if interactive:
        raw_input('Masukan kunci')

from shutil import move
from sys import stderr

from PIL import Image, ImageFile
from os import rename, stat
from os.path import getsize, isfile, join, dirname
from stat import S_IWRITE


def image_upload(file):
    """Renames the specified image to a backup path,
    and writes out the image again with optimal settings."""
    BASE_DIR = join(dirname(__file__), '../..')
    filename = BASE_DIR + file
    print filename
    try:
        # Skip read-only files
        if (not stat(filename)[0] & S_IWRITE):
            print 'Ignoring read-only file "' + filename + '".'
            return False

        print filename
        # Create a backup
        backupname = filename + '.' + 'backupextension'

        if isfile(backupname):
            print 'Ignoring file "' + filename + '" for which existing backup file is present.'
            return False

        rename(filename, backupname)
    except Exception as e:
        stderr.write('Skipping file "' + filename + '" for which backup cannot be made: ' + str(e) + '\n')
        return False

    ok = False

    try:
        # Open the image
        with open(backupname, 'rb') as file:
            img = Image.open(file)

            # Check that it's a supported format
            format = str(img.format)
            if format != 'PNG' and format != 'JPEG' and format != 'MPO':
                print 'Ignoring file "' + filename + '" with unsupported format ' + format
                return False

            # This line avoids problems that can arise saving larger JPEG files with PIL
            ImageFile.MAXBLOCK = img.size[0] * img.size[1]

            # print img.size[0]
            # print img.size[1]

            # The 'quality' option is ignored for PNG files
            img = img.resize((700, ((img.size[1] * 700) / img.size[0])), Image.ANTIALIAS)
            img.save(filename, quality=90, optimize=True)

        # Check that we've actually made it smaller
        origsize = getsize(backupname)
        newsize = getsize(filename)
        # move(backupname, )

        if newsize >= origsize:
            print 'Cannot further compress "' + filename + '".'
            return False

        # Successful compression
        ok = True
    except Exception as e:
        stderr.write('Failure whilst processing "' + filename + '": ' + str(e) + '\n')
    finally:
        if not ok:
            try:
                move(backupname, filename)
            except Exception as e:
                stderr.write('ERROR: could not restore backup file for "' + filename + '": ' + str(e) + '\n')

    return ok

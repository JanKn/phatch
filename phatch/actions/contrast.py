# Phatch - Photo Batch Processor
# Copyright (C) 2007-2008 www.stani.be
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/
#
# Phatch recommends SPE (http://pythonide.stani.be) for editing python files.

# Embedded icon is taken from www.openclipart.org (public domain)

# Follows PEP8

from core import models
from lib.reverse_translation import _t

#---PIL


def init():
    global Image, ImageColor, imtools
    import Image
    import ImageColor
    from lib import imtools


def contrast(image, amount=50):
    """Adjust brightness from black to white
    - amount: -1(black) 0 (unchanged) 1(white)
    - repeat: how many times it should be repeated"""
    if amount == 0:
        return image
    elif amount < 0:
        #low contrast
        mean = reduce(lambda a, b:
            a + b, image.convert("L").histogram()) / 256.0
        im = imtools.blend(
                image,
                Image.new("L", image.size, mean).convert(image.mode),
                -amount / 100.0)
    else:
        #high contrast
        im = imtools.blend(
                image,
                image.point(lambda x: x > 128 and 255),
                amount / 100.0)
    #fix image transparency mask
    if image.mode == 'RGBA':
        im.putalpha(imtools.get_alpha(image))
    return im

#---Phatch


class Action(models.Action):
    label = _t('Contrast')
    author = 'Stani'
    email = 'spe.stani.be@gmail.com'
    init = staticmethod(init)
    pil = staticmethod(contrast)
    version = '0.1'
    tags = [_t('color')]
    __doc__ = _t('Adjust from grey to black & white')

    def interface(self, fields):
        fields[_t('Amount')] = self.SliderField(50, -100, 100)

    icon = \
'x\xda\x01\x1d\t\xe2\xf6\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x000\x00\
\x00\x000\x08\x06\x00\x00\x00W\x02\xf9\x87\x00\x00\x00\x04sBIT\x08\x08\x08\
\x08|\x08d\x88\x00\x00\x08\xd4IDATh\x81\xed\x9a[l\x14\xd7\x19\xc7\xff\xe7\
\xcc\xac\xf76k\xbc\xb0\xc4Y\xab\x96\xc1\x05*\x0b; \xa0\x02\xa9E\xa8M\x8b\x14\
TA\x8b\x04R\xd26\x08E\xaa\xdf\xaaF}\x01\x021\xb6U$*\xb5Om\x11\xb2\xa8T\xd2\
\x87H\xe6\xa5\xb1\xfa\x10\x11\xa4\x08\x14\x13\x08\x08\x12\xa4\x06\x97\x9b\
\x83\xcc\xac\x17_b\xe3\xbd\xcc\xed\x9c\xd3\x87\x9d3\x9e]\xef\x15H\xd3H=\xd2\
\xa7\x19\xef\x9c\x9d\xf9\xff\xce\xf7}\xe7|s\xd6D\x08\x81or\xa3_\xb7\x80gm\
\xff\x07\xf8\xba\x9b\xfa\x15\xdc\x93\xd4\xb8\xfe\\\x93\xeey\x00\xf8\x05\x93\
\xa1\xa1!\xe5\xcc\x993\xad\xd9l\xf6E\xc7qZ;;;\xedm\xdb\xb6\x99\x9c\xf3\xeb}}\
}9\xb7\xbf\x84xf\x18\xf2\x0c\xb3\x90\x14N\xb6l\xd9\xb21\x97\xcb\xfd\x94s\xbe\
;\x1a\x8dv\'\x93I%\x99L"\x91H \x12\x89\xe0g{\xf6 \x93\xc9@O\xa5\xec\xd9\xd9\
\xd9\xbbz*\xf5\xd7\x8e\x8e\x8e?\x1d8p\xc0r!\x9e^\xc4S\x00\x10\x00\x18\x1e\
\x1e\xa6\x03\x03\x03\xaf\xda\xb6\xdd\xb7i\xd3\xa65;v\xec@[[\x1b\x9a\x9b\x9bA\
\xc8\xa2S4M\xc3\xb7;;\x01\x00\x8e\xe3\xc0\xb2,\xcc\xcf\xcda||\x9c\xdf\xbb\
\x7f\xff\xe2B&\xf3\xda\xa1C\x87\xd2O\x0b\xd2(\x00\x01@zzz~h\xdb\xf6\xc9\xb5k\
\xd7n\xda\xb3g\x0fV\xadZ\x05B\x88g\x00\xbc\xa3\xa6iX\xb3f\r\xe0>G\x00\x80\
\x100M\x133\xd3\xd3H\xa5R\xec\xea\xb5kgm\xdb\xfeU__\x1fk\x14\xa2\x11\x002<<L\
\xfb\xfa\xfa\xfa\x97-[\xf6\xd6\xde\xbd{\xd1\xdd\xdd\rB\x08(\xa5E\x00\xa5\x1e\
X\xb7vmA\xbc\xefY\x12$\x9f\xcfc\xea\xf1c\x8c\x8d\x8dM\xeb\xe3\xe3\xdf}\xf3\
\xf0\xe1/\x1a\x81\xa8\x17\x80\xec\xda\xb5+6>>\xfeN(\x14\xda\xdd\xdb\xdb\x8bd\
2\tJ\xa9g\xa5\xc2\xe5y,\x16\xc3w\xd6\xad["\\\x9e\x0b!\xe0\xd86R\xba\x8e\x89\
\x89\t\xf3\xf2\xe8\xe8+\'N\x9e\xfc\xb0^\x88z\xd6\x01\xd2\xdb\xdb\x1b~\xf0\
\xe0\xc1\xfb\xaa\xaa\xee\xde\xbf\x7f?V\xae\\\t!\x04\x84\x10\xe0\x9c\x831\x06\
\xc6\x18\x1c\xc7\x81\xe38E\xe7\x8e\xe3x}=s\x85\xc35EU\xb1\xf2\x85\x17\xd0\
\xd6\xd6\x16\xfc\xc1\xcb/\x7fp\xe2\xc4\x89\x1f\xa1\xf6t\\\x17\x00\x01@.]\xba\
tJQ\x94m;w\xee\xc4\xea\xd5\xab\x8bDK\xb1\xb6m{fY\x96g\xa5\x00R\xb4\x1f\x06B\
\xa0\xa9\xa9\t+\x12\t\xc4[Z\xe8K\xdd\xdd#\x83\x83\x83\xdf\xaa\x07\xa2&@WW\
\xd7o\x08!\xafwtt`\xe3\xc6\x8d`\x8cy\x00\xa5\xc2\xcb\x99\xe38\xe0\x9c/1?\x90\
\x8c\x95p8\x8cH$\x82\xd6\xd6\xd6`G{\xfb\'\xfd\xfd\xfdJ-\x88j\x0b\x19\xd9\xba\
uk\x07\x80\x13\xaa\xaa\xa2\xa7\xa7\x07\x8c1\x00\x85\xe9\x90R\x8az\xf2Gz\xa0Z\
\x93^\x10B \x12\x8d"\x9f\xcf\xa3\xab\xab\xabuzff\x08\xc0\x1b\xa8\x92\x0f\xd5\
<@\x16\x16\x16\x06\x15E\t\x06\x02\x01\xb4\xb7\xb7\x17\x85\x8deY5G_z`I\x0e\
\x94\x98?\xa4\x9a\x9a\x9a\xbc\t\xa1{\xfd\xfa_\x0e\x0c\x0c\xb4\xa0\x8a\x17*y\
\x80l\xd8\xb0a\x03\x80W\x03\x81\x004M\x83\xa2(\x9e\xeb\xfd\xb3M\xad\xe6\xf7@\
\xbdS\xb6\x1a\x08\xc0\xb6,\xc4\xe3qE\x8bD\xfe\x06`w\xc3\x00\xa6i\xfeZUU\xaa\
\xaa*4M\xf3\xc2\xa7\x11\xf1\x12\x80s^w\x7f!\x04\x14J\xe1P\n"\x04zzz^A!RX\xb9\
\xfe\xe5B\x88\xf4\xf7\xf7SB\xc8OTUE \x10\x80i\x9au%\xec\xd3\x86P9\x93a\xd4\
\xd2\xd2\xa2\xfcnp\xf0\x17\xa8\x10Fe=p\xee\xdc\xb9\xef\x11B\x12\x8a\xa2@Q\
\x14\x10B\x90\xcb\xe5\x10\n\x85\xea\x1eI9\x9ae\x93\xb8J(q\x00\xdc\x07@\x08\
\xc1\xb2\x96\x96\x83\x00\xce\xd6\x0b@\x1c\xc7\xd9\xa5(\n(\xa5\x1e\x80\xae\
\xebhoooH<\xe0\xe6\x80/\x84je\x81mY\x85\xc5\x07\x00\xdcpmK&7c\xd1\x03E\xb7(\
\xeb\x01BH\'!\xc4\x13O\x08\xc1\xe4\xe4$Z[[\xeb\xca\x01\xff\x88;\x8e\x03\xde@\
\xc1hY\x96\x14\xe1A\xc4\xe3\xf1H\xa5\xfe\xa59 \xd5%Kk\x1c\xc30p\xf7\xee\xdd\
\xba\xe3\xbej)\xe17\xce=3\x0c\xa30YH\xf1\xae\xa0h4JGFF\xa2\xf5\x00\x00\x008\
\xe7I\x7fY,mvv\x16\x8f\x1e=j<\x89}"\x97\x98\x0bb\xd96l9\xfa\xdep.j\xb8u\xeb\
\xd6\xfarZ+\x85P\xd4w^t-\x9dNCUU\xc4b\xb1r_]\xd2\xaa\xad\xc4\xf2S\xce\x18,\
\xd3\\\xaa\xc3wn\xdb\xf6\x8ar\xf7\xa8\xb4\x0e\xa4\x85\x10\xad\x00\x8a\x16!\t\
\xa3\xeb:\x9a\x9b\x9b\xb1|\xf9r(\x8aRu\x81\xaa\x9a\x03\xee,\xe58N\xf9\xcb\
\xbesEQn\xd7\x03 \x00\x10BHJ\x08\xf1R\xd1r_\xf4\\\x81\xf9\xf9y,,, \x16\x8b-y\
\x8d\x94}$@\xb9iT\x96$U\xbd\xe3\xbb\xc7\xd1\xa3G\xc7\xeb\x01\x90\x0f\xd7e\
\xad\xef\xaf\x1cKEr\xce1??\x8fL&\x83H$\x02EQ\xa0\xaa*Tu\xf1\xb6^\x0e\xf8\x06\
C\xde\xb3b\x93e\xb7\x0b\xf2\xe4\xc9\x13\x07\x15f\xe0r\x00\x02\xc0\'B\x88\x83\
\xb2t.\xe7\x05\x7fc\x8caaa\xa1\xe83\xb9\x08j\x9a\xb685\xd6\xd9\xbc=\x17\x17$\
\x9dN\xa7J.y\xad\xec,\x14\x8f\xc7\xdfc\x8c\t\x7f\xf5Y\x0b\xa2\xb4\xc9\x8a\
\xb5\x91:\xc8S\xe8{\x96\x10\x02\xe9\xa9\xa9\x7f\x96\x13_\t@\x8c\x8e\x8e\xa6\
\x00\\\xf1\xbfqU\x8b\xd7\xe7\xdaJ\xd6\t\xce9\x1c\xc7\xf9C\xa5\xee\x95\xde\
\x07\x04!\xe4]\xc6\x18l\xdb\xf6\xde\xc2j\xc6\xee36\xf9\xae\xec\xb7;w\xee<>|\
\xf8\xf0}4\xe0\x01\x00\xc0\xf6\xed\xdb\x878\xe7\x0f\xfdU\xa8\x04\xf9o\x89\
\xe7\x9c\xe3\xfe\xbd{oV\x12\x0fT\xf1\xc0\xe9\xd3\xa7\rJ\xe9\xdb~\x00\x19J_\t\
D\xe9\xcb\xbe\x10\xb8\xfd\xf9\xe7\x0f\xdf\xee\xef\x7f\xb7\xda\xd7\xaa\xbdR\
\x8a\xe3\xc7\x8f\xff\x9ds~\xcd\xb2,\x98\xa6\xe9\xed2<O\x08\xff\xc8\xcbM2\xce\
9\xb2\xd9\xac\xf8bb\xe2u\xd9\xe5\xa9\x00\xf6\xed\xdb\xc7\x9b\x9b\x9b\xf73\
\xc6\xa6%\x84i\x9aE\xdex\x96\x9c\xf0/V\xe1p\x18\xf1\xe5\xcb\xa1\xc5b\xe0\x9c\
\xe3\xa3\xcb\x97O\x1e;v\xecb5\xf1\xb5\x00\x00@\\\xb9re\xbc\xa9\xa9i\x9fm\xdb\
\xb6\x04(\xe7\x8dF@\xe4\x90\n!@(ET\xd3\xa0\xc5b\x08\x85B\x98\xfb\xf2K\xdc\
\xbcq\xe3\xc3#G\x8e\xbcU\xcf\xbd\xea\xd9\x99\x137o\xde\xbc\xa8\xaa\xea\x1b\
\x96eY\x86a \x9f\xcf\xc30\x0c\x0fD&x\xe9\xc2\xe7_;\xfc\xa2e\x19MP\xd8z\xd44\
\r\x8a\xaa"\xa5\xeb\xb8\xfc\xf1\xc77\xa0(;Q#td\xab\xf9\x03\x07!\x84n\xde\xbc\
Y\x89\xc5b\xe7\xe6\xe6\xe6\xa6m\xdb~\x87s\xbeBnn\x05\x02\x01\xaf|(\xdd\xe4\
\x05\xb0\xb8\x08\x02\x8b\x9bX.DT\xd3\x10\x89D\xbc\r\xde\x0f.\\\xf8\xc7_N\x9d\
:h\x9afSoo/\x000!D\xd5d\xab\x08@\n\n\x08\x80\xc0\xf5\xeb\xd7\x83\xd1h4\xcc\
\x18\xbb\x1d\x8f\xc7_\xd34\xed\x8fB\x88\xf5\xb2\x92TU\xd5\xab\x83J!\xfc\xabq\
\xd1\xde(\xe7x2?\x8f\xf9\xb99\xe8\xba\xce\xde?\x7f\xfe\xcfg\xcf\x9e\x1dr\x1c\
\xa7\xc50\x8c,\n\xd1a\x12B\x9cj\x10\x95\xde\x07<\xf1\x00B\x00\xc2\xd9lV\x03\
\xa0MMM\xe5fgg\x7f\x9bH$~\x1c\x8dF\x7f\xce\x18{\x91R\xea\x89\x97\xaf\xa1\x94\
\x16\xa2\xd30\x0c0\xce\x17\x8b3_h\xe5\xf3yq\xfe\xc2\x85O\x87\x86\x86~?333E\
\x08\xd1l\xdb\x06|\x11\xe7\xea\xa9\x08Qq_\x08\x80\xe2\x9a\n (\xcdq\x9c\xa0\
\x10"<99y\x93Rz?\x91H|?\x14\nm\n\x06\x83\x9d\x94\xd2@\xe9\xef\x04\x86a\x80\
\xbb{J\xbe\xd5\xd5\xbcr\xf5\xea\xbf\xdf\x1b\x199\xa7\xeb\xfaC\xce\xb9\xcd\
\x18\x93\xcf\xa3\xae\xd5\xb5\x01U\t@\xa0\xb0\xc3\xc1\x008\x00l\xd7\x1c\x00\
\x9c\x15v\xb9\x18\x00;\x9dN_\xa5\x94\xfeKQ\x94fM\xd3\xba\x82\xc1`RU\xd5fJi\
\x94R\x1a\x9c\x99\x99\x11\x1f\x8d\x8e\x06u]\xcfLLL<\xfe\xf4\xb3\xcf\xae\x8f\
\x8d\x8d=\xe0\x9cg\x08!Y\xc6\x98\t\xc0p-\xe7Z\xd6\xfd\xdb\x02P5\x84\xaa\xfe\
\xc0A\x08\xa1.d\x13\n\xa1\xa4\xf9,\xea;F(\xa5Q\x00a\x00\x01Ji\x00\x85\xd1$\
\xbe\x81\xb08\xe7&\x00\x83\x10\x92c\x8ce\\\xa1\x19\x00\x0b\xee1\xeb\x9a\xe9\
\x0e\x18\x135\xe6\xe7\xba~\xa1qA\xfc0A\x17(\x0c \xe2\x1e\x83\xee\xb5\x80\xdb\
O\x86\x81\xdf\x93\x96+.\xefZ\xce=J\xc1\xd2\xcb\xa2\x96\xf0\x86\x00\xca\x00\
\xc9\x1c\x91P\x8a\xcf\x08\x8acX&#\xf7\x99\xe3\x83\xe2\x8d\x08~.\x00\xffK\xed\
\x1b\xff\xbf\x12\xff\x01lP\xf1\xda\xe2\x88E\xb2\x00\x00\x00\x00IEND\xaeB`\
\x82n\x06WM'
import os
import unittest

from os.path import realpath, sep, dirname

parentdir = dirname(dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from lib.xml_parser import parse_wallpapoz_file

tests_dir = dirname(realpath(__file__))


class WallpapozXmlParsingTests(unittest.TestCase):

    def test_parse_xml_workspaces_type(self):
        test_file = os.path.join(tests_dir, 'wallpapoz_example_workspace_type.xml')

        workspaces, conf = parse_wallpapoz_file(test_file)
        self.assertEqual(workspaces, [
            ('workspace1', ['/home/sky/Pictures/wallpapers/naruto.jpg',
                            '/home/sky/Pictures/wallpapers/bleach.jpg']),
            ('workspace_2', ['/home/sky/Pictures/wallpapers/lands_cape.gif',
                             '/home/sky/Pictures/wallpapers/cameron-highland.gif']),
            ('workspace 3', ['/home/sky/wallpapers with space/paris.jpg',
                             '/home/sky/wallpapers with space/café.jpg']),
            ('workspaceчетири', ['/home/sky/unicode/漢語.png',
                                 '/home/sky/unicode/日本語.png'])
        ])

    def test_parse_xml_desktop_type(self):
        test_file = os.path.join(tests_dir, 'wallpapoz_example_desktop_type.xml')
        files, conf = parse_wallpapoz_file(test_file)
        self.assertEqual(files, ['/home/sky/Pictures/wallpapers/naruto.jpg',
                                 '/home/sky/Pictures/wallpapers/bleach.jpg',
                                 '/home/sky/Pictures/wallpapers/lands_cape.gif',
                                 '/home/sky/Pictures/wallpapers/cameron-highland.gif',
                                 '/home/sky/wallpapers with space/paris.jpg',
                                 '/home/sky/wallpapers with space/café.jpg',
                                 '/home/sky/unicode/漢語.png',
                                 '/home/sky/unicode/日本語.png'])


if __name__ == '__main__':
    unittest.main()

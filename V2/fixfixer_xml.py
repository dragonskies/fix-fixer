################################################################################
# Copyright (c) 2012  Timothy Davis
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
################################################################################

"""XML-related functions for Fix Fixer"""

import xml.etree.ElementTree
import os

fix_xml = xml.etree.ElementTree.parse( os.path.join('resources', 'fields.xml') )

def find_tag_desc(find_tag):
    for each_element in fix_xml.getroot().getchildren():
        tag_text=each_element.find('.//Tag')
        #print tag_text.text
        desc_text = each_element.find('.//Desc')
        # print desc_text.text
        if tag_text.text == find_tag:
            return str(desc_text.text)
    #nothing found
    return "Tag [%s] could not be found." % find_tag

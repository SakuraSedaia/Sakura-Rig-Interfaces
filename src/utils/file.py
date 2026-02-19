# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import shutil

def ensure_directory(path):
    """
    Ensures that a directory exists, creating it if necessary.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False

def copy_file(src, dst):
    """
    Copies a file from src to dst.
    """
    try:
        shutil.copy2(src, dst)
        return True
    except Exception as e:
        print(f"Error copying file: {e}")
        return False

def delete_file(path):
    """
    Deletes a file if it exists.
    """
    if os.path.exists(path):
        os.remove(path)
        return True
    return False

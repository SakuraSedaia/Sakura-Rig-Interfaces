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
import json

def ensure_directory(path):
    """
    Ensures that a directory exists, creating it if necessary.
    """
    if not path:
        return False
    
    # If path is a file, get directory
    if os.path.isfile(path) or ('.' in os.path.basename(path) and not os.path.isdir(path)):
        dir_path = os.path.dirname(path)
    else:
        dir_path = path

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        return True
    return False

def read_json(path):
    """
    Reads a JSON file and returns the data.
    """
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading JSON: {e}")
    return {}

def write_json(path, data):
    """
    Writes data to a JSON file.
    """
    try:
        ensure_directory(path)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error writing JSON: {e}")
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

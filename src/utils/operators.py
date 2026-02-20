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

import bpy
import bpy.types as T
import os
import json
import urllib.request as request
from . import config as C
from . import file as F

def allow_online():
    # In legacy it checked system properties, here we might want a preference or just return True
    return True

def retrieveJSON(url):
    try:
        with request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error retrieving JSON from {url}: {e}")
        return "http"

def download(url, path):
    try:
        F.ensure_directory(os.path.dirname(path))
        request.urlretrieve(url, path)
        return True
    except Exception as e:
        print(f"Error downloading {url} to {path}: {e}")
        return False

def grabProfile(uuid):
    url = f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
    data = retrieveJSON(url)
    if data == "http":
        return None
    
    import base64
    for prop in data.get("properties", []):
        if prop["name"] == "textures":
            decoded = base64.b64decode(prop["value"]).decode()
            return json.loads(decoded)
    return None

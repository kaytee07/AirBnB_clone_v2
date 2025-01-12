#!/usr/bin/python3
# generates a .tgz archive from the contents of web_static.
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    archive_path = "versions/{}".format(archive_name)
    current_directory = os.getcwd()
    versions_directory = os.path.join(current_directory, "versions")
    archive_path1 = os.path.join(versions_directory, archive_name)

    try:
        os.makedirs(versions_directory, exist_ok=True)
        local("tar -czvf {} web_static".format(archive_path))
        archive_size = os.path.getsize(archive_path)

        print("web_static packed: {} -> {}Bytes"
              .format(archive_path, archive_size))
        return archive_path
    except Exception as e:
        return None

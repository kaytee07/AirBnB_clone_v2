from fabric.api import run, env, put
import os


env.hosts = ['xx-web-01', 'xx-web-02']  # Replace with your web server names
env.user = 'your-username'  # Replace with your SSH username
env.key_filename = 'path-to-your-ssh-key'  # Replace with the path to your SSH key


def do_deploy(archive_path):
    """Distribute the archive to the web servers and deploy the code."""
    if not os.path.isfile(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_base_name = os.path.splitext(archive_name)[0]
        releases_path = "/data/web_static/releases/{}/".format(archive_base_name)

        # Upload the archive to /tmp/ directory on the web servers
        put(archive_path, "/tmp/")

        # Uncompress the archive to the releases path
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, releases_path))

        # Delete the archive from the web servers
        run("rm /tmp/{}".format(archive_name))

        # Delete the current symbolic link and create a new one
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))

        print("Deployment completed!")
        return True

    except Exception as e:
        print("Deployment failed: {}".format(e))
        return False

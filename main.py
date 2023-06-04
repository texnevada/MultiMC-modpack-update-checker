import argparse
import os
import sys

import requests
import urllib.parse


parser = argparse.ArgumentParser(description="Mod File Checker")
parser.add_argument("--manifest", help="URL of the manifest file")
args = parser.parse_args()


def download_file(url, file_name):
    response = requests.get(f"{url}/{file_name}")
    if response.status_code == 200:
        with open(f"./mods/{file_name}", 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {file_name}")


def delete_file(file_name):
    os.remove(file_name)
    print(f"Deleted: {file_name}")


def main(manifest_url, mods_folder):
    files = []
    urls = []

    # Download the manifest file
    response = requests.get(manifest_url)
    if response.status_code == 200:
        manifest = response.text.splitlines()
        for url in manifest:
            if url.startswith("http"):
                url, jar_file = url.rsplit("/", 1)
                jar_file = urllib.parse.unquote(jar_file)
                files.append(jar_file)
                urls.append(url)
    else:
        print("Failed to download the manifest file.")
        sys.exit(0)

    # Compare files to the manifest
    marked_deletions = []
    custom_mods = []
    to_be_replaced = []

    replace_mods_only = True

    print_statement = 0
    for file_name in os.listdir(mods_folder):
        file_path = os.path.join(mods_folder, file_name)
        if os.path.isfile(file_path):
            for new_name in files:
                if file_name != new_name and file_name.startswith(new_name.split(".")[0]):
                    if print_statement == 0:
                        print_statement += 1
                        print("########## The following files will be updated ##########")
                    marked_deletions.append(file_name)
                    to_be_replaced.append(new_name)
                    print(f"{file_name} -> {new_name}")

    print_statement = 0
    for file_name in os.listdir(mods_folder):
        file_path = os.path.join(mods_folder, file_name)
        if os.path.isfile(file_path):
            for old_name in files:
                if file_name != old_name and file_name.startswith(old_name.split(".")[0]) and file_name in to_be_replaced:
                    if print_statement == 0:
                        print_statement += 1
                        print("########## The following files will be deleted ##########")
                        replace_mods_only = False
                    marked_deletions.append(file_name)
                    print(file_name)
            if file_name not in files:
                if file_name not in marked_deletions:
                    if file_name != new_name and file_name.startswith(new_name.split(".")[0]):
                        if print_statement == 0:
                            print_statement += 1
                            print("########## The following files is marked for deletion ##########")

                        marked_deletions.append(file_name)
                        custom_mods.append(file_name)
                        print(file_name)

    print_statement = 0
    for file_name in files:
        if file_name not in to_be_replaced and file_name not in os.listdir(mods_folder):
            if print_statement == 0:
                print_statement += 1
                print("########## The following files will be downloaded ##########")
            print(file_name)

    # Determine if user has custom mods

    if replace_mods_only is True:
        has_custom_mods = False
    else:
        has_custom_mods = input("Do you have any custom mods installed? (y/n): ").lower() == 'y'
    # Delete missing files (if any)
    if marked_deletions:
        print("#################### Deleting files ####################")
        for file_name in marked_deletions:
            if file_name in custom_mods and has_custom_mods is not False:
                print(file_name)
                answer = input("Do you want to keep this file? (y/n): ")
                if answer.lower() != 'y':
                    delete_file(os.path.join(mods_folder, file_name))
            else:
                delete_file(os.path.join(mods_folder, file_name))

    # Download missing files from the manifest
    for url, file in zip(urls, files):
        # Download the file if missing
        if file not in os.listdir(mods_folder):
            download_file(url, file)


if __name__ == "__main__":

    if args.manifest:
        main(args.manifest, "./mods/")
    else:
        print(f"No manifest URL provided.")

import os


def get_files(input_dir: str, extension: str = ".*", output_dir: str = None):
    """
    small program to produce a txt file containing all files with extension matching that provided.
    If no extension is provided, all files are returned.
    """
    if output_dir == None:
        output_dir = input_dir
    os.chdir(output_dir)
    count = 0
    output = open("files.txt", "w")
    if extension != ".*":
        for file in os.listdir(input_dir):
            if file.endswith(extension.lower()):
                path = os.path.join(input_dir, file)
                output.write(f"\n {path}")
                count = count + 1
        output.close()
        if count == 0:
            output_text = f"No files with extension {extension} found."
        else:
            output_text = f"{count} file(s) with extension '{extension}' found. \nList saved as 'files.txt' in {output_dir}"
    else:
        for file in os.listdir(input_dir):
            path = os.path.join(input_dir, file)
            output.write(f"\n {path}")
            count = count + 1
        if count == 0:
            output_text = f"No files found."
        else:
            output_text = (
                f"{count} file(s) found. \nList saved as 'files.txt' in {output_dir}"
            )
    return output_text


def recursive_get_files(input_dir: str, extension: str = ".*", output_dir: str = None):
    if output_dir == None:
        output_dir = input_dir
    os.chdir(output_dir)
    count = 0
    output = open("files.txt", "w")
    if extension == ".*":
        for directory, subdirs, files in os.walk(input_dir):
            for file in files:
                path = os.path.join(directory, file)
                output.write(f"\n {path}")
                count = count + 1
        output_text = (
            f"{count} files found. Output saved as 'files.txt' in {output_dir}"
        )
    else:
        for directory, subdirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith(extension.lower()):
                    path = os.path.join(directory, file)
                    output.write(f"\n {path}")
                    count = count + 1
        if count == 0:
            output_text = f"No files with extension {extension} found."
        else:
            output_text = f"{count} file(s) with extension '{extension}' found. \nList saved as 'files.txt' in {output_dir}"
    return output_text


# print(get_files(input_dir="/Users/James/"))

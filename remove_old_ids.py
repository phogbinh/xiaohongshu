def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('\n'.join(data))

def main():
    # File paths
    ids_new_path = 'ids-new.txt'
    ids_path = 'ids.txt'
    ids_exclude_path = 'ids-exclude.txt'

    # Read the content of the files
    ids_new_set = read_file(ids_new_path)
    ids_set = read_file(ids_path)

    # Remove common strings
    ids_exclude_set = ids_new_set - ids_set

    # Write the result to the output file
    write_file(ids_exclude_path, ids_exclude_set)

if __name__ == "__main__":
    main()

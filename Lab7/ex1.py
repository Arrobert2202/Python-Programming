import os
import sys

def find_read_file(directory_path, file_extension):
  try:
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
      raise NotADirectoryError(f"Invalid directory path: {directory_path}")

    if not file_extension.startswith('.'):
      raise ValueError("File extension should start with '.'")

    files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]

    if not files:
      print(f"There are no files with '{file_extension}' extension")

    for file in files:
      file_path = os.path.join(directory_path, file)
      try:
        with open(file_path, 'r') as f:
          content = f.read()
          print(f"File {file}: {content}")
          print()
      except FileNotFoundError as e:
        print(f"File not found: {file_path}")
      except PermissionError as e:
        print(f"Permission error for file {file}: {e}")
      except Exception as e:
        print(f"Error reading file {file}: {e}")
  except (NotADirectoryError, ValueError, Exception) as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Error: 2 arguments")
  else:
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    find_read_file(directory_path, file_extension)
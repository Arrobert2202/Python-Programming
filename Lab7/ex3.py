import sys
import os

def total_size(directory_path):
  size = 0

  try:
    if not os.path.exists(directory_path):
      raise FileNotFoundError(f"The directory {directory_path} doesn't exist")

    for (root, directories, files) in os.walk(directory_path):
      for file_name in files:
        file_path = os.path.join(root, file_name)
        try:
          size += os.path.getsize(file_path)
        except OSError as e:
          print(f"Error accessing file '{file_path}': {e}")
          
    print(f"Directory {directory_path}'s total size is: {size}")
  
  except PermissionError:
    print(f"Error: Permission denied to files in {directory_path}")
if __name__ == "__main__":
  if len(sys.argv)!=2:
    print("Error: add an argument")
  else:
    directory_path = sys.argv[1]

    total_size(directory_path)
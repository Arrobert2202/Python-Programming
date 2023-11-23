import sys
import os

def rename_files(directory_path):
  try:
    if not os.path.exists(directory_path):
      raise FileNotFoundError(f"The directory {directory_path} doesn't exist")
    
    files = os.listdir(directory_path)

    for i, file_name in enumerate(files):
      old_file_path = os.path.join(directory_path, file_name)
      new_file_name = f"file{i}.{file_name.split('.')[-1]}"
      new_file_path = os.path.join(directory_path, new_file_name)

      try:
        os.rename(old_file_path, new_file_path)
      except OSError as e:
        print(f"Error renaming {file_name}: {e}")
  except FileNotFoundError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  if len(sys.argv)!=2:
    print("Error: not 1 argument")
  else:
    directory_path = sys.argv[1]
    rename_files(directory_path)

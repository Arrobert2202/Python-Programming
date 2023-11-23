import sys
import os

def count_files(directory_path):
  try:
    if not os.path.exists(directory_path):
      raise FileNotFoundError(f"The directory {directory_path} doesn't exist")
    
    files = os.listdir(directory_path)
    if not files:
      raise ValueError(f"Directory is empty: {directory_path}")

    extension_counts = {}
    for file in files:
      _, extension = os.path.splitext(file)
      extension_counts[extension] = extension_counts.get(extension, 0) + 1

    for extension, count in extension_counts.items():
      print(f"Number of files with extension {extension}: {count}")
  
  except (FileNotFoundError, NotADirectoryError, ValueError, Exception) as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  if len(sys.argv)!=2:
    print("Error: add an argument")
    sys.exit(1)
  else:
    directory_path = sys.argv[1]

    count_files(directory_path)
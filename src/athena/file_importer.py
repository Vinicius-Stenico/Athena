from pathlib import Path


def list_files(inbox: Path) -> list[Path]:
    found_files = []

    for item in inbox.iterdir():
        if item.is_file():
            found_files.append(item)

    return found_files


def filter_files(files: list[Path]) -> list[Path]:
    supported_extensions = {".pdf", ".docx", ".txt", ".md"}
    filtred_files = []

    for file in files:
        extension = file.suffix.lower()

        if extension in supported_extensions:
            filtred_files.append(file)
        else:
            print(f"O arquivo {file} não é suportado")

    return filtred_files

def get_supported_files(inbox: Path) -> list[Path]:
	files = list_files(inbox)
	filtred_files = filter_files(files)
	return filtred_files

if __name__ == "__main__":
	inbox = Path("inbox")
	
	print(get_supported_files(inbox))
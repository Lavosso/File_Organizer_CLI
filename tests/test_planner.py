from src import planner


def test_planner():
    data_files = ["outro.mp3","regulamin_sklepu.pdf","deklaracja.pdf","test_main.py",
                        "harmonogram.txt","pies.jpg","scraper.py"]
    data_file_types = ['.txt', '.jpg', '.pdf', '.py', '.mp3']
    correct_result = {'.txt': ['harmonogram.txt'],
                      '.jpg': ['pies.jpg'],
                      '.pdf': ['regulamin_sklepu.pdf', 'deklaracja.pdf'],
                      '.py': ['test_main.py', 'scraper.py'],
                      '.mp3': ['outro.mp3']}
    assert correct_result == planner.map_files(data_files, data_file_types)
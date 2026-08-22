from src import cli


def test_print_and_confirm_plan():
    plan = {
        ".txt": ["harmonogram.txt"],
        ".jpg": ["pies.jpg"],
        ".pdf": ["regulamin_sklepu.pdf", "deklaracja.pdf"],
        ".py": ["test_main.py", "scraper.py"],
        ".mp3": ["outro.mp3"],
    }
    cli.print_plan(plan)
    assert True

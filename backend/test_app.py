from app import save_task


def test_save_task():

    filename = "tes1t.txt"

    save_task("hello world", filename)

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    assert content == "hello world"
from src.cracker import PasswordCracker


def test_password_crack():
    output_path = 'tests/res/steghide_crack_output'
    password_cracker = PasswordCracker('tests/res/password/dog.jpg', 'tests/res/password/common.txt', output_path)
    password_cracker.run()

    with open(output_path, 'r') as out, open('tests/res/hidden/hidden.txt', 'r') as hidden:
        assert out.read() == hidden.read()

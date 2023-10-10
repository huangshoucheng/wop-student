def test_print_hello_world(capsys):
    # Arrange
    expected_output = "hello world\n"
    
    # Act
    print("hello world")
    captured_output = capsys.readouterr().out
    
    # Assert
    # assert captured_output == expected_output
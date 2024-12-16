from scaflog_mcp_server.server import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n" 
import pytest
from scaflog_mcp_server.server import main
from scaflog_mcp_server.environment import EnvironmentManager

@pytest.fixture(autouse=True)
def setup_test_environment():
    EnvironmentManager.init("testing")
    yield
    
def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out 
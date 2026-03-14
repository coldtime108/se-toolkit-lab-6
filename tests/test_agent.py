import subprocess
import json

def test_agent():
    result = subprocess.run(
        ["uv", "run", "agent.py", "What is 2+2?"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    try:
        output = json.loads(result.stdout)
    except json.JSONDecodeError:
        assert False, "stdout is not valid JSON"
    assert "answer" in output
    assert "tool_calls" in output
    assert isinstance(output["tool_calls"], list)

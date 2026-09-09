"""Tests basic project structure and imports."""


def test_project_structure_exists():
    """Verify the project structure is in place."""
    import os

    expected_dirs = [
        "data",
        "notebooks",
        "src",
        "models",
        "dashboard",
        "tests",
        "docs",
    ]

    for directory in expected_dirs:
        assert os.path.isdir(directory), f"Missing directory: {directory}"


def test_requirements_file_exists():
    """Verify requirements.txt exists."""
    import os

    assert os.path.isfile("requirements.txt"), "requirements.txt missing"


def test_readme_exists():
    """Verify README.md exists."""
    import os

    assert os.path.isfile("README.md"), "README.md missing"


def test_gitignore_exists():
    """Verify .gitignore exists."""
    import os

    assert os.path.isfile(".gitignore"), ".gitignore missing"


def test_dashboard_app_exists():
    """Verify dashboard/app.py exists."""
    import os

    assert os.path.isfile("dashboard/app.py"), "dashboard/app.py missing"


def test_dashboard_imports_streamlit():
    """Verify dashboard/app.py imports streamlit."""
    import ast

    with open("dashboard/app.py", "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend([alias.name for alias in node.names])
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

    assert any("streamlit" in imp for imp in imports), (
        "dashboard/app.py should import streamlit"
    )


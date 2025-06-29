# LeetCode Solutions

A collection of Python solutions to LeetCode problems managed with [leetcode-cli](https://github.com/leetcode-tools/leetcode-cli).

## Structure

```
code/
├── __init__.py
├── 1.two-sum.py
├── 5.longest-palindromic-substring.py
├── 15.3sum.py
└── 25.reverse-nodes-in-k-group.py
```

## Setup

### Prerequisites
- Install [leetcode-cli](https://github.com/leetcode-tools/leetcode-cli)

### Configuration
The repository is configured with `leetcode.toml`:
- **Editor**: vim
- **Language**: Python 3
- **Code directory**: `code/`
- **Problems cache**: `Problems`

### Usage with leetcode-cli

```bash
# Show problem list
leetcode list

# Show problem details
leetcode show <problem-id>

# Test solution
leetcode test <problem-id>

# Submit solution
leetcode submit <problem-id>
```

### Manual Usage

Each file contains a `Solution` class with methods that solve the corresponding LeetCode problem:

```python
from code.problem_name import Solution

solution = Solution()
result = solution.method_name(inputs)
```

## Problems Solved

- **Problem 1**: Two Sum
- **Problem 5**: Longest Palindromic Substring
- **Problem 15**: 3Sum
- **Problem 25**: Reverse Nodes in k-Group

## Development

The repository uses:
- **leetcode-cli** for problem management and testing
- **Python type hints** for better code quality
- **Docstrings** for documentation
- **Ruff** for linting and formatting (configured in `ruff.toml`)
- **Pre-commit hooks** for code quality checks

### Code Quality Tools

```bash
# Run linting
ruff check

# Format code
ruff format

# Install pre-commit hooks
pre-commit install
```

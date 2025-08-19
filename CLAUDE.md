# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository contains code for the ARC-AGI Code Golf Competition, a challenge to implement the shortest possible Python solutions for 400 different tasks from the Abstraction and Reasoning Corpus (ARC-AGI). The goal is to create minimal Python programs that correctly transform input grids to output grids according to task-specific patterns.

## Common Commands

### Development Environment

```bash
# Build and start Docker container with GPU support
docker-compose up -d --build

# Run bash in the container
docker-compose exec app bash

# Check GPU availability
make gpu-check
# or directly:
python src/check_gpu.py
```

### Code Quality

```bash
# Lint code
make lint
# or directly:
ruff check .

# Format code
make format
# or directly:
ruff format .

# Clean temporary files
make clean
```

### Workflow

For each task:

1. Analyze the task examples in the Jupyter notebook
2. Develop a solution in the notebook
3. Optimize the solution for minimal character count
4. Test the solution against all test cases
5. Save the solution to the appropriate file in `src/my_src/`

## Code Architecture

### Directory Structure

- **inputs/** - Input data files
  - **google-code-golf-2025/** - Contains task JSON files (task001.json to task400.json) and utilities
    - **code_golf_utils/** - Utility functions for task testing and visualization
- **notebooks/** - Jupyter notebooks for exploring and solving tasks
  - Task notebooks named as `task_001.ipynb`, `task_002.ipynb`, etc.
- **outputs/** - Directory for generated outputs
- **src/** - Source code directory
  - **my_src/** - Contains optimized Python solutions for each task
    - Files named as `task001.py`, `task002.py`, etc.

### Key Components

1. **Task JSON Files**: Each task is defined by a JSON file containing:
   - `train`: Training examples with input/output grid pairs
   - `test`: Test examples for validation
   - `arc-gen`: Additional examples from ARC-GEN-100K dataset

2. **Solution Format**:
   - Each solution file should contain a single function (typically named `p`) that transforms input grids to output grids
   - Functions must be self-contained and only use Python standard libraries
   - Code should be minimized for character count while maintaining correctness

3. **Testing Process**:
   - Solutions can be tested in notebooks against all examples
   - Tests verify that each solution works correctly on all inputs

## Key Constraints

1. Only Python standard library may be used (no external dependencies)
2. Solutions must be self-contained in a single function
3. All solutions must transform input grids to output grids correctly
4. Code must be minimized for character count (evaluation formula: max(1, 2500 - character_count))

## Development Notes

- The repository contains a Dockerfile and docker-compose.yml for setting up a GPU-enabled environment
- Typical workflow involves developing in Jupyter notebooks and then optimizing solutions
- When optimizing, focus on reducing character count while maintaining functionality
- Use common code golf techniques to minimize character count
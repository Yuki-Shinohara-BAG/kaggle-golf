#!/usr/bin/env python3
import json
import os

def update_notebook(notebook_path):
    """Replace the test_json function with test_all in a notebook"""
    
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading {notebook_path}: {e}")
        return False
    
    # New test_all function to replace test_json
    test_all_function = """def test_all(task_num, solution_function=p, show_details=True):
    # テストデータと訓練データ、arc-genデータすべてでテストする機能強化版テスト関数
    with open(f"../inputs/google-code-golf-2025/task{task_num:03d}.json", "r", encoding="utf-8") as f:
        task_data = json.load(f)
    
    # 訓練データのテスト
    train_success = 0
    train_total = len(task_data["train"])
    if show_details:
        print("===== 訓練データ =====")
    
    for i, example in enumerate(task_data["train"]):
        input_grid = example["input"]
        expected_output = example["output"]
        actual_output = solution_function(input_grid)
        
        is_correct = actual_output == expected_output
        if is_correct:
            train_success += 1
        
        if show_details:
            status = "✓ 成功" if is_correct else "✗ 失敗"
            print(f"Train例{i+1}: {status}")
    
    if show_details or train_success < train_total:
        print(f"訓練データの成功率: {train_success}/{train_total}")
    
    # テストデータのテスト
    test_success = 0
    test_total = len(task_data["test"])
    if show_details:
        print("\\n===== テストデータ =====")
    
    for i, example in enumerate(task_data["test"]):
        input_grid = example["input"]
        expected_output = example["output"]
        actual_output = solution_function(input_grid)
        
        is_correct = actual_output == expected_output
        if is_correct:
            test_success += 1
        
        if show_details:
            status = "✓ 成功" if is_correct else "✗ 失敗"
            print(f"Test例{i+1}: {status}")
    
    if show_details or test_success < test_total:
        print(f"テストデータの成功率: {test_success}/{test_total}")
    
    # arc-genデータのテスト (追加された部分)
    arcgen_success = 0
    arcgen_total = len(task_data.get("arc-gen", []))
    
    if arcgen_total > 0:
        if show_details:
            print("\\n===== ARC-GENデータ =====")
        
        for i, example in enumerate(task_data["arc-gen"]):
            input_grid = example["input"]
            expected_output = example["output"]
            actual_output = solution_function(input_grid)
            
            is_correct = actual_output == expected_output
            if is_correct:
                arcgen_success += 1
            
            if show_details:
                status = "✓ 成功" if is_correct else "✗ 失敗"
                print(f"ARC-GEN例{i+1}: {status}")
        
        if show_details or arcgen_success < arcgen_total:
            print(f"ARC-GENデータの成功率: {arcgen_success}/{arcgen_total}")
    
    # 総合成功率
    total_success = train_success + test_success + arcgen_success
    total_examples = train_total + test_total + arcgen_total
    
    print("\\n===== 総合評価 =====")
    print(f"総合成功率: {total_success}/{total_examples} ({total_success/total_examples*100:.2f}%)")
    
    # 全例成功したかどうか
    all_passed = total_success == total_examples
    print(f"全テスト通過: {'✓ 成功' if all_passed else '✗ 失敗'}")
    
    return all_passed"""
    
    # Extract task number from filename
    filename = os.path.basename(notebook_path)
    task_num = int(filename.split('_')[1].split('.')[0])
    
    # Add test execution cell content
    test_execution_cell = f"# テスト実行\ntest_all({task_num}, p)"
    
    # Find and replace the test_json function or add test_all if not found
    test_json_found = False
    test_execution_found = False
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Check for test_json function
            if 'def test_json():' in ''.join(cell['source']):
                cell['source'] = [test_all_function]
                test_json_found = True
            
            # Check for test_json() execution
            elif 'test_json()' in ''.join(cell['source']):
                cell['source'] = [test_execution_cell]
                test_execution_found = True
    
    # Add new cells if needed
    if not test_json_found:
        # Create a new cell for test_all function
        test_all_cell = {
            "cell_type": "code",
            "execution_count": None,
            "id": "test_all_cell",
            "metadata": {},
            "outputs": [],
            "source": [test_all_function]
        }
        notebook['cells'].append(test_all_cell)
    
    if not test_execution_found:
        # Create a new cell for test execution
        test_run_cell = {
            "cell_type": "code",
            "execution_count": None,
            "id": "test_run_cell",
            "metadata": {},
            "outputs": [],
            "source": [test_execution_cell]
        }
        notebook['cells'].append(test_run_cell)
    
    # Write updated notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
    
    return True

def main():
    """Update all task notebooks with the new test_all function"""
    notebooks_dir = 'notebooks'
    
    # Skip task_000.ipynb since it already has the new function
    notebooks = [f for f in os.listdir(notebooks_dir) 
                if f.startswith('task_') and f.endswith('.ipynb') and f != 'task_000.ipynb']
    
    # Sort notebooks by task number for better organization
    notebooks.sort()
    
    updated_count = 0
    for notebook in notebooks:
        notebook_path = os.path.join(notebooks_dir, notebook)
        success = update_notebook(notebook_path)
        if success:
            updated_count += 1
            print(f"Updated {notebook}")
    
    print(f"\nSuccessfully updated {updated_count} notebooks with the new test_all function.")

if __name__ == "__main__":
    main()
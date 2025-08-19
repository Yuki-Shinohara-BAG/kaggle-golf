def p(g):
    """
    ARC Task: Extract the quadrant with different number pattern
    
    Input: Grid divided into 4 quadrants separated by rows/columns of zeros
    Output: The quadrant that has a different number distribution pattern
    """
    height = len(g)
    width = len(g[0])
    
    # Step 1: Find separator rows and columns (filled with zeros)
    separator_rows = []
    separator_cols = []
    
    for r in range(height):
        if all(cell == 0 for cell in g[r]):
            separator_rows.append(r)
    
    for c in range(width):
        if all(g[r][c] == 0 for r in range(height)):
            separator_cols.append(c)
    
    # Step 2: Determine quadrant boundaries
    row_split = min(separator_rows)
    col_split = min(separator_cols) 
    row_split2 = max(separator_rows) + 1
    col_split2 = max(separator_cols) + 1
    
    # Step 3: Extract the 4 quadrants
    top_left = []
    top_right = []
    bottom_left = []
    bottom_right = []
    
    for r in range(row_split):
        top_left.append(g[r][:col_split])
        top_right.append(g[r][col_split2:])
    
    for r in range(row_split2, height):
        bottom_left.append(g[r][:col_split])
        bottom_right.append(g[r][col_split2:])
    
    # Step 4: Analyze number distribution in each quadrant
    def get_number_set(quadrant):
        """Get unique numbers in quadrant"""
        numbers = set()
        for row in quadrant:
            for cell in row:
                numbers.add(cell)
        return numbers
    
    quadrants = [
        (top_left, "top_left"),
        (top_right, "top_right"), 
        (bottom_left, "bottom_left"),
        (bottom_right, "bottom_right")
    ]
    
    # Step 5: Find the quadrant with different pattern
    number_patterns = []
    for quadrant, name in quadrants:
        pattern = get_number_set(quadrant)
        number_patterns.append((quadrant, pattern, name))
    
    # Step 6: Identify unique pattern
    for i, (quad_i, pattern_i, name_i) in enumerate(number_patterns):
        different_count = 0
        for j, (quad_j, pattern_j, name_j) in enumerate(number_patterns):
            if i != j and pattern_i != pattern_j:
                different_count += 1
        
        # If this quadrant differs from most others, return it
        if different_count >= 2:  # Different from at least 2 others
            return quad_i
    
    # Fallback: if no clear unique pattern, return bottom_left
    return bottom_left
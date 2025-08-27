# Shared Utilities for Data Science Assignments

This folder contains reusable utilities that can be used across all data science assignments throughout the semester.

## FileAnalyzer Class

The `FileAnalyzer` class provides comprehensive file and data analysis capabilities.

### Features

- **File Information**: Size, type, format detection
- **DataFrame Analysis**: Shape, data quality checks
- **Human-readable Output**: File sizes in KB, MB, GB format
- **Error Handling**: Robust error handling for missing files
- **Multiple Formats**: Supports CSV, Excel, JSON, Parquet files
- **Data Quality**: Detects null rows, duplicate rows, column types

### Usage Examples

#### Basic Usage
```python
import sys
sys.path.append('../../shared')  # Adjust path as needed
from file_analyzer import FileAnalyzer

# Create analyzer
analyzer = FileAnalyzer('./your_file.csv')

# Print summary
analyzer.print_summary()

# Get DataFrame
df = analyzer.get_dataframe()
```

#### Quick Analysis
```python
from file_analyzer import analyze_file

# Quick analysis with summary
analysis = analyze_file('./your_file.csv', print_summary=True)
```

#### Accessing Specific Information
```python
analyzer = FileAnalyzer('./your_file.csv')
analysis = analyzer.get_comprehensive_analysis()

# File info
file_info = analysis['file_info']
print(f"Size: {file_info['size_readable']}")

# DataFrame info
df_info = analysis['dataframe_info']
print(f"Rows: {df_info['rows']}, Columns: {df_info['columns']}")
```

### Output Example

```
==================================================
FILE ANALYSIS SUMMARY
==================================================
📁 File: your_data.csv
📊 Type: CSV
💾 Size: 293.8 KB
📈 Shape: (309, 14)
🔢 Columns: 14
📋 Rows: 309
==================================================
```

## Extending the Utilities

You can easily extend the `FileAnalyzer` class by adding new methods:

```python
class FileAnalyzer:
    # ... existing code ...
    
    def get_statistical_summary(self):
        """Add statistical analysis methods."""
        df = self.get_dataframe()
        return df.describe()
    
    def check_data_quality(self):
        """Add custom data quality checks."""
        # Your custom logic here
        pass
```

## File Structure

```
assignments/shared/
├── __init__.py          # Package initialization
├── file_analyzer.py     # Main FileAnalyzer class
└── README.md           # This documentation
```

## Dependencies

- pandas
- pathlib (built-in)
- os (built-in)
- typing (built-in)

## Future Enhancements

Consider adding these features as the semester progresses:

- [ ] Statistical analysis methods
- [ ] Data visualization helpers
- [ ] Data cleaning utilities
- [ ] Export functionality
- [ ] Performance profiling
- [ ] Data validation rules

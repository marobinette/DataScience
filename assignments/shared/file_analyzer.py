import os
import pandas as pd
from pathlib import Path
from typing import Dict, Any, Optional, Union


class FileAnalyzer:
    """
    A utility class for analyzing data files and providing useful metadata.
    Can be extended throughout the semester with additional analysis functions.
    """
    
    def __init__(self, file_path: str):
        """
        Initialize the FileAnalyzer with a file path.
        
        Args:
            file_path (str): Path to the file to analyze
        """
        self.file_path = Path(file_path)
        self._df = None
    
    def get_file_info(self) -> Dict[str, Any]:
        """
        Get comprehensive file information including size, format, and basic stats.
        
        Returns:
            Dict containing file metadata
        """
        if not self.file_path.exists():
            return {"error": f"File '{self.file_path}' not found"}
        
        try:
            # Get file size
            size_bytes = self.file_path.stat().st_size
            
            # Convert to human-readable format
            size_readable = self._bytes_to_readable(size_bytes)
            
            # Get file extension
            file_extension = self.file_path.suffix.lower()
            
            # Determine file type
            file_type = self._get_file_type(file_extension)
            
            return {
                "file_path": str(self.file_path),
                "file_name": self.file_path.name,
                "file_extension": file_extension,
                "file_type": file_type,
                "size_bytes": size_bytes,
                "size_readable": size_readable,
                "exists": True
            }
        except OSError as e:
            return {"error": f"Error accessing file: {e}"}
    
    def get_dataframe_info(self) -> Dict[str, Any]:
        """
        Get DataFrame information including shape, and basic stats.
        
        Returns:
            Dict containing DataFrame metadata
        """
        try:
            if self._df is None:
                self._load_dataframe()
            
            if self._df is None:
                return {"error": "Could not load DataFrame"}
            
            # Basic info
            shape = self._df.shape
            
            # Column info
            column_info = {
                "total_columns": len(self._df.columns),
                "column_names": list(self._df.columns),
                "column_types": self._df.dtypes.to_dict(),
                "null_counts": self._df.isnull().sum().to_dict()
            }
            
            # Row info
            row_info = {
                "total_rows": len(self._df),
                "null_rows": self._df.isnull().all(axis=1).sum(),
                "duplicate_rows": self._df.duplicated().sum()
            }
            
            return {
                "shape": shape,
                "rows": shape[0],
                "columns": shape[1],
                "column_info": column_info,
                "row_info": row_info
            }
        except Exception as e:
            return {"error": f"Error analyzing DataFrame: {e}"}
    
    def get_comprehensive_analysis(self) -> Dict[str, Any]:
        """
        Get both file and DataFrame information in one call.
        
        Returns:
            Dict containing both file and data analysis
        """
        file_info = self.get_file_info()
        df_info = self.get_dataframe_info()
        
        return {
            "file_info": file_info,
            "dataframe_info": df_info,
            "analysis_timestamp": pd.Timestamp.now().isoformat()
        }
    
    def _load_dataframe(self) -> None:
        """Load the DataFrame based on file extension."""
        if not self.file_path.exists():
            self._df = None
            return
        
        try:
            file_extension = self.file_path.suffix.lower()
            
            if file_extension == '.csv':
                self._df = pd.read_csv(self.file_path)
            elif file_extension in ['.xlsx', '.xls']:
                self._df = pd.read_excel(self.file_path)
            elif file_extension == '.json':
                self._df = pd.read_json(self.file_path)
            elif file_extension == '.parquet':
                self._df = pd.read_parquet(self.file_path)
            else:
                print(f"Unsupported file format: {file_extension}")
                self._df = None
        except Exception as e:
            print(f"Error loading file: {e}")
            self._df = None
    
    def _bytes_to_readable(self, size_bytes: int) -> str:
        """Convert bytes to human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def _get_file_type(self, extension: str) -> str:
        """Determine file type based on extension."""
        file_types = {
            '.csv': 'CSV',
            '.xlsx': 'Excel',
            '.xls': 'Excel',
            '.json': 'JSON',
            '.parquet': 'Parquet',
            '.txt': 'Text',
            '.tsv': 'TSV'
        }
        return file_types.get(extension, 'Unknown')
    
    def get_dataframe(self) -> Optional[pd.DataFrame]:
        """
        Get the loaded DataFrame.
        
        Returns:
            pandas DataFrame or None if loading failed
        """
        if self._df is None:
            self._load_dataframe()
        return self._df
    
    def print_summary(self) -> None:
        """Print a formatted summary of the file and data analysis."""
        analysis = self.get_comprehensive_analysis()
        
        print("=" * 50)
        print("FILE ANALYSIS SUMMARY")
        print("=" * 50)
        
        # File info
        file_info = analysis.get("file_info", {})
        if "error" in file_info:
            print(f"❌ {file_info['error']}")
            return
        
        print(f"📁 File: {file_info['file_name']}")
        print(f"📊 Type: {file_info['file_type']}")
        print(f"💾 Size: {file_info['size_readable']}")
        
        # DataFrame info
        df_info = analysis.get("dataframe_info", {})
        if "error" in df_info:
            print(f"❌ {df_info['error']}")
            return
        
        print(f"📈 Shape: {df_info['shape']}")
        print(f"🔢 Columns: {df_info['column_info']['total_columns']}")
        print(f"📋 Rows: {df_info['row_info']['total_rows']}")
        
        if df_info['row_info']['null_rows'] > 0:
            print(f"⚠️  Null rows: {df_info['row_info']['null_rows']}")
        
        if df_info['row_info']['duplicate_rows'] > 0:
            print(f"🔄 Duplicate rows: {df_info['row_info']['duplicate_rows']}")
        
        print("=" * 50)


# Convenience function for quick analysis
def analyze_file(file_path: str, print_summary: bool = True) -> Dict[str, Any]:
    """
    Quick function to analyze a file and optionally print summary.
    
    Args:
        file_path (str): Path to the file
        print_summary (bool): Whether to print formatted summary
    
    Returns:
        Dict containing analysis results
    """
    analyzer = FileAnalyzer(file_path)
    analysis = analyzer.get_comprehensive_analysis()
    
    if print_summary:
        analyzer.print_summary()
    
    return analysis

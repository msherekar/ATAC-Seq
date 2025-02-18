from streaming.__main__ import run_streaming_pipeline
from src.atac.main import run_processing_pipeline

if __name__ == "__main__":
    print("🚀 Running Full ATAC-Seq Pipeline...")
    
    # Step 1: Download ATAC-Seq Data
    run_streaming_pipeline()

    # Step 2: Process ATAC-Seq Data
    run_processing_pipeline()
    
    print("✅ Full Pipeline Completed!")
    print("🚀 Running Full ATAC-Seq Pipeline...")
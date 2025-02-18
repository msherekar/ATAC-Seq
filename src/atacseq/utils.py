import logging

# Configure logging
logging.basicConfig(
    filename="../logs/pipeline.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(message, level="info"):
    """
    Logs messages with different severity levels.
    """
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)

# Usage Example
log_message("ATAC-Seq pipeline started", "info")

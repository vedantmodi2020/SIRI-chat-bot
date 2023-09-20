#!/bin/bash

# Run the spt command
spt

# Sleep for 10 seconds
sleep 10

# Send Ctrl+C (interrupt signal)
kill -INT $$

# Exit the script
exit 0

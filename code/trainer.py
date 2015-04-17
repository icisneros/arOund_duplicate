""" ****************************************************************
	
	The equivalent of a make file, in the sense that it trains the
	crawled tweets (runs training stages 1 and 2) and then run 
	analytics on the result, outputting the results to analytics.txt

    **************************************************************"""

import sys
import subprocess

# Run trainer_stage1.py
trainer_stage1 = subprocess.Popen([sys.executable, "trainer_stage1.py"])
trainer_stage1.communicate()

# Run trainer_stage2.py
trainer_stage2 = subprocess.Popen([sys.executable, "trainer_stage2.py"])
trainer_stage2.communicate()

# Run analytics.py
analytics = subprocess.Popen([sys.executable, "analytics.py"])
analytics.communicate()
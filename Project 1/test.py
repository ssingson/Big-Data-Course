import subprocess

# set the variable in Python
var1 = "hello world"

# pass the variable to Bash using subprocess
subprocess.run(["bash", "-c", f'export MY_VAR="{var1}"'])

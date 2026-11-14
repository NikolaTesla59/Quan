import re

# Let's see the string tables and function lookups for validator.js
with open(r"C:\Users\Admin\Downloads\95GG_PRO\core\validator.js", "r", encoding="utf-8") as f:
    val_content = f.read()

# Let's evaluate validator's strings using node
node_script = """
const fs = require('fs');
let code = fs.readFileSync('C:\\\\Users\\\\Admin\\\\Downloads\\\\95GG_PRO\\\\core\\\\validator.js', 'utf8');
// Extract the string table function and deobfuscation function
// Run in node
eval(code);
"""

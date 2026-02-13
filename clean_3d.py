import re

# Read the file
with open(r'e:\Library of us\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the world-container opening div (line ~1151)
content = content.replace('<div class="world-container">', '')

# Find and remove the entire 3D animation block
# From "/* --- 3D Infinite Hallway Logic ---" to just before "class Particle"
pattern = r'/\* ---.*?3D.*?Hallway.*?Logic.*?---.*?\*/.*?setTimeout\(.*?\{.*?\}\, 100\);.*?(?=\s+class Particle)'
content = re.sub(pattern, '// 3D Animation removed - using normal scroll\n\n', content, flags=re.DOTALL)

# Also remove the closing </div> for world-container (before footer or at end of sections)
# Find the pattern: </section>...whitespace...<!--...Footer...-->...whitespace...</div>
content = re.sub(r'(\</section\>.*?\<\!-- End World Container --\>.*?\<\!-- Password Modal --\>)', 
                 r'\1', content, flags=re.DOTALL)

# Simpler: just remove the comment and look for orphan closing div
content = content.replace('<!-- End World Container -->', '')
content = content.replace('</div><!-- End World Container -->', '')

# Write back
with open(r'e:\Library of us\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("3D animation and world-container removed successfully!")

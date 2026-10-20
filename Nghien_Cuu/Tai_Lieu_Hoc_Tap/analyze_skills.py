import os
import yaml
import glob
from collections import defaultdict

SKILL_DIRS = [
    r"C:\Users\Admin\.gemini\config\plugins",
    r"C:\Users\Admin\.gemini\config\skills",
    r"C:\Users\Admin\.gemini\antigravity\builtin\skills"
]

def parse_skill_md(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                if isinstance(frontmatter, dict):
                    name = frontmatter.get("name", os.path.basename(os.path.dirname(file_path)))
                    desc = frontmatter.get("description", "")
                    return name, desc
    except Exception as e:
        pass
    return os.path.basename(os.path.dirname(file_path)), ""

skills = []

for root_dir in SKILL_DIRS:
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "SKILL.md" in filenames:
            skill_file = os.path.join(dirpath, "SKILL.md")
            name, desc = parse_skill_md(skill_file)
            
            # Determine source/plugin
            rel = os.path.relpath(skill_file, r"C:\Users\Admin\.gemini")
            skills.append({
                "name": name,
                "desc": desc,
                "path": skill_file,
                "rel": rel
            })

print(f"Total skills found: {len(skills)}")

# 1. Exact name duplicates
by_name = defaultdict(list)
for s in skills:
    by_name[s["name"].strip().lower()].append(s)

exact_dupes = {k: v for k, v in by_name.items() if len(v) > 1}
print(f"\n=== EXACT NAME DUPLICATES ({len(exact_dupes)} groups) ===")
for k, v in exact_dupes.items():
    print(f"\n[Skill Name: '{k}'] ({len(v)} occurrences):")
    for item in v:
        print(f"  - Path: {item['rel']}")

# 2. Semantic Clustering / Topic Overlaps
# Define thematic keywords to cluster overlapping skills
DOMAINS = {
    "Web Scraping / Crawling": ["scrape", "crawling", "crawler", "crawl4ai", "scrapling", "firecrawl"],
    "PR / Code Review": ["review pr", "code review", "pull request", "bmad-os-review-pr", "code-review-skill", "qa"],
    "UI / Web Design / Frontend": ["ui-ux", "taste-frontend", "minimalist-ui", "industrial-brutalist", "design-taste", "high-end-visual", "web-design", "redesign-existing"],
    "BigQuery / SQL / Data Cleaning": ["bigquery", "sql", "data-autocleaning", "dataform", "dbt", "enforcing-resource-attribution"],
    "Social Media / Post Writing / Video": ["post-writer", "linkedin", "reels-scripting", "carousel", "quote-post", "youtube-thumbnail", "content-matrix", "profile-optimizer"],
    "Academic Writing / Paper Search": ["scientific-writing", "scientific-brainstorming", "literature-review", "paper-search", "arxiv", "europepmc", "citation", "scholar"],
    "Genomics / Bioinformatics (Bulk & Single Cell)": ["anndata", "scanpy", "scvi", "scvelo", "pysam", "polars-bio", "tiledbvcf", "geniml", "gtars", "deeptools"],
    "Cheminformatics / Drug Discovery": ["chembl", "pubchem", "rdkit", "datamol", "diffdock", "molfeat", "medchem", "pytdc", "torchdrug", "opentargets"],
    "Office Documents (Word, Excel, PPT)": ["docx", "xlsx", "pptx", "gdocs", "gsheets", "gslides", "pdf", "latex-posters", "pptx-posters"],
    "Flutter / Mobile": ["flutter", "dart"]
}

print("\n=== SEMANTIC & FUNCTIONAL OVERLAPS ===")
for domain, kws in DOMAINS.items():
    matched = []
    for s in skills:
        text = (s["name"] + " " + s["desc"]).lower()
        if any(kw in text for kw in kws):
            matched.append(s)
    if len(matched) > 1:
        print(f"\n--- Group: {domain} ({len(matched)} skills) ---")
        for m in matched:
            short_desc = (m['desc'][:80] + '...') if len(m['desc']) > 80 else m['desc']
            print(f"  * {m['name']} [{m['rel'].split(os.sep)[1] if os.sep in m['rel'] else m['rel']}] : {short_desc.strip()}")

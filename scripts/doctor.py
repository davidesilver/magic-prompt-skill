#!/usr/bin/env python3
"""
Doctor & Dependency Installer for magic-prompt-skill.
Checks all required skills and optimization engines across Claude Code, Codex, Antigravity, and OneDrive.
Supports --fix to automatically install or symlink missing skills.
"""

import os
import sys
import argparse
import subprocess
import shutil

REQUIRED_SKILLS = {
    # Core process & superpowers
    "brainstorming": "Superpowers native brainstorming module",
    "writing-plans": "Superpowers native planning module",
    "systematic-debugging": "Superpowers native debugging module",
    "using-superpowers": "Superpowers rule enforcement",
    
    # Discovery & Grilling
    "find-skills": "Context and available skill discovery",
    "ponytail": "Repository and context analyzer",
    "wayfinder": "Goal mapping, decision tickets, and frontier tracking",
    "grill-me": "Relentless interactive design interview",
    
    # Validation Councils
    "llm-council": "Karpathy-style 5-advisor low-cost architecture validation",
    "roast-room": "Founder board debate for commercial/product viability",
    
    # Governance & Setup
    "claude-code-setup": "CLAUDE.md and project governance scaffolding",
    
    # Execution & QA
    "implement": "Engineering build workflow",
    "gstack": "Full-stack quality and integration verification",
    "claudex-loop": "Independent cross-family plan review and build inspection"
}

ECOSYSTEM_PATHS = [
    os.path.expanduser("~/.agents/skills"),
    os.path.expanduser("~/.claude/skills"),
    os.path.expanduser("~/.codex/skills"),
    os.path.expanduser("~/Library/CloudStorage/OneDrive-Personale/.agents/skills")
]

FALLBACK_SOURCES = [
    os.path.expanduser("~/.openclaw/agents/main/agent/codex-home/.tmp/plugins/plugins/superpowers/skills"),
    os.path.expanduser("~/Backups/vault-git/_struttura/"),
    os.path.expanduser("~/Progetti")
]

def check_skills():
    results = {}
    for skill_name, desc in REQUIRED_SKILLS.items():
        found_in = []
        for base_path in ECOSYSTEM_PATHS:
            skill_dir = os.path.join(base_path, skill_name)
            if os.path.exists(skill_dir) and (os.path.isfile(os.path.join(skill_dir, "SKILL.md")) or os.path.islink(skill_dir)):
                found_in.append(base_path)
        results[skill_name] = {
            "description": desc,
            "found": len(found_in) > 0,
            "locations": found_in
        }
    return results

def check_layer0():
    aso_path = os.path.expanduser("~/Backups/vault-git/_struttura/agent-stack-optimizer")
    aso_installed = os.path.exists(aso_path) or os.path.exists(os.path.expanduser("~/Progetti/agent-stack-optimizer"))
    return {
        "agent-stack-optimizer": aso_installed
    }

def check_optional_tools():
    wt_path = shutil.which("wt")
    return {
        "worktrunk (wt)": {
            "installed": wt_path is not None,
            "path": wt_path,
            "description": "High-concurrency Git worktree isolation & lifecycle hooks (optional accelerator)",
            "install_hint": "brew install max-sixty/worktrunk/wt or cargo install worktrunk"
        }
    }

def auto_fix(missing_skills):
    print("\n[+] Attempting auto-fix for missing skills...")
    fixed_count = 0
    for skill in missing_skills:
        found_src = None
        for src_dir in FALLBACK_SOURCES:
            candidate = os.path.join(src_dir, skill)
            if os.path.exists(candidate) and (os.path.isfile(os.path.join(candidate, "SKILL.md")) or os.path.isdir(candidate)):
                found_src = candidate
                break
        
        # Also check other ecosystem paths if one has it
        if not found_src:
            for eco_path in ECOSYSTEM_PATHS:
                candidate = os.path.join(eco_path, skill)
                if os.path.exists(candidate):
                    found_src = candidate
                    break

        if found_src:
            for target_base in ECOSYSTEM_PATHS:
                if os.path.exists(target_base):
                    target_dest = os.path.join(target_base, skill)
                    if not os.path.exists(target_dest):
                        try:
                            if os.path.isdir(found_src) and not os.path.islink(found_src):
                                shutil.copytree(found_src, target_dest)
                            else:
                                os.symlink(found_src, target_dest)
                            print(f"  ✓ Installed {skill} -> {target_dest}")
                            fixed_count += 1
                        except Exception as e:
                            print(f"  ✗ Failed to link {skill} -> {target_dest}: {e}")
        else:
            print(f"  ⚠ Could not find local source for '{skill}'. Recommended to run: python install_skill.py {skill}")
            
    return fixed_count

def main():
    parser = argparse.ArgumentParser(description="Verify and install dependencies for magic-prompt-skill")
    parser.add_argument("--fix", action="store_true", help="Automatically install/symlink missing skills from local sources")
    args = parser.parse_args()

    print("=====================================================")
    print(" 🪄 Magic-Prompt-Skill: Pre-flight Doctor Check")
    print("=====================================================\n")

    skill_status = check_skills()
    missing = [name for name, data in skill_status.items() if not data["found"]]

    for skill_name, data in skill_status.items():
        status_icon = "✓" if data["found"] else "✗"
        status_color = "\033[92m" if data["found"] else "\033[91m"
        reset_color = "\033[0m"
        loc_str = f"({len(data['locations'])}/{len(ECOSYSTEM_PATHS)} locations)" if data["found"] else "MISSING"
        print(f"{status_color}[{status_icon}] {skill_name:<28}{reset_color} {loc_str:<18} - {data['description']}")

    layer0 = check_layer0()
    print("\nLayer 0 Optimization Engines:")
    for tool, installed in layer0.items():
        status_icon = "✓" if installed else "✗"
        print(f"[{status_icon}] {tool:<28} {'Available' if installed else 'Not Found'}")

    optional = check_optional_tools()
    print("\nOptional Execution & Isolation Accelerators:")
    for tool, info in optional.items():
        if info["installed"]:
            status_icon = "✓"
            status_color = "\033[92m"
            print(f"{status_color}[{status_icon}] {tool:<28}\033[0m Detected ({info['path']}) - {info['description']}")
        else:
            print(f"[i] {tool:<28} Optional (Not installed) - {info['description']}")
            print(f"    └─ Recommendation: {info['install_hint']}")

    if missing:
        print(f"\n⚠️  {len(missing)} required skills are missing from your environment.")
        if args.fix:
            auto_fix(missing)
            print("\nRe-checking status...")
            post_check = check_skills()
            still_missing = [n for n, d in post_check.items() if not d["found"]]
            if not still_missing:
                print("🎉 All dependencies successfully installed and verified!")
                sys.exit(0)
            else:
                print(f"Remaining missing skills: {', '.join(still_missing)}")
                sys.exit(1)
        else:
            print("Run with --fix to automatically locate and install them:")
            print("  python3 scripts/doctor.py --fix\n")
            sys.exit(1)
    else:
        print("\n🎉 All required skills and tools are properly installed and ready!")
        sys.exit(0)

if __name__ == "__main__":
    main()

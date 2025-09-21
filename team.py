"""
AIMeetMate: print team.
"""

from dataclasses import dataclass

@dataclass
class Member:
    role: str
    first: str
    last: str

TEAM = [
    Member("Product Manager",  "Maya", "Bilous"),
    Member("Tech Lead",        "Maksym",   "Hubar"),
    Member("Backend Engineer", "Slyusarchuk",  "Anton"),
    Member("UI/UX Designer",   "Vladyslav", "Myhalyov"),
    ]

def print_table():
    headers = ["#", "Role", "First name", "Last name"]
    rows = [[
        str(i+1), m.role, m.first, m.last
    ] for i, m in enumerate(TEAM)]

    widths = [max(len(h), *(len(r[c]) for r in rows)) for c, h in enumerate(headers)]
    def fmt(cells): return " | ".join(c.ljust(widths[i]) for i, c in enumerate(cells))
    sep = "-+-".join("-"*w for w in widths)

    print("\nProject: AIMeetMate")
    print(fmt(headers))
    print(sep)
    for r in rows: print(fmt(r))
    print()

def print_devs_last_names():
    dev_roles = {"Tech Lead", "Backend Engineer", "Frontend Engineer", "Full-stack Engineer"}
    dev_last_names = [m.last for m in TEAM if m.role in dev_roles]
    print("Developers' last names:", ", ".join(dev_last_names) or "n/a")

if __name__ == "__main__":
    print_table()
    print_devs_last_names()

import os
from github import Github

# Konfiguration
REPO_OWNER = 'spikestone'
REPO_NAME = 'test'
BRANCH_NAME = 'Jan Sternberg'  # oder der Name deiner Hauptentwicklungszweig
SCRIPT_NAME = 'test.py'  # der Name deines Skripts

# Anmeldung bei GitHub mit deinem Benutzernamen und einem Access Token oder Passwort
g = Github(os.environ.get(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))

# Finde das Repository und den entsprechenden Branch
repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)
branch = repo.get_branch(BRANCH_NAME)

# Finde die neueste Version des Skripts im Repository
script_file = repo.get_contents(SCRIPT_NAME, ref=branch.commit.sha)

# Lese den Inhalt des Skripts und führe ihn aus
script_content = script_file.decoded_content.decode('utf-8')
exec(script_content)

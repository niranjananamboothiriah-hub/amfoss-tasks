Terminal Voyage Logbook

#Level 1

*OBJECTIVE:Navigate through the repository,find the genuine devil fruit,and recover the hidden flag.

*STEPS FOLLOWED:
Explored the cloned repository using basic linux commands.
Inspected the files and folders that connects with the clues.
Used various file exploration commands to identify the genuine fruit,which is "devil_fruits6.txt",from the decoys.
Used "eat.sh" to try eating the genuine fruit,as mentioned in the level1 text.
The script responded and gave the AWAKENING SIGNATURE.

*COMMANDS USED:
ls
ls -la
pwd
cat
find
grep

*RESULT:Successfully found the genuine Devil fruit and discovered the level1 flag.

*SCREENSHOT:
level1(screenshots/level1.png)

#level 2

Objective:Investigate Whiskey_peak,find the hidden executive transmission code and recover level 2 flag
#Steps followed:
navigated to whiskey_peak folder and investigated the files inside it.
inspected git history to understand the commits and the branches available.
found whiskey_peak_investigation branch,so switched to it.
Set the awakening signature i got after solving level1,AWAKENING_SIGNATURE="ONE_PIECE{GITO_GITO_NO_AWAKENING}.
Located the hidden .baroque_works_cache folder.
Used unlock_vault.sh that generated two logs:
  marine_intercept.log
  bounty_hunter_feed.log
Compared the two logs using diff command and as a result i got the level2 hidden transmission:BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}.

This level taught me how Git branches and Git history can contain important information that is not visible in the current working tree. I also learned how to inspect hidden directories, use environment variables, execute shell scripts, and compare files using diff to identify hidden information.

#commands used:



1. Navigate to the repository:
   cd ~/Terminal-Voyage-User-Edition

2. Check the Git status:
   git status

3. View the complete Git history:
   git log --all --oneline --graph --decorate

4. Inspect the Level 2 investigation commit:
   git show --stat bc5aff3

5. List the files stored in that commit:
   git ls-tree -r --name-only bc5aff3

6. View all available branches:
   git branch -a

7. Switch to the Level 2 investigation branch:
   git switch -c whiskey_peak_investigation origin/whiskey_peak_investigation

8. Set the required awakening signature:
   export AWAKENING_SIGNATURE="ONE_PIECE{GITO_GITO_NO_AWAKENING}"

9. List files, including hidden files:
   ls -la

10. Enter the hidden Baroque Works cache:
    cd .baroque_works_cache

11. List the files inside the hidden directory:
    ls -la

12. Run the vault unlocking script:
    ./unlock_vault.sh

13. Compare the two generated log files:
    diff marine_intercept.log bounty_hunter_feed.log
    
#level3

Objective:Find the genuine report containing the first Poneglyph cipher fragment.

steps:

Read the Level 3 instructions and identified the Security Tag.
Searched the repository for the tag using grep.
Located the relevant agent_manifest.log file.
Used cat to read the file and obtained the Poneglyph fragment.

I searched for the Wax_Jungle directory, switched to the little_garden branch where it was available, entered GrandLine/Wax_Jungle, and inspected the reports. I searched for the clue BAROQUE using grep, which led me to:

sector_beta/outpost/watchtower/storage/archive/agent_manifest.log

I then used cat to read the file and found the first Poneglyph fragment.

Cipher Fragment:
KjY2MjF4bw0lKzYqNyBsIS0vbTAtJTcnL

Commands used:

cd Terminal-Voyage-User-Edition
cd GrandLine
ls
ls -la
find . -type d -name "Wax_Jungle"
cd ..
find . -type d -name "Wax_Jungle"
git branch -a
git switch -c little_garden origin/little_garden
git branch
cd GrandLine
cd Wax_Jungle
ls
head report_001.log
head report_002.log
grep -R "BAROQUE"
cat sector_beta/outpost/watchtower/storage/archive/agent_manifest.log



## Level 4 — Blueprint Recovery

### Objective
Recover the hidden blueprint files from Git history, extract the archive, locate the secret link, and use the recovered Poneglyph fragment to proceed.

## STEPS:
* I searched the Git history for the Poneglyph-related information using:


git log --all -S'PONEGLYPH_FRAGMENT_II' --oneline -- GrandLine.

* I located the required historical commit and recovered the compressed blueprint file using:
git show aa616cacc1e0608f1b80627261a34ef02dd08f73:GrandLine/Water_7/galley_locompany/puffing_tom_blueprints | gzip -d > /tmp/step2.tar.

* I created a temporary directory and extracted the archive:
mkdir -p /tmp/level4
tar -xf /tmp/step2.tar -C /tmp/level4

* I searched the extracted files:
find /tmp/level4 -type f

* I found the blueprint archive and extracted it:
mkdir -p /tmp/level4_extracted
unzip -o /tmp/level4/step1_blueprints.zip -d /tmp/level4_extracted

* The extraction revealed:
/tmp/level4_extracted/blueprints_extracted/secret_link.txt
/tmp/level4_extracted/blueprints_extracted/hull_design/frame_specs.dat

* I read the secret link file:
cat /tmp/level4_extracted/blueprints_extracted/secret_link.txt

It contained:
PONEGLYPH_FRAGMENT_II="SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA="

The second Poneglyph fragment was successfully obtained and used to reveal the next clue.

## Level 5 — Vault Sealed

### Objective
Investigate the Git history, recover the two Poneglyph fragments, combine them, and decode the restored inscription to obtain the final clue.

### Steps Taken

* I inspected the Git history to identify the Level 5 commit:

git log --all --oneline --decorate --graph

The Level 5 commit was:

d4e7bf5 Level 5 : Vault Sealed

* I inspected the files created in the Level 5 commit:
git show d4e7bf53daab989e73febe1ae901427da093820f

This revealed the secure vault and the poneglyph.py decoder.

* I investigated the Git history because the later commits removed several vault files. I used commands such as:
git log --all --oneline
git show --stat

* I recovered the first Poneglyph fragment from Level 3:
KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL

* I recovered the second Poneglyph fragment from Level 4:
SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA=

* I combined the two fragments in the correct order:
KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnLSwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA=

* The Level 5 decoder used Base64 decoding followed by XOR with the key 0x42.
Since the original poneglyph.py had been removed from the current working tree, I recovered it directly from the Level 5 commit:
git show d4e7bf5:GrandLine/Enies_Lobby/.cp9_secure_vault/poneglyph.py > /tmp/poneglyph.py

* I executed the recovered decoder:
python3 /tmp/poneglyph.py
 
* I entered the reconstructed encoded Poneglyph string.
Result

The decoder successfully produced the Level 5 Prize:

https://github.com/rogueone-x/Laugh-Tale-Merge-War

This Prize repository provided the clue needed to proceed to Level 6.

Skills Learned
Investigating Git commit history
Recovering deleted files using git show
Understanding Git branches and historical commits
Extracting and reconstructing encoded data
Base64 decoding
XOR-based decoding
Using Python scripts from historical Git commits
Following clues across multiple levels.

## Level 6 — Reconciling Both Histories

### Objective

The objective was to reconcile two different Git histories and recover the complete inscription by resolving the merge conflicts.

### Steps Taken

* I cloned the repository obtained from Level 5 and checked the available branches:

used:
git branch -a

* The two important branches were:

ancient_history
pirate_king_path

* I switched to the ancient_history branch:
git switch ancient_history

* I merged the pirate_king_path branch:
git merge pirate_king_path

* Git reported conflicts in two files:
treasure/key_part_1.txt
treasure/key_part_2.txt

* I inspected the conflicting contents. The two branches contained complementary parts of the inscription.

The first file contained:

TheGrand
Line

which gave:

TheGrandLine

The second file contained:

Remem
bers

which gave:

Remembers

* I resolved the conflicts by restoring the complete inscription:
TheGrandLine.

TheGrandLine
Remembers

* I staged the resolved files:
git add treasure/key_part_1.txt treasure/key_part_2.txt

* I removed the unwanted temporary backup file:
rm treasure/key_part_1.txt.save

* I completed the merge by creating a merge commit:
git commit -m "Reconcile ancient and pirate histories"

The merge was successfully committed.

* I inspected the final victory.sh script:
cat victory.sh

* I executed the script:
./victory.sh

* The script asked for the Pirate King's password. I entered:
TheGrandLineRemembers

Result:

The password was accepted successfully and the final treasure vault was opened.

Skills Learned:

Git branch management
Switching between branches
Merging branches
Resolving merge conflicts
Recovering information from different Git histories
Staging and committing changes
Understanding how different branches can contain complementary information




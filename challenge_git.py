#Script to automate #100daysofcode challenge pushing to github
import subprocess as sp

sp.run('git add .')
sp.run('git commit -m "Challenge progress update"')
sp.run('git push')

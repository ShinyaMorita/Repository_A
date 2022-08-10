team = ["勇者", "戦士", "魔法使い","盗賊"]


print("<select name='job'>")
for job in team:
    print("<option>" + job + "</option>")
print("</select>")

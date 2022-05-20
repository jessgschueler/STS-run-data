--Order by score, highest to lowest
SELECT *
FROM `deb-01-346001.STS_run_data.april_runs`
ORDER BY score DESC

--Show times where the game was won, in this dataset seven times
SELECT *
FROM `deb-01-346001.STS_run_data.april_runs`
WHERE victory LIKE "True"

--Show times where the game was lost to one of the Act 1 bosses, in this dataset 14 times
SELECT *
FROM `deb-01-346001.STS_run_data.april_runs`
WHERE killed_by IN ('Slime Boss', 'The Guardian', 'Hexaghost') 

--Show times where Pandora's box was chosen as a relic from times where the game was won. This happened once.
SELECT *
FROM (SELECT * FROM `deb-01-346001.STS_run_data.april_runs` WHERE victory LIKE "True")
WHERE relics LIKE "%Pandora's Box%"

--The following set of queries show how how many times each character is chosen in descending order, and how many times the game was won with those characters. Despite being chosen least, the Watcher had the most wins.
SELECT character_chosen, COUNT(character_chosen) AS COUNT
FROM `deb-01-346001.STS_run_data.april_runs`
GROUP BY character_chosen
ORDER BY COUNT(*) DESC

SELECT character_chosen, COUNT(character_chosen) AS COUNT
FROM `deb-01-346001.STS_run_data.april_runs`
WHERE victory LIKE "True"
GROUP BY character_chosen
ORDER BY COUNT(*) DESC

--Shows the longest playtime, 2 hours and 37 minutes
SELECT MAX(playtime)
FROM `deb-01-346001.STS_run_data.april_runs`

--Shows which enemy is defeated by the most, in this dataset Hexaghost.
SELECT killed_by, COUNT(killed_by) AS COUNT
FROM `deb-01-346001.STS_run_data.april_runs`
GROUP BY killed_by
ORDER BY COUNT(*) DESC


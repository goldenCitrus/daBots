leaderboard = {"387424639980142596": 1, "519850436899897346": 1}
print(leaderboard)
if leaderboard.get("387424639980142596") is not None:
            leaderboard["387424639980142596"] += 1
else:
            leaderboard["387424639980142596"] = 1
            
print(leaderboard)
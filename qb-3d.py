import csv

# Global Variables
table = dict()
qbTable = dict()
rbTable = dict()

# Pre-processing
with open('pbp-2016.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[7] == "3":
            play = row
            del play[18]
            del play[17]
            del play[13]
            del play[11]
            if row[0] not in table:
                table[row[0]] = [play]
            else:
                # in table
                valueSet = table[row[0]]
                valueSet.append(play)

# with open('pbp-2016.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         if row[7] == '3':
#             print("")
                # row[43])


    #Get rid of the unnecssary record
table.pop("GameId", None)
    # print(table.get("GameId"))
    # print(len(table))
    # for key in table:
        # print("\n"+str(table.get(key)[0]))
        # print (key, table.get(key))


# 0 GameId
# 1 GameDate
# 2 Quarter
# 3 Minute
# 4 Second
# 5 OffenseTeam
# 6 DefenseTeam
# 7 Down
# 8 ToGo
# 9 YardLine
# 10 SeriesFirstDown
# 11 NextScore
# 12 Description
# 13 TeamWin
# 14 SeasonYear
# 15 Yards
# 16 Formation
# 17 PlayType
# 18 IsRush
# 19 IsPass
# 20 IsIncomplete
# 21 IsTouchdown
# 22 PassType
# 23 IsSack
# 24 IsChallenge
# 25 IsChallengeReversed
# 26 Challenger
# 27 IsMeasurement
# 28 IsInterception
# 29 IsFumble
# 30 IsPenalty
# 31 IsTwoPointConversion
# 32 IsTwoPointConversionSuccessful
# 33 RushDirection
# 34 YardLineFixed
# 35 YardLineDirection
# 36 IsPenaltyAccepted
# 37 PenaltyTeam
# 38 IsNoPlay
# 39 PenaltyType
# 40 PenaltyYards

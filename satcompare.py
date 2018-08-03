import matplotlib.pyplot as plt
import school_scores

years = []
alabama_scores = []
alaska_scores = []

scores = school_scores.get_all()

for i in scores:
  if i["State"]["Code"] == AL:
    alabama_scores.append(i["Total"]["Math"])
    years.append(i["Year"])
  elif i["State"]["Code"] == "AK":
    alaska_scores.append(i["Total"]["Math"])
    

plt.plot(years, alabama_scores)
plt.plot(years, alaska_scores)
plt.legend(['AL', 'AK'], loc = 'upper left')

plt.xlabel("Years")
plt.ylabel("Scores")
plt.title("Math SAT Scores in Alabama and Alaska")

plt.show()

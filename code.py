import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import scipy

df = pd.read_csv("data.csv")
reading_time = df["reading_time"].tolist()
means = []


def sample100_average():
    inte = random.randint(1, len(reading_time)-31)
    test = reading_time[inte:inte+30]
    mean = statistics.mean(test)
    means.append(mean)


for i in range(1, 100):
    sample100_average()

mean_final = statistics.mean(means)
stdev = statistics.stdev(reading_time)
print("final mean is(without sampling) "+str(statistics.mean(reading_time)))
print("final mean is "+str(mean_final))
print("standard deviation "+str(statistics.stdev(reading_time)))

std_first_start, first_std_end = mean_final - stdev, mean_final + stdev
std_second_start, second_std_end = mean_final - (2 * stdev), mean_final + (2 * stdev)
std_third_start, third_std_end = mean_final - (3 * stdev), mean_final + (3 * stdev)

fig = ff.create_distplot([means], ["temp"], show_hist = False)
fig.add_trace(go.Scatter(x= [mean_final, mean_final], y=[0, 0.17], mode = "lines", name="MEAN"))
fig.add_trace(go.Scatter(x= [std_first_start, std_first_start], y=[0, 0.17], mode = "lines", name="first start"))
fig.add_trace(go.Scatter(x= [first_std_end, first_std_end], y=[0, 0.17], mode = "lines", name="first end"))
fig.add_trace(go.Scatter(x= [std_second_start, std_second_start], y=[0, 0.17], mode = "lines", name="second start"))
fig.add_trace(go.Scatter(x= [second_std_end, second_std_end], y=[0, 0.17], mode = "lines", name="second end"))
fig.add_trace(go.Scatter(x= [std_third_start, std_third_start], y=[0, 0.17], mode = "lines", name="third start"))
fig.add_trace(go.Scatter(x= [third_std_end, third_std_end], y=[0, 0.17], mode = "lines", name="third end"))
fig.show()
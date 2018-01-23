#!/usr/bin/env python

import matplotlib.pyplot as plt 




year=[1800, 1850, 1900, 1950,1951,1952, 2100]
pop=[1.0,1.262,1.650, 2.538,2.57,2.62,10.85]

plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
ytick_val=[0,2,4,6,8,10]
ytick_lab =['0','2B','4B','6B','8B','10B']
plt.yticks(ytick_val,ytick_lab)
plt.show()


# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')


# Add grid() call
plt.grid(True) 

# Show the plot
plt.show()
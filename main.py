import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defining Input and Output Descriptors

# Dirt
D_SM = 'Small Dirt'
D_MD = 'Medium Dirt'
D_LG = 'Large Dirt'

# Grease
G_NG = 'No Grease'
G_MD = 'Medium Grease'
G_LG = 'High Grease'

# Wash Time
WS_VS = 'Very Short'
WS_S = 'Short'
WS_M = 'Medium'
WS_L = 'Long'
WS_VL = 'Very Long'

def membership_dirt(x, DESCRIPTOR):
    if DESCRIPTOR == D_SM:
        return max(0, (1 - x/50))
    elif DESCRIPTOR == D_MD:
        return max(0, min(x/50, 2 - x/50))
    elif DESCRIPTOR == D_LG:
        return max(0, x/50 - 1)
        
# Plotting the membership functions
x = np.arange(0, 100, 0.1)

plt.plot(x, [membership_dirt(i, D_SM) for i in x], label=D_SM)
plt.plot(x, [membership_dirt(i, D_MD) for i in x], label=D_MD)
plt.plot(x, [membership_dirt(i, D_LG) for i in x], label=D_LG)
plt.legend()
plt.title('Dirt')
plt.xlabel('Dirt Level (%)')
plt.ylabel('Membership')
plt.show()

# Defining the membership functions for grease
def membership_grease(x, DESCRIPTOR):
    if DESCRIPTOR == G_NG:
        return max(0, (1 - x/50))
    elif DESCRIPTOR == G_MD:
        return max(0, min(x/50, 2 - x/50))
    elif DESCRIPTOR == G_LG:
        return max(0, x/50 - 1)
        
# Plotting the membership functions
x = np.arange(0, 100, 0.1)
plt.plot(x, [membership_grease(i, G_NG) for i in x], label=G_NG)
plt.plot(x, [membership_grease(i, G_MD) for i in x], label=G_MD)
plt.plot(x, [membership_grease(i, G_LG) for i in x], label=G_LG)
plt.legend()
plt.title('Grease')
plt.xlabel('Grease Level (%)')
plt.ylabel('Membership')
plt.show()

def membership_washtime(x, DESCRIPTOR):
    if DESCRIPTOR == WS_VS:
        return max(0, (1 - x/10))
    elif DESCRIPTOR == WS_S:
        return max(0, min(x/10, 25/15 - x/15))
    elif DESCRIPTOR == WS_M:
        return max(0, min((x - 10)/15, (40 - x)/15))
    elif DESCRIPTOR == WS_L:
        return max(0, min((x - 25)/15, (60 - x)/20))
    elif DESCRIPTOR == WS_VL:
        return max(0, (x - 40)/20)
        
# Plotting the membership functions
x = np.arange(0, 60, 0.1)
plt.plot(x, [membership_washtime(i, WS_VS) for i in x], label=WS_VS)
plt.plot(x, [membership_washtime(i, WS_S) for i in x], label=WS_S)
plt.plot(x, [membership_washtime(i, WS_M) for i in x], label=WS_M)
plt.plot(x, [membership_washtime(i, WS_L) for i in x], label=WS_L)
plt.plot(x, [membership_washtime(i, WS_VL) for i in x], label=WS_VL)
plt.legend()
plt.title('Wash Time')
plt.xlabel('Wash Time (min)')
plt.ylabel('Membership')
plt.show()

# Defining the rules
def inference(DIRT, GREASE):
    if DIRT == D_SM and GREASE == G_NG:
        return WS_VS
    elif DIRT == D_SM and GREASE == G_MD:
        return WS_M
    elif DIRT == D_SM and GREASE == G_LG:
        return WS_L
    elif DIRT == D_MD and GREASE == G_NG:
        return WS_S
    elif DIRT == D_MD and GREASE == G_MD:
        return WS_M
    elif DIRT == D_MD and GREASE == G_LG:
        return WS_L
    elif DIRT == D_LG and GREASE == G_NG:
        return WS_M
    elif DIRT == D_LG and GREASE == G_MD:
        return WS_L
    elif DIRT == D_LG and GREASE == G_LG:
        return WS_VL
        
# Assuming the input is: `Dirt = 60%` and `Grease = 70%`
DIRT = 50
GREASE = 70

# Get Membership Values
DIRT_SM = membership_dirt(DIRT, D_SM)
DIRT_MD = membership_dirt(DIRT, D_MD)
DIRT_LG = membership_dirt(DIRT, D_LG)
GREASE_NG = membership_grease(GREASE, G_NG)
GREASE_MD = membership_grease(GREASE, G_MD)
GREASE_LG = membership_grease(GREASE, G_LG)
# Print the membership values
print('DIRT_SM =', DIRT_SM)
print('DIRT_MD =', DIRT_MD)
print('DIRT_LG =', DIRT_LG)
print('GREASE_NG =', GREASE_NG)
print('GREASE_MD =', GREASE_MD)
print('GREASE_LG =', GREASE_LG)

S1 = min(DIRT_MD, GREASE_MD)
S2 = min(DIRT_MD, GREASE_LG)
S3 = min(DIRT_LG, GREASE_MD)
S4 = min(DIRT_LG, GREASE_LG)

# Print the strength of the rules
print('S1 =', S1)
print('S2 =', S2)
print('S3 =', S3)
print('S4 =', S4)

# Since, According to the Rule, we have Time is Medium, we need to calculate the $x$ values for which the membership function of Time when Time is Medium is equal to strength of the rule i.e. 0.6
x = np.arange(0, 60, 0.1)
y = [membership_washtime(i, WS_M) for i in x]

final_x_values = []
for i in range(len(y)):
    if abs(y[i] - S1) < 0.000000000000001:
        final_x_values.append(x[i])

plt.plot(x, y)
plt.axhline(y=S1, color='r', linestyle='-')
plt.title('Wash Time')
plt.xlabel('Wash Time (min)')
plt.ylabel('Membership')
plt.show()

# Print the X values
print('x values =', final_x_values)

ans = sum(final_x_values)/len(final_x_values)
print('Wash Time =', ans, 'min')

from collections import Counter
import random
import sys
# course [name, no_students, instructors]


c1 = ['c1', 25, ['James', 'Mike']]
c2 = ['c2', 35, ['James', 'Mike', 'Steve']]
c3 = ['c3', 25, ['James', 'Mike']]
c4 = ['c4', 30, ['Jane', 'Steve']]
c5 = ['c5', 35, ['Jane']]
c6 = ['c6', 45, ['James', 'Steve']]
c7 = ['c7', 45, ['Jane', 'Mike']]

course = [c1, c2, c3, c4, c5, c6, c7]

# rooms  [id, capacity]
r1 = ['r1', 25]
r2 = ['r2', 45]
r3 = ['r3', 35]

rooms = [r1, r2, r3]

# instructor [id, name]
i1 = ['i1', 'James']
i2 = ['i2', 'Mike']
i3 = ['i3', 'Steve']
i4 = ['i4', 'Jane']

instructor = [i1, i2, i3, i4]

# meetingtime [id, time]
# m1 = ['m1', '9am-10am']
# m2 = ['m2', '10am-11am']
# m3 = ['m3', '11am-12pm']
# m4 = ['m4', '12pm-1pm']

meettime = ['m1', 'm2', 'm3', 'm4']

# departments
math = [c1, c3]
ee = [c2, c4, c5]
phy = [c6, c7]

dept = [math, ee, phy]
data = [dept, instructor, course, rooms, meettime]
days = ['mon', 'tues', 'wed', 'thur', 'fri']


            

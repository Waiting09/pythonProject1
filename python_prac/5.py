#字典
alien_0 = {'color': 'green', 'points': 5}
#现在，你可以访问外星人alien_0的颜色和点数。如果玩家射杀了这个外星人，你就可以使用下面的代码来确定玩家应获得多少个点
print(alien_0['points'])
#在字典alien_0中添加两项信息：外星人的x坐标：0，y坐标：25
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#创建一个空字典，添加两项信息 'color': 'green', 'points': 5
alien_0 ={}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#将外星人从绿色改为黄色
alien_0 = {'color': 'green'}
alien_0['color'] = 'yellow'
print(alien_0)
#向右移动外星人
#据外星人当前速度决定将其移动多远
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': '慢速'}
if alien_0['speed'] == '慢速':
    x = 1
elif alien_0['speed'] == '中速':
    x = 1
else:
    x = 3
alien_0['x_position'] = alien_0['x_position'] + x  # 新位置等于老位置加上增量
print(alien_0['x_position'])
print(alien_0)
#删除键—值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
#遍历所有的键—值对
c = {
    '1': '小米',
    '2': '女',
    '3': '3',
    '4': '3',

    }
for k, v in c.items():
    print("\nKey: " + k)
    print("Value: " + v)
#遍历字典中的所有键keys()
for k in c.keys():
    print(k)
for k in c:
    print(k)
#按顺序遍历字典中的所有键
for name in sorted(c.keys()):
    print(name)
#遍历字典中的所有值 方法values()
for value in c.values():
    print(value)
#剔除重复项，可使用集合set
for value in set(c.values()):
    print(value)
#字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
for i in range(len(aliens)):
    print(i)
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(len(aliens))
#在字典中存储列表
like = {'name': '小白','color': ['yellow','red']}
for i in like['color']:
    print('\t'+i)

#在字典中存储字典
c = {
    '1': {
        'name': '小白',
        'color':'yellow',
        },
    '2': {
        'name': '小黑',
        'color':'red',
        },
    }
for a,b in c.items():
    print(b['name'])
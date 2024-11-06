import networkx as nx  
import matplotlib.pyplot as plt
# 假设我们已经有节点和边的数据  
nodes = [ ["Yanyan-Wang",50.95],["Aarebecca",23.82],["pomelo-nwu",22.36],["tyn1998",16.64],["frank-zsy",15.8],["will-ww",13.5],["zhicheng-ning",8.35],["xgdyp",7.58],["stevending1st",6.28],["andyhuang18",6.27],["Zzzzzhuzhiwei",6.21],["wxharry",4.79],["bifenglin",4.01],["yangzy0603",3.83],["lidongze0629",3.73],["wj23027",3.56],["PureNatural",3.37],["kunal8411",3.36],["birdflyi",3.28],["lhbvvvvv",3.12],["xiaoya-yaya",2.39],["stealth-bombeer",2.36],["yikenie",2.31],["RackweLLizm",2.28],["pranavshuklaa",1.79],["Vlad116",1.79],["Maple0817",1.63],["yvonneyx",1.22],["yubo0923",1.12],["zhaosj975",1],["longyanz",0.74]]
edges = [["Yanyan-Wang","Aarebecca",25.3],["Yanyan-Wang","pomelo-nwu",25.09],["Aarebecca","pomelo-nwu",24.84],["andyhuang18","tyn1998",15.28],["yangzy0603","pomelo-nwu",13.85],["bifenglin","will-ww",13.32],["tyn1998","pomelo-nwu",12.48],["yangzy0603","Aarebecca",11.92],["tyn1998","frank-zsy",11.87],["yangzy0603","Yanyan-Wang",11.85],["wj23027","andyhuang18",11.03],["zhicheng-ning","will-ww",10.82],["wj23027","tyn1998",10.64],["tyn1998","bifenglin",9.84],["tyn1998","Yanyan-Wang",9.62],["Zzzzzhuzhiwei","frank-zsy",9.52],["tyn1998","will-ww",9.15],["Zzzzzhuzhiwei","will-ww",8.83],["xgdyp","frank-zsy",8.44],["andyhuang18","will-ww",8.19],["lidongze0629","pomelo-nwu",8.1],["Zzzzzhuzhiwei","tyn1998",7.93],["andyhuang18","zhicheng-ning",7.88],["lhbvvvvv","tyn1998",7.84],["PureNatural","bifenglin",7.75],["zhicheng-ning","tyn1998",7.73],["yvonneyx","Aarebecca",7.73],["Zzzzzhuzhiwei","xgdyp",7.71],["xgdyp","PureNatural",7.67],["yvonneyx","pomelo-nwu",7.63],["will-ww","frank-zsy",7.62],["xgdyp","bifenglin",7.61],["xiaoya-yaya","bifenglin",7.42],["yvonneyx","Yanyan-Wang",7.39],["Zzzzzhuzhiwei","lhbvvvvv",7.37],["tyn1998","PureNatural",7.32],["PureNatural","frank-zsy",7.29],["Yanyan-Wang","lidongze0629",7.25],["yangzy0603","tyn1998",7.15],["wj23027","zhicheng-ning",7.1],["lhbvvvvv","andyhuang18",7.07],["PureNatural","will-ww",7.06],["birdflyi","xgdyp",6.99],["xgdyp","tyn1998",6.96],["lhbvvvvv","will-ww",6.92],["tyn1998","stevending1st",6.85],["stevending1st","frank-zsy",6.84],["birdflyi","frank-zsy",6.71],["Aarebecca","lidongze0629",6.58],["wxharry","tyn1998",6.54],["Zzzzzhuzhiwei","PureNatural",6.49],["bifenglin","frank-zsy",6.4],["tyn1998","Aarebecca",6.4],["zhicheng-ning","bifenglin",6.34],["andyhuang18","frank-zsy",6.29],["wj23027","will-ww",6.26],["Zzzzzhuzhiwei","birdflyi",6.22],["xiaoya-yaya","will-ww",6.19],["xgdyp","will-ww",6.14],["Zzzzzhuzhiwei","zhicheng-ning",6.11],["birdflyi","bifenglin",6.04],["birdflyi","PureNatural",6.01],["lhbvvvvv","frank-zsy",5.92],["yangzy0603","yvonneyx",5.84],["Zzzzzhuzhiwei","bifenglin",5.79],["yangzy0603","lidongze0629",5.6],["andyhuang18","bifenglin",5.59],["andyhuang18","wxharry",5.53],["wj23027","frank-zsy",5.48],["zhicheng-ning","frank-zsy",5.33],["Zzzzzhuzhiwei","andyhuang18",5.31],["birdflyi","tyn1998",5.19],["xiaoya-yaya","tyn1998",5.09],["birdflyi","will-ww",4.97],["lhbvvvvv","zhicheng-ning",4.97],["RackweLLizm","pomelo-nwu",4.97],["Zzzzzhuzhiwei","stevending1st",4.96],["RackweLLizm","Aarebecca",4.84],["xiaoya-yaya","xgdyp",4.75],["yikenie","pomelo-nwu",4.66],["zhicheng-ning","PureNatural",4.63],["yikenie","Aarebecca",4.55],["Zzzzzhuzhiwei","wj23027",4.53],["RackweLLizm","Yanyan-Wang",4.5],["lhbvvvvv","wj23027",4.43],["yangzy0603","RackweLLizm",4.29],["andyhuang18","stevending1st",4.28],["yikenie","Yanyan-Wang",4.25],["zhicheng-ning","xgdyp",4.23],["pranavshuklaa","tyn1998",4.19],["xiaoya-yaya","PureNatural",4.15],["xiaoya-yaya","zhicheng-ning",4.11],["bifenglin","pomelo-nwu",4.11],["tyn1998","lidongze0629",4.1],["lhbvvvvv","wxharry",4.08],["yangzy0603","yikenie",4.06],["longyanz","bifenglin",3.97],["pomelo-nwu","frank-zsy",3.96],["pranavshuklaa","wxharry",3.95],["yvonneyx","lidongze0629",3.93],["xgdyp","stevending1st",3.91],["yubo0923","pomelo-nwu",3.9],["yvonneyx","tyn1998",3.87],["wj23027","pomelo-nwu",3.86],["andyhuang18","PureNatural",3.83],["yubo0923","Aarebecca",3.82],["pranavshuklaa","andyhuang18",3.75],["longyanz","will-ww",3.69],["Zzzzzhuzhiwei","xiaoya-yaya",3.69],["lhbvvvvv","PureNatural",3.66],["wj23027","bifenglin",3.62],["yubo0923","Yanyan-Wang",3.61],["andyhuang18","pomelo-nwu",3.56],["lhbvvvvv","bifenglin",3.55],["lhbvvvvv","stevending1st",3.54],["stevending1st","will-ww",3.51],["stealth-bombeer","tyn1998",3.51],["birdflyi","stevending1st",3.48],["yangzy0603","yubo0923",3.47],["RackweLLizm","lidongze0629",3.4],["wj23027","stevending1st",3.37],["PureNatural","stevending1st",3.36],["stealth-bombeer","wxharry",3.35],["RackweLLizm","tyn1998",3.35],["xiaoya-yaya","birdflyi",3.33],["Maple0817","pomelo-nwu",3.32],["will-ww","pomelo-nwu",3.27],["Maple0817","Aarebecca",3.27],["yikenie","lidongze0629",3.26],["yvonneyx","RackweLLizm",3.24],["lhbvvvvv","xgdyp",3.23],["yikenie","tyn1998",3.21],["stealth-bombeer","andyhuang18",3.2],["Yanyan-Wang","Maple0817",3.11],["yvonneyx","yikenie",3.11],["zhicheng-ning","stevending1st",3.07],["tyn1998","Vlad116",3.05],["pranavshuklaa","lhbvvvvv",3.02],["birdflyi","zhicheng-ning",3.01],["yangzy0603","Maple0817",3.01],["longyanz","tyn1998",2.96],["longyanz","xiaoya-yaya",2.94],["wxharry","Vlad116",2.93],["yubo0923","lidongze0629",2.86],["xiaoya-yaya","frank-zsy",2.84],["zhaosj975","tyn1998",2.84],["yubo0923","tyn1998",2.83],["andyhuang18","Vlad116",2.81],["kunal8411","andyhuang18",2.78],["lhbvvvvv","birdflyi",2.78],["RackweLLizm","yikenie",2.77],["yubo0923","yvonneyx",2.75],["kunal8411","wj23027",2.74],["longyanz","zhicheng-ning",2.72],["stevending1st","bifenglin",2.71],["lhbvvvvv","stealth-bombeer",2.66],["pranavshuklaa","stealth-bombeer",2.6],["Maple0817","lidongze0629",2.54],["zhicheng-ning","pomelo-nwu",2.52],["tyn1998","Maple0817",2.51],["yubo0923","RackweLLizm",2.48],["andyhuang18","xgdyp",2.47],["yvonneyx","Maple0817",2.45],["yubo0923","yikenie",2.4],["lhbvvvvv","Vlad116",2.38],["PureNatural","pomelo-nwu",2.36],["wj23027","Yanyan-Wang",2.34],["longyanz","xgdyp",2.34],["pranavshuklaa","Vlad116",2.34],["longyanz","andyhuang18",2.33],["kunal8411","tyn1998",2.32],["xiaoya-yaya","andyhuang18",2.28],["longyanz","PureNatural",2.26],["xiaoya-yaya","pomelo-nwu",2.24],["RackweLLizm","Maple0817",2.23],["Zzzzzhuzhiwei","wxharry",2.22],["wj23027","PureNatural",2.21],["yikenie","Maple0817",2.17],["stealth-bombeer","Vlad116",2.11],["xgdyp","pomelo-nwu",2.1],["longyanz","pomelo-nwu",2.1],["Yanyan-Wang","frank-zsy",2.1],["wxharry","stevending1st",2.03],["kunal8411","zhicheng-ning",2.02],["yubo0923","Maple0817",1.99],["lhbvvvvv","xiaoya-yaya",1.98],["wj23027","xgdyp",1.87],["Zzzzzhuzhiwei","pranavshuklaa",1.87],["wj23027","xiaoya-yaya",1.85],["longyanz","wj23027",1.83],["yangzy0603","frank-zsy",1.77],["pranavshuklaa","stevending1st",1.73],["Zzzzzhuzhiwei","stealth-bombeer",1.72],["wj23027","wxharry",1.71],["kunal8411","stevending1st",1.69],["xiaoya-yaya","stevending1st",1.69],["zhaosj975","will-ww",1.65],["Zzzzzhuzhiwei","Vlad116",1.6],["stealth-bombeer","stevending1st",1.6],["Zzzzzhuzhiwei","longyanz",1.59],["zhaosj975","andyhuang18",1.56],["zhaosj975","bifenglin",1.54],["andyhuang18","birdflyi",1.51],["wxharry","frank-zsy",1.51],["Zzzzzhuzhiwei","pomelo-nwu",1.5],["Vlad116","stevending1st",1.5],["pranavshuklaa","wj23027",1.49],["zhaosj975","PureNatural",1.43],["stealth-bombeer","wj23027",1.4],["longyanz","birdflyi",1.36],["pranavshuklaa","frank-zsy",1.34],["birdflyi","pomelo-nwu",1.33],["wj23027","Vlad116",1.32],["yangzy0603","wj23027",1.31],["zhaosj975","zhicheng-ning",1.26],["stealth-bombeer","frank-zsy",1.26],["wj23027","birdflyi",1.25],["kunal8411","frank-zsy",1.2],["Vlad116","frank-zsy",1.2],["andyhuang18","Yanyan-Wang",1.14],["lhbvvvvv","pomelo-nwu",1.09],["zhaosj975","frank-zsy",1.09],["lhbvvvvv","zhaosj975",1.09],["zhaosj975","pomelo-nwu",1],["zhaosj975","wj23027",1],["Aarebecca","frank-zsy",0.97],["zhaosj975","xgdyp",0.93],["lhbvvvvv","longyanz",0.89],["lidongze0629","frank-zsy",0.89],["longyanz","frank-zsy",0.89],["yvonneyx","frank-zsy",0.88],["Yanyan-Wang","bifenglin",0.86],["RackweLLizm","frank-zsy",0.85],["yikenie","frank-zsy",0.84],["yangzy0603","andyhuang18",0.83],["longyanz","zhaosj975",0.83],["yubo0923","frank-zsy",0.81],["kunal8411","will-ww",0.79],["Maple0817","frank-zsy",0.78],["yangzy0603","bifenglin",0.67],["zhaosj975","birdflyi",0.67],["zhaosj975","xiaoya-yaya",0.67],["Zzzzzhuzhiwei","zhaosj975",0.67]]  # 示例数据，需要完整数据  
  
# 创建图对象  
G = nx.Graph()  
  
# 添加节点及其影响力分数（作为节点属性）  
for node in nodes:  
    G.add_node(node[0], influence_score=node[1])   
# 添加边及其权重  
for edge in edges:  
    G.add_edge(edge[0], edge[1], weight=edge[2])
# 创建一个字典来存储每个用户的直接朋友  
direct_friends = {node: list(G.neighbors(node)) for node in G.nodes()}  

# 计算度数并找出度数最多的前5个用户  
degree_dict = dict(G.degree())  
sorted_degree = sorted(degree_dict.items(), key=lambda item: item[1], reverse=True)  
top_5_degree_users = sorted_degree[:5]  
  
print("度数最多的前5个用户及其朋友数量:")  
for user, degree in top_5_degree_users:  
    print(f"{user}: {degree}")

#找出影响力最高的五个用户
sorted_influence = sorted(nodes, key=lambda node: node[1], reverse=True)#key=lambda node:node[1]以第二个数为基准排序， reverse=True降序排序
top_5_influence_users = [node[0] for node in sorted_influence[:5]] 
print("影响力最高的5个用户:")
for user in top_5_influence_users:
    print(user)

#列出最有影响力的用户 50%度数+50%影响力  
combined_scores = {node: 0.5 * G.nodes[node]['influence_score'] + 0.5 * degree_dict[node] for node in G.nodes()}  
sorted_combined = sorted(combined_scores.items(), key=lambda item: item[1], reverse=True)  
top_combined_scores = sorted_combined[0]
print("对社交网络最有影响力的用户：")
print(top_combined_scores)

# 对于Yanyan-Wang，找出其“朋友的朋友”中最有可能成为新朋友的用户（有最多共同的朋友）  
yanyan_friends = set(G.neighbors("Yanyan-Wang"))  
potential_friends = {}  
  
for friend in yanyan_friends:  
    common_friends = len(set(G.neighbors(friend)) & yanyan_friends)  # 计算共同朋友数量（但这里应该排除friend自己，所以实际上应该使用差集）  
    # 更准确的做法是使用二阶邻居，但这里为了简化，我们仅考虑直接朋友的共同朋友  
    # 注意：这种方法可能不准确，因为它没有考虑到通过其他路径连接的“朋友的朋友”  
    potential_friends[friend] = common_friends + G[friend]["Yanyan-Wang"]["weight"] if G.has_edge("Yanyan-Wang", friend) else common_friends  # 这里加上了边权重作为额外考虑（如果已经是朋友，则加上权重）  
  
# 找出有最多共同朋友的用户（这里我们仅考虑共同朋友数量，不考虑边权重作为排序的唯一标准）  
# 如果要考虑边权重，可以调整排序的key  
sorted_potential_friends = sorted(potential_friends.items(), key=lambda item: item[1], reverse=True)  
  
print("推荐给Yanyan-Wang的新朋友(按共同朋友数量排序):")  
for friend, common_count in sorted_potential_friends:  
    print(f"{friend}: {common_count}个共同朋友")
    # 找出与Yanyan-Wang连接强度最高的5个用户（无论是否已经是直接朋友）  
# 注意：这里我们考虑的是所有到达Yanyan-Wang的路径上的边权重之和（但为简化，我们只考虑直接连接）  
yanyan_connections = [(node, G[node]["Yanyan-Wang"]["weight"]) if G.has_edge("Yanyan-Wang", node) else (node, 0) for node in G.nodes()]  
# 对于不是直接朋友的节点，我们需要找到通过其他路径到达Yanyan-Wang的权重之和，但这通常涉及更复杂的图算法（如Dijkstra或Bellman-Ford）  
# 这里为了简化，我们只考虑直接连接  
  
# 排序并打印结果（仅考虑直接连接）  
sorted_yanyan_connections = sorted(yanyan_connections, key=lambda item: item[1], reverse=True)  
print("与Yanyan-Wang连接强度最高的5个用户(仅考虑直接连接):")  
for node, weight in sorted_yanyan_connections[:5]:  
    print(f"{node}: 权重为{weight}")

# 绘制网络图  
pos = nx.spring_layout(G)  # 使用spring布局算法  
nx.draw(G, pos, with_labels=True, node_size=[G.nodes[node]['influence_score'] * 10 for node in G.nodes()], node_color=[G.nodes[node]['influence_score'] for node in G.nodes()], cmap=plt.cm.Reds)  

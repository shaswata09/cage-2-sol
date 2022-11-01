from CybORG import CybORG
import inspect
from pprint import pprint

path = str(inspect.getfile(CybORG))
path = path[:-10] + '/Shared/Scenarios/Scenario2.yaml'

env = CybORG(path, 'sim')

results = env.reset(agent='Red')
obs = results.observation

pprint(obs)

action_space = results.action_space

print(list(action_space.keys()))

print(action_space['subnet'])

from CybORG.Agents import B_lineAgent

agent = B_lineAgent()

action = agent.get_action(obs,action_space)
# print(action)

results = env.step(agent='Red',action=action)
pprint(results)

pprint(results.observation)
print(76*'-')
print(results.action)
print(76*'-')
print(results.done)

from CybORG.Agents import B_lineAgent, GreenAgent, BlueMonitorAgent

agents = {
    'Red': B_lineAgent,
    'Green': GreenAgent
}

env = CybORG(path,'sim',agents=agents)

results = env.reset(agent='Blue')
obs = results.observation
action_space = results.action_space
agent = BlueMonitorAgent()

for step in range(20):
    action = agent.get_action(obs,action_space=action_space)
    results = env.step(agent='Blue',action=action)
    obs = results.observation
    reward = results.reward
    print(action, reward, sep=" :: ")


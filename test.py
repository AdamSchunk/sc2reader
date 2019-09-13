import sc2reader as reader
import os

replay_dir = 'test_replays/engagemetnts'
replays = reader.load_replays(os.path.join(replay_dir))
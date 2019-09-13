import sc2reader as reader
import os

replay_dir = 'test_replays/engagements'
replay = reader.load_replay(os.path.join(replay_dir,"test.SC2Replay"))


event_names = set([event.name for event in replay.events])
events_of_type = {name: [] for name in event_names}
for event in replay.events:
    events_of_type[event.name].append(event)

unit_born_events = events_of_type["UnitBornEvent"]
for ube in unit_born_events:
    print("Player {} created {}".format(ube.control_pid,
        ube.unit_type_name))


unit_died_events = events_of_type["UnitDiedEvent"]
for udiede in unit_died_events:
        print("Unit id {} was killed by player {} using {}".format(udiede.unit_id_index,
            udiede.killing_player_id, udiede.killing_unit_index))



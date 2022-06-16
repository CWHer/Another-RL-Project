from collections import namedtuple

AGENT_CONFIG = {
    "checkpoint_dir": "checkpoint",

    "action_size": 4,
    "gamma": 0.98,

    # features
    # "n_periods": 4,

    # AGENT architecture
    "in_channels": 5,
    "n_res": 5,
    "n_channels": 64,

    # optimizer
    "learning_rate": 0.001,
    "l2_weight": 1e-4,

    # soft update
    "tau": 0.1,

    # epsilon-greedy
    "init_epsilon": 0.5,
    "min_epsilon": 0.1,
    "delta_epsilon": 0.01
}

DATA_CONFIG = {
    "dataset_dir": "dataset",
    "save_freq": 200,
    "replay_size": 20000,

    # sample
    "train_thr": 50,
    "batch_size": 32,
}

TRAIN_CONFIG = {
    "parameters_dir": "parameters",
    "log_dir": "logs/",

    # total
    "epochs": 500,

    # explore the environment
    "n_game": 1,

    # update the model
    "train_epochs": 2,

    # evaluate
    # NOTE: current_reward >= best_reward * update_thr
    "update_thr": 1.02,
}


def saveSettings():
    import json
    import os
    from datetime import datetime

    para_dir = TRAIN_CONFIG["parameters_dir"]
    if not os.path.exists(para_dir):
        os.mkdir(para_dir)

    timestamp = datetime.now().strftime("%m-%d_%H-%M-%S")
    TRAIN_CONFIG["log_dir"] += timestamp
    file_path = para_dir + f"/para_{timestamp}.json"
    with open(file_path, "w") as f:
        json.dump(
            {"AGENT_CONFIG": AGENT_CONFIG,
             "DATA_CONFIG": DATA_CONFIG,
             "TRAIN_CONFIG": TRAIN_CONFIG},
            f, indent=4)


saveSettings()


AGENT_CONFIG_TYPE = namedtuple("AGENT_CONFIG", AGENT_CONFIG.keys())
AGENT_CONFIG = AGENT_CONFIG_TYPE._make(AGENT_CONFIG.values())

DATA_CONFIG_TYPE = namedtuple("DATA_CONFIG", DATA_CONFIG.keys())
DATA_CONFIG = DATA_CONFIG_TYPE._make(DATA_CONFIG.values())

TRAIN_CONFIG_TYPE = namedtuple("TRAIN_CONFIG", TRAIN_CONFIG.keys())
TRAIN_CONFIG = TRAIN_CONFIG_TYPE._make(TRAIN_CONFIG.values())

# DRL_Taxi_Custom

A deep reinforcement learning project on a customized environment from OpenAi's Gymnasium.

## Installation

The customized environment has to be built from source. To do so, run

```bash
python setup.py build install
```

After installation, you'll see a new folder named `gym_taxi_custom.egg-info` in the current directory.

To install dependencies, run

```bash
pip install -r requirements.txt
```

## Usage

To see how the model trains, you can follow the instructions on this [site](https://dibranmulder.github.io/2019/09/06/Running-an-OpenAI-Gym-on-Windows-with-WSL/) to learn how to run the environment on Windows.

After installation, you can run the model by running

```bash
python app.py
```

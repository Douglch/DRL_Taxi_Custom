from gym.envs.registration import register

register(
    id="gym_taxi_custom/Taxi-v0",
    entry_point="gym_taxi_custom.envs:CustomTaxiEnv",
)

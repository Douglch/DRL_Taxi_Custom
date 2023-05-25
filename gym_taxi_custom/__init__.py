from gym.envs.registration import register

register(
    id="gym_taxi_custom/taxi-V0",
    entry_point="gym_taxi_custom.envs.toy_text:CustomTaxiEnv",
)

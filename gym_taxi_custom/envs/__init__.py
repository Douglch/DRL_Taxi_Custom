from gym.envs.registration import register

register(
    id="gym_taxi_custom/taxi_custom",
    entry_point="gym_taxi_custom.envs.toy_text:taxi_custom",
)

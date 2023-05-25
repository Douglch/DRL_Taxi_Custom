from gym.envs.registration import register

register(
    id="gym-taxi-custom/taxi-custom",
    entry_point="gym-taxi-custom.envs.toy_text:taxi-custom",
)

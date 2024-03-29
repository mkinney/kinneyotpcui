# About

Character user interface for the kinneyotp (one time pad) module.

# Screens
![encode tab](https://github.com/mkinney/kinneyotpcui/blob/main/screens/encode.png?raw=true "Encode")
![decode tab](https://github.com/mkinney/kinneyotpcui/blob/main/screens/decode.png?raw=true "Decode")
![generate tab](https://github.com/mkinney/kinneyotpcui/blob/main/screens/generate.png?raw=true "Generate")
![settings tab](https://github.com/mkinney/kinneyotpcui/blob/main/screens/settings.png?raw=true "Settings")
![about tab](https://github.com/mkinney/kinneyotpcui/blob/main/screens/about.png?raw=true "About")


# To install locally

```
python3 -m venv venv
act
pip install --upgrade pip
pip install textual kinneyotp

python otp
```

# To install using docker

```
docker run -it mkinney/kinneyotpcui
```


# Tips
- How to select text to copy:
  * iTerm Hold the OPTION key.
  * Gnome Terminal Hold the SHIFT key.
  * Windows Terminal Hold the SHIFT key.

# For development
For development, need to install a few more things:

```
pip install pytest pytest-asyncio
```

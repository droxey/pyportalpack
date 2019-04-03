# 🐍 PyPortal Starter Pack

Clone this starter pack and dive into coding on the excellent Adafruit PyPortal!

## How to Use This Repository

1. **Connect your `PyPortal` device via USB**. Be sure to use a good quality USB cable!

2. **In a blank `/Volumes/CIRCUITPY` directory, clone this repository to the root of `/Volumes/CIRCUITPY`**. Make sure to remove the `.git` directory:

    ```bash
    cd /Volumes/CIRCUITPY
    git clone git@github.com:droxey/pyportalpack.git . && rm -rf .git
    ```

3. Initialize your own Git repository in the directory:

    ```bash
    git init
    ```

4. Create a checkpoint by adding and committing the starter code:

    ```bash
    git add .
    git commit -m "[add] initial starter pack"
    ```

5. Create a file named **`secrets.py`** that contains the following code:

    ```python
    secrets = {
      'ssid': 'CHANGE ME',             # Keep the two '' quotes around the name
      'password': 'CHANGE ME',         # Keep the two '' quotes around password
      'timezone': "America/Los_Angeles",  # http://worldtimeapi.org/timezones
      'aio_username': 'YOUR_ADAFRUIT_ACCOUNT_USERNAME',
      'aio_key': 'YOUR_ADAFRUITIO_KEY',
    }
    ```

6. Update your `ssid`, `password`, `timezone`, `aio_username`, and `aio_key` with your relevant values. **You'll need at least `ssid` and `password` filled into connect the PyPortal device to your Wifi**.

7. **Time to start developing!** You can find more documentation in the `/docs` directory in this repository.

# Welcome to the Hemagon Tests

## Usage - Local

1. Copy `.env.dist` to `.env`

2. Change:
   - `TEST_BASEURL` to your test target URL
   - `DEV_ENV_MODE` to `local`
   - other ENVs related to your configuration

3. Install [Chromium](https://www.chromium.org/Home/) and [Python3](https://www.python.org/downloads/) with [Pip](https://pip.pypa.io/en/stable/installation/)

4. Install deps
   ```shell
   pip install -r requirements.txt
   ```

5. Run tests:
   ```shell
   pytest -vv -s %test_name%
   ```
   *replace `%test_name%` with path to tests, like: `test_main_page.py`


## Usage - Docker

1. Copy `.env.dist` to `.env`

2. Change:
    - `TEST_BASEURL` to your test target URL
    - `DEV_ENV_MODE` to `remote`
    - `SELENIUM_HUB_URL` to HUB Docker container name
    - other ENVs related to your configuration

3. Install [Docker](https://docs.docker.com/engine/install/)

4. Prepare and run containers:
   ```shell
   make up
   ```
   to start the containers  
   Also you can update base containers by:
   ```shell
   make pull
   ```
   
5. Run tests:
   ```shell
   docker compose -f dev.docker-compose.yml exec -iT pytest pytest -vv -s %test_name%
   ```
   *replace `%test_name%` with path to tests, like: `test_main_page.py`  

6. After all things are done call:
   ```shell
   make down
   ```
   to stop the containers

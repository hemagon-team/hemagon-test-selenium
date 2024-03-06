# Welcome to the Hemagon Tests

## Installation

1. Copy `.env.dist` to `.env`

2. Change `TEST_BASEURL` to your test target URL

3. On `/hemagon-test-selenium` folder call:
   ```shell
   make up
   ```
   to start the containers  
   Also you can update base containers by:
   ```shell
   make pull
   ```
   
4. Run tests:
   ```shell
   docker compose -f dev.docker-compose.yml exec -iT pytest pytest -vv -s %test_name%
   ```
   *replace `%test_name%` with path to tests, like: `test_suits/test_suit_tournament_view.py`  

5. After all things are done call:
   ```shell
   make down
   ```
   to stop the containers

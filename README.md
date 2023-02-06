# Netflix&Chilwell

<!-- ![Build Status](https://github.com/BassCoder2808/Netflix-and-Chilwell/actions/workflows/main.yml/badge.svg) -->

_Netflix&Chilwell_ is a package for using Machine learning to pick a Fantasy Premier League team.

<!-- For some background information and details see https://www.turing.ac.uk/research/research-programmes/research-engineering/programme-articles/Netflix-and-Chilwell.

We welcome contributions and comments - if you'd like to join the Netflix-and-Chilwell community please refer to our [contribution guidelines](https://github.com/BassCoder2808/Netflix-and-Chilwell/blob/master/CONTRIBUTING.md) -->

## Features (6th February 2023):

## GOOD TO HAVE FEATURES (Todo):

1. Creating Database from FPL API
2. Prediction Model
3. Transfer & Squad Optimization
4. Apply Transfers and Selecting Lineup
5. Creation of Pipeline

## Mini-league for 2023/24 season

We will be making a mini-league **"Prem-AI League"** for players using this software. To join, login to the FPL website, and navigate to the page to join a league: https://fantasy.premierleague.com/leagues/create-join then click "join a league or cup".
The code to join is: **coming soon**.
Hope to see your AI team there! :)

Our own Netflix-and-Chilwell team's id for the 2022/23 season is **[2779516](https://fantasy.premierleague.com/entry/2779516/history)**.

<!-- ## Installation

We recommend running Netflix-and-Chilwell in a conda environment. For instructions on how to install conda go to this link: https://docs.anaconda.com/anaconda/install/, or the more lightweight MiniConda: https://docs.conda.io/en/latest/miniconda.html.

With conda installed, run these commands in a terminal to create a new conda environment and download and install Netflix-and-Chilwell:

### Linux and macOS

```shell
git clone https://github.com/BassCoder2808/Netflix-and-Chilwell.git
cd Netflix-and-Chilwell
conda env create
conda activate Netflix-and-Chilwellenv
```

### Windows

The best ways to run Netflix-and-Chilwell on Windows are either to use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) (WSL), which allows you to run Netflix-and-Chilwell in a Linux environment on your Windows system, or Docker (see below).

After installing WSL, if you'd like to use Netflix-and-Chilwell with conda run the following commands to install it from your WSL terminal (following the Linux instructions [here](https://docs.conda.io/en/latest/miniconda.html#linux-installers)):

```shell
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

You can then follow the installation instructions for Linux and macOS above (or the instructions for without conda below).

You're free to try installing and using Netflix-and-Chilwell in Windows itself, but so far we haven't got it working. The main difficulties are with installing [jax](https://github.com/google/jax#installation) and some database/pickling errors (e.g. #165). If you do get it working we'd love to hear from you!

### Use Netflix-and-Chilwell without conda

To use Netflix-and-Chilwell without conda:

```shell
git clone https://github.com/BassCoder2808/Netflix-and-Chilwell.git
cd Netflix-and-Chilwell
pip install pygmo  # Linux only
pip install .
```

Netflix-and-Chilwell has an optional optimisation algorithm using the PyGMO package, which is only pip-installable on Linux (either use conda or don't install pygmo on other platforms). However, we have also occasionally seen errors when using conda (e.g. [#81](https://github.com/BassCoder2808/Netflix-and-Chilwell/issues/81))

### Docker

Build the docker-image:

```shell
docker build -t Netflix-and-Chilwell .
```

Create a volume for data persistance:

```shell
docker volume create Netflix-and-Chilwell_data
```

Run commands with your configuration as environment variables, eg:

```shell
docker run -it --rm -v Netflix-and-Chilwell_data:/tmp/ -e "FPL_TEAM_ID=<your_id>" -e "Netflix-and-Chilwell_HOME=/tmp" Netflix-and-Chilwell [Netflix-and-Chilwell_run_pipeline]
```

```Netflix-and-Chilwell_run_pipeline``` is the default command.

## Optional dependencies

Netflix-and-Chilwell has optional dependencies for plotting, running notebooks, and an in development Netflix-and-Chilwell API. To install them run:

```shell
pip install ".[api,notebook,plot]"
```

## Configuration

Once you've installed the module, you will need to set the following parameters:

**Required:**

1. `FPL_TEAM_ID`: the team ID for your FPL side.

**Optional:**

2. `FPL_LOGIN`: your FPL login, usually email (this is only required to get FPL league standings, or automating transfers via the API).

3. `FPL_PASSWORD`: your FPL password (this is only required to get FPL league standings, or automating transfers via the API).

4. `FPL_LEAGUE_ID`: a league ID for FPL (this is only required for plotting FPL league standings).

5. `Netflix-and-Chilwell_DB_FILE`: Local path to where you would like to store the Netflix-and-Chilwell sqlite3 database. If not set `Netflix-and-Chilwell_HOME/data.db` will be used by default.

The values for these should be defined either in environment variables with the names given above, or as files in `Netflix-and-Chilwell_HOME` (a directory Netflix-and-Chilwell creates on your system to save config files and the database).

To view the location of `Netflix-and-Chilwell_HOME` and the current values of all set Netflix-and-Chilwell environment variables run:

```bash
Netflix-and-Chilwell_env get
```

Use `Netflix-and-Chilwell_env set` to set values and store them for future use. For example:

```bash
Netflix-and-Chilwell_env set -k FPL_TEAM_ID -v 123456
```

See `Netflix-and-Chilwell_env --help` for other options.

## Getting Started

If you installed Netflix-and-Chilwell with conda, you should always make sure the `Netflix-and-Chilwellenv` virtual environment is activated before running Netflix-and-Chilwell commands. To activate the environment use:

```shell
conda activate Netflix-and-Chilwellenv
```

Note: Most the commands below can be run with the `--help` flag to see additional options and information.

### 1. Creating the database

Once the module has been installed and your team ID configured, run the following command to create the Netflix-and-Chilwell database:

```shell
Netflix-and-Chilwell_setup_initial_db
```

This will fill the database with data from the last 3 seasons, as well as all available fixtures and results for the current season.
On Linux/Mac you should get a file ```/tmp/data.db``` containing the database (on Windows you will get a `data.db` file in a the temporary directory returned by the python [tempfile module](https://docs.python.org/3/library/tempfile.html) on your system).

You can run sanity checks on the data using the following command:

```shell
Netflix-and-Chilwell_check_data
```

### 2. Updating and Running Predictions

To stay up to date in the future, you will need to fill three tables: ```match```, ```player_score```, and ```transaction```
with more recent data, using the command

```shell
Netflix-and-Chilwell_update_db
```

The next step is to use the team- and player-level Stan models to predict the expected points for all players for the next fixtures.  This is done using the command

```shell
Netflix-and-Chilwell_run_prediction --weeks_ahead 3
```

(we normally look 3 weeks ahead, as this is an achievable horizon to run the optimization over, but also because things like form and injuries can change a lot in 3 weeks!)

Predicted points must be generated before running the transfer or squad optimization (see below).

### 3. Transfer or Squad Optimization

Finally, we need to run the optimizer to pick the best transfer strategy over the next weeks (and hence the best team for the next week).

```shell
Netflix-and-Chilwell_run_optimization --weeks_ahead 3
```

This will take a while, but should eventually provide a printout of the optimal transfer strategy, in addition to the teamsheet for the next match (including who to make captain, and the order of the substitutes). You can also optimise chip usage with the arguments ` --wildcard_week <GW>`, `--free_hit_week <GW>`, `--triple_captain_week <GW>` and `--bench_boost_week <GW>`, replacing `<GW>` with the gameweek you want to play the chip (or use `0` to try playing the chip in all gameweeks).

Note that `Netflix-and-Chilwell_run_optimization` should only be used for transfer suggestions after the season has started. If it's before the season has started and you want to generate a full squad for gameweek one you should instead use:

```shell
Netflix-and-Chilwell_make_squad --num_gameweeks 3
```

### 4. Apply Transfers and Lineup

To apply the transfers recommended by Netflix-and-Chilwell to your team on the FPL website run `Netflix-and-Chilwell_make_transfers`. This can't be undone! You can also use `Netflix-and-Chilwell_set_lineup` to set your starting lineup, captaincy choices, and substitute order to Netflix-and-Chilwell's recommendation (without making any transfers). Note that you must have created the `FPL_LOGIN` and `FPL_PASSWORD` files for these to work (as described in the "Configuration" section above).

### Run the Full Netflix-and-Chilwell Pipeline

Instead of running the commands above individually you can use:

```shell
Netflix-and-Chilwell_run_pipeline
```

This will update the database and then run the points predictions and transfer optimization.  Add `--help` to see the available options.

## Issues and New Features

Netflix-and-Chilwell is regularly developed to fix bugs and add new features. If you have any problems during installation or usage please let us know by [creating an issue](https://github.com/BassCoder2808/Netflix-and-Chilwell/issues/new) (or have a look through [existing issues](https://github.com/BassCoder2808/Netflix-and-Chilwell/issues) to see if it's something we're already working on).

You may also like to try the development version of Netflix-and-Chilwell, which has the latest fixes and features. To do this checkout the `develop` branch of the repo and reinstall:

```shell
git pull
git checkout develop
pip install --force-reinstall .
```


## Development

If you're developing Netflix-and-Chilwell you may find it helpful to install it in editable mode:

```shell
pip install -e .
```

We're in the process of migrating to [Poetry](https://python-poetry.org/docs/), but as `PyGMO` is not available on `PyPI` on all platforms this is a work on progress. However, you can set up a development environment without `PyGMO` by running `poetry install` and then `poetry shell` to enter the environment.

We also have a [pre-commit](https://pre-commit.com/) config to run the code quality tools we use (`flake8`, `isort`, and `black`) automatically when making commits. If you're using `poetry` it will be installed as a dev dependency, otherwise run `pip install pre-commit`. Then to setup the commit hooks:

```shell
pre-commit install --install-hooks
``` -->

## Contributing

We welcome all types of contribution to Netflix&Chilwell, for example questions, documentation, bug fixes, new features and more. Please see our [contributing guidelines](CONTRIBUTING.md). If you're contributing for the first time but not sure what to do a good place to start may be to look at our [current issues](https://github.com/BassCoder2808/Netflix-and-Chilwell/issues), particularly any with the ["Good first issue" tag](https://github.com/BassCoder2808/Netflix-and-Chilwell/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22). Also feel free to just say hello!

import os
from datetime import datetime

import pandas as pd
from tqdm import tqdm

from pepai.framework.schema import Absence, session
from pepai.framework.season import CURRENT_SEASON, sort_seasons
from pepai.framework.utils import (
    get_next_gameweek_by_date,
    get_past_seasons,
    get_player,
)


def load_absences(season, dbsession):
    print(f"ABSENCES {season}")
    path = os.path.join(
        os.path.dirname(__file__), "..", "data", f"absences_{season}.csv"
    )
    absences = pd.read_csv(
        path, parse_dates=["from", "until"], infer_datetime_format=True
    )

    for _, row in tqdm(absences.iterrows(), total=absences.shape[0]):
        p = get_player(row["player"], dbsession=dbsession)
        if not p:
            print(f"Couldn't find player {row['player']}")
            continue
        date_from = row["from"].date()
        if date_from is pd.NaT:
            print(f"{row['player']} {row['absence']} has no from date")
            continue
        date_until = None if row["until"] is pd.NaT else row["until"].date()

        gw_from = get_next_gameweek_by_date(date_from, season, dbsession)
        gw_until = (
            get_next_gameweek_by_date(date_until, season, dbsession)
            if date_until
            else None
        )

        url = row["url"]
        timestamp = datetime.now().isoformat()
        absence = Absence(
            player=p,
            player_id=p.player_id,
            season=season,
            reason=row["reason"],
            details=row["details"],
            date_from=date_from,
            date_until=date_until,
            gw_from=gw_from,
            gw_until=gw_until,
            url=url,
            timestamp=timestamp,
        )

        dbsession.add(absence)
    dbsession.commit()


def make_absence_table(seasons=get_past_seasons(3), dbsession=session):
    for season in sort_seasons(seasons):
        if season == CURRENT_SEASON:
            continue
        load_absences(season, dbsession)

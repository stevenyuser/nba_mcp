from fastmcp import FastMCP
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import playercareerstats, playerawards, playergamelog, teamyearbyyearstats, teamdetails, teamgamelog, leaguestandingsv3

mcp = FastMCP("NBA MCP Server")

# Tools

# Player Tools

@mcp.tool
def get_player_career_stats(player_id: str) -> dict:
    """
    Get career stats for a player by their ID.
    
    Args:
      player_id: str
        The id of the player.
    """
    try:
      stats = playercareerstats.PlayerCareerStats(player_id=player_id)
      return stats.get_json()
    except Exception as e:
      return {"error": str(e)}

@mcp.tool
def get_player_awards(player_id: str) -> dict:
    """
    Get awards for a player by their ID.

    Args:
      player_id: str
        The id of the player.
    """
    try:
      awards = playerawards.PlayerAwards(player_id=player_id)
      return awards.get_json()
    except Exception as e:
      return {"error": str(e)}

@mcp.tool
def get_player_game_log(player_id: str, season: str, season_type: str) -> dict:
   """
   Get game log for a player by their ID, season, and season type.

   Args:
      player_id: str
        The id of the player.
      season: str
        The season in the format 'YYYY-YY'.
      season_type: str
        The type of season. Pattern: "Regular Season", "Pre Season", "Playoffs", "All Star"
    """

   try:
      log = playergamelog.PlayerGameLog(player_id=player_id, 
                                        season=season, 
                                        season_type_all_star=season_type)
      return log.get_json()
   except Exception as e:
      return {"error": str(e)}

# Team Tools

@mcp.tool
def get_team_details(team_id: str) -> dict:
    """
    Get details for a team by their ID.
    Details include championship awards, conference awards, division awards, background, history, and more.

    Args:
      team_id: str
        The id of the team.
    """
    try:
        details = teamdetails.TeamDetails(team_id=team_id)
        return details.get_json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool
def get_team_year_by_year_stats(team_id: str) -> dict:
    """
    Get year-by-year stats for a team by their ID.

    Args:
      team_id: str
        The id of the team.
    """
    try:
        stats = teamyearbyyearstats.TeamYearByYearStats(team_id=team_id)
        return stats.get_json()
    except Exception as e:
        return {"error": str(e)}
    
@mcp.tool
def get_team_game_log(team_id: str, season: str, season_type: str) -> dict:
    """
    Get game log for a team by their ID, season, and season type.
    
    Args:
      team_id: str
        The id of the team.
      season: str
        The season in the format 'YYYY-YY'.
      season_type: str
        The type of season. Pattern: "Regular Season", "Pre Season", "Playoffs", "All Star"
    """
    try:
        log = teamgamelog.TeamGameLog(team_id=team_id, 
                                      season=season, 
                                      season_type_all_star=season_type)
        return log.get_json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool
def get_league_team_standings(season: str, season_type: str) -> dict:
    """
    Get league team standings for a given season and season type.
    
    Args:
      season: str
        The season in the format 'YYYY-YY'.
      season_type: str
        The type of season. Pattern: "Regular Season", "Pre Season"
    """
    try:
        standings = leaguestandingsv3.LeagueStandingsV3(league_id="00",
                                                        season=season, 
                                                        season_type=season_type)
        return standings.get_json()
    except Exception as e:
        return {"error": str(e)}

# Resources

@mcp.resource("nba://players")
def get_players() -> list:
  """
  Get a list of all NBA players.
  """
  return players.get_players()

@mcp.resource("nba://active_players")
def get_active_players() -> list:
  """
  Get a list of all active NBA players.
  """
  return players.get_active_players()

@mcp.resource("nba://teams")
def get_teams() -> list:
  """
  Get a list of all NBA teams.
  """
  return teams.get_teams()

if __name__ == "__main__":
    mcp.run()
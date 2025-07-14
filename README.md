# NBA MCP Server

A simple MCP (Model Context Protocol) server for getting NBA data through [nba_api](https://github.com/swar/nba_api). 
This server allows LLMs to retrieve player stats, team stats, game logs, team standings, and more.

## Tools

### Player Tools
`get_player_career_stats(player_id: str)`

Get comprehensive career statistics for a player.

`get_player_awards(player_id: str)`

Retrieve all awards and achievements for a player, including MVP awards, All-Star selections, championships, etc.

`get_player_game_log(player_id: str, season: str, season_type: str)`

Player game-by-game statistics and results.

### Team Tools
`get_team_details(team_id: str)`

Get comprehensive team information includes championships, conference awards, division awards, history, and background.

`get_team_year_by_year_stats(team_id: str)`
Historical year-by-year team performance statistics.

`get_team_game_log(team_id: str, season: str, season_type: str)`

Team game-by-game statistics and results.

`get_league_team_standings(season: str, season_type: str)`

Standings for all teams in the league by season.

## Resources
`nba://players`

Returns a list of all NBA players (past and present).

`nba://active_players`

Returns a list of currently active NBA players.

`nba://teams`

Returns a list of all NBA teams.

## Usage
To use this MCP server via Claude for Desktop, add the following to your Claude Desktop config file.

```
{
  "mcpServers": {
    "nba_mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/nba_mcp",
        "run",
        "server.py"
      ]
    }
  }
}
```
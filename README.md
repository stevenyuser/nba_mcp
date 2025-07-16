# NBA MCP Server

A simple MCP (Model Context Protocol) server for getting NBA data through [nba_api](https://github.com/swar/nba_api). 
This server allows LLMs to retrieve live game data, player stats, team stats, game logs, team standings, and more.

## Demo
https://github.com/user-attachments/assets/ce448f94-0226-4303-95e2-19f125a83a02

## Tools

### Player Tools
`get_player_career_stats(player_id: str)`

Gets comprehensive career statistics for a player.

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

## Live Game Tools
`get_today_scoreboard()`
Retrieves today's NBA games, including live scores, game statuses, and teaminformation.

`get_live_game_boxscore(game_id: str)`
Gets live game data, including scores, player stats, timeouts, and more.

`get_live_game_play_by_play(game_id: str)`
Gets live play-by-play data from a game.

## Resources
`nba://players`

Returns a list of all NBA players (past and present).

`nba://active_players`

Returns a list of currently active NBA players.

`nba://teams`

Returns a list of all NBA teams.

## Usage
To use this MCP server with Claude for Desktop, add either of the following to your Claude Desktop config file.

Via uv:
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

Via Docker:
```
{
  "mcpServers": {
    "nba_mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "stevenyuser/nba-mcp"
      ]
    }
  }
}
```

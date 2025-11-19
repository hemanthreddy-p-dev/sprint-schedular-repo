# main.py

import os

import yaml

from datetime import date, timedelta

from dotenv import load_dotenv

from prstrands.orchestrator import main_run  # Ensure this module is installed and available
 
def load_config():

    """Load configuration from YAML file."""

    with open("config.yaml", "r") as f:

        return yaml.safe_load(f)
 
def get_next_monday():

    """Compute the next Monday from today."""

    today = date.today()

    days_ahead = (0 - today.weekday() + 7) % 7

    if days_ahead == 0:  # If today is Monday, start next Monday

        days_ahead = 7

    return today + timedelta(days=days_ahead)
 
def build_prompt(cfg):

    """Builds the structured LLM prompt for sprint ceremonies using dynamic start date and config values."""

    start_date = get_next_monday()

    return f"""

    Generate a {cfg['sprint_length_days']}-day sprint schedule for the team "{cfg['team_name']}" starting on {start_date} (Monday).

    Include the following ceremonies:

    - Sprint Planning: First day at {cfg['sprint_planning_time']}, duration 120 minutes. Agenda: Review backlog, prioritize stories, estimate tasks.

    - Daily Standup: Every weekday at {cfg['daily_standup_time']}, duration 15 minutes. Agenda: What did you do yesterday? What will you do today? Any blockers?

    - Technical Refinement: Twice mid-sprint (e.g., Day 5 and Day 10) at {cfg['technical_refinement_time']}, duration 30 minutes. Agenda: Discuss technical challenges and architecture decisions.

    - Sprint Review: Last day at {cfg['sprint_review_time']}, duration 60 minutes. Agenda: Demo completed work, collect feedback.

    - Retrospective: Immediately after Sprint Review (same day) at {cfg['retrospective_time']}, duration 60 minutes. Agenda: What went well, what didn’t, action items.
 
    IMPORTANT: Ensure Daily Standup is scheduled on the first day (Monday) along with Sprint Planning.
 
    Provide output in **valid JSON** format as a list of objects, e.g.:

    [

        {{

            "name": "Sprint Planning",

            "date": "{start_date}",

            "time": "{cfg['sprint_planning_time']}",

            "duration_minutes": 120,

            "agenda": "Review backlog, prioritize stories, estimate tasks."

        }},

        {{

            "name": "Daily Standup",

            "date": "{start_date}",

            "time": "{cfg['daily_standup_time']}",

            "duration_minutes": 15,

            "agenda": "What did you do yesterday? What will you do today? Any blockers?"

        }},

        ...

    ]

    """
 
if __name__ == "__main__":

    # ✅ Step 1: Load environment variables

    load_dotenv()
 
    # ✅ Step 2: Load configuration

    cfg = load_config()
 
    # ✅ Step 3: Build structured prompt for LLM

    user_prompt = build_prompt(cfg)
 
    # ✅ Step 4: Run the Strands orchestration

    print("🚀 Running Sprint Automation AI Orchestrator...")

    main_run(cfg, user_prompt)
 
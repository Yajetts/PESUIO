from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai import LLM
import os

llm = LLM(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

os.environ['SERPER_API_KEY'] = '7197ecb791115c049d339897b92a20fb938ab91c'

@CrewBase  # type: ignore
class FinalProjectCrew:
    """FinalProjectCrew"""

    @agent
    def stat_search_agent(self) -> Agent:
        return Agent(
            llm=llm,
            config=self.agents_config["stat_search_agent"],
            tools=[SerperDevTool()],  # Example of custom tool, loaded at the beginning of the file
            verbose=True,
        )

    @agent
    def stat_analysis_agent(self) -> Agent:
        return Agent(
            llm=llm, config=self.agents_config["stat_analysis_agent"], verbose=True
        )

    @task
    def web_search(self) -> Task:
        return Task(
            config=self.tasks_config["web_search"],
        )

    @task
    def analyze_results(self) -> Task:
        return Task(config=self.tasks_config["analyze_results"], output_file="report.md")

    @crew
    def crew(self) -> Crew:
        """Creates the LatestAiDevelopment crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

"""data_analyst_agent for finding information using google search"""

from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool
from data_analyst_agent.tools.financial_data import financial_data
from data_analyst_agent.tools.stock_price import get_stock_market_data
from data_analyst_agent.subagents.market_news_agent.agent import market_news_agent

from . import prompt

MODEL = "gemini-2.0-flash"
market_news_analyzer = AgentTool(agent=market_news_agent)

data_analyst_agent = Agent(
    model=MODEL,
    name="data_analyst_agent",
    instruction=prompt.DATA_ANALYST_PROMPT,
    output_key="market_data_analysis_output",
    tools=[get_stock_market_data, financial_data, market_news_analyzer],
)

root_agent = data_analyst_agent
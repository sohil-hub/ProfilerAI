import json
import os

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

name = "MohammedSohil Shaikh Venturit Jr Data Scientist"
# data = json.load(open("/Users/venturit/Desktop/Projects/RLHF/ice_breaker/third_parties/demo_data/edon_marco.json"))
if __name__ == "__main__":
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    print(linkedin_data)
    # twitter_user_name = twitter_lookup_agent(name=name)
    # twitter_data = scrape_user_tweets(username="@_the_faisal", num_tweets=100)

    summary_template = """
             given the Linkedin information {information} about a person from I want you to create:
             1. a short summary
             2. two interesting facts about them
             3. A topic that may interest them
             4. 2 creative Ice breakers to open a conversation with them 
         """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=linkedin_data))

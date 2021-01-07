import requests
from bs4 import BeautifulSoup as bs
import re
import twitter
import os

api_key = os.getenv('API_KEY_TWIT')
secret_key = os.getenv('secret_key')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

# api = twitter.Api(consumer_key=api_key, consumer_secret=secret_key, access_token_key=access_token, access_token_secret=access_token_secret)

def get_jaden_tweets():
  #get info from webpage
  r = requests.get("https://everydaypower.com/jaden-smith-quotes/")
  soup = bs(r.content, features="html5lib")
  headers = soup.find_all("p")
  just_text = [text for text in soup.stripped_strings]
  quotes = []
  for q in just_text:
      value = re.search("^\d+\.", q)
      if value is not None:
          text = re.sub(r'\d+', '', value.string)
          if (len(text) < 5):
              continue
          text = text[3:]
          text = text.replace('\xa0', "")
          text = text.replace('” –', "")
          quotes.append(text)

  url = 'https://mashable.com/2014/12/30/jaden-smith-tweets-2014/'
  r = requests.get(url)
  soup = bs(r.content, features="html5lib")
  just_text = [text for text in soup.stripped_strings]
  tweets = just_text[144:187]
  for t in tweets:
      if t.find("2014") > -1:
        
          tweets.remove(t)
      if t == "— Jaden Smith (@officialjaden)":
          
          tweets.remove(t)
      
  for t in tweets:
      if t.find("2014") > -1:
          
          tweets.remove(t)
          
  quotes.extend(tweets)

# just_text = [text for text in soup.stripped_strings]
# print(just_text)
  firstphraselist = [ "dear everyone:",
			"Dude,",
			"FYI haters,",
			"Girl, you so fine. But",
			"Jaden says:",
			"my pshyche says:",
			"I speak jaden.",
			"I'm sorry bae, but",
			"I've said it before and i'll say it again,",
			"it's like i always say,",
			"in conclusion,",
			"listen,",
			"REAL TALK:",
			"Sup girl.",
			"That feeling when your bae tells you",
			"trees be all like",
			"Yo"]

  secondphaselist = ["a book always runs out of paper.",
			 "a mindframe is still a frame.",
			 "a mirror is only a prison for your reflection.",
			 "adults confuse me.",
			 "all trees are time travellers.",
			 "age isn't a religion.", 
			 "bats don't need to listen because they can already hear everything.",
			 "can you prove human beings CAN'T teleport?",
			 "do any of us really have a mind?",
			 "do you believe existence believes in you?",
			 "does anyone else taste dark matter?",
			 "DON'T stay in school.",
			 "don't read everything you believe.",
			 "don't listen to the distractions.",
			 "experience is a choice.",
			 "gravity isn't real.",
			 "how can someone find themself if they're in school all day?",
			 "how come we don't have passports for trees?",
			 "how do we know cupcakes aren't afraid to be eaten?",
			 "how do you know when you fall asleep that you're not actually waking up?",
			 "I am a sad.",
			 "I blow my own mind on an hourly basis.",
			 "I can't decide if i should take a trip to Norway or Jupiter.",
			 "i cry distilled tears.",
			 "i don't need to listen to you.",
			 "I use two dreamcatchers because just one fills up too quickly.",
		     "I'm embaressed for you.",
		     "I'm just being real.",
		     "I'm looking at trees.",
			 "If only all the extinct animals hadn't gone extinct, they would probably be able to talk by now.",
			 "If more people were willing to speak the same truth as me the world would be less sad.",
			 "if pilot school was necessary then why are there still plane crashes?",
			 "if you can't appreciate what i say you can't appreciate honest philosophy and poetry.",
			 "if you could speak to babies you would be the most intelligent person on the planet.",
			 "if you could weigh thoughts human beings would be the heaviest things on this planet.",
			 "if you were born on this planet you can already speak every language in the world.",
			 "I am 10,000% lé git.",
			 "I don't recognize what you call grammar.",
			 "Jake Gyllenhaal.",
			 "just like school your grammar can't hold me.",
			 "Listen to your mind",
			 "Let's meld particles.",
			 "let's bond on a cellular level.",
			 "Lets get all sad and shit.",
			 "look at your hands.",
			 "maybe I was born in the wrong dimension.",
			 "maybe that's the point.",
			 "meet me in the DMs.",
			 "meet me on FaceTime and let's talk about SpaceTime.",
			 "my young mind is older than you think.",
			 "next time you see a tree you should apologize.",
			 "no i will not follow trolls.",
			 "no one teaches school to teach.",
			 "nothing that's worth learning can be taught in school.",
			 "our eyes aren't the begining.",
			 "realness is my only religion.",
			 "school isn't real.",
			 "Shia LaBeouf.",
			 "some of us are better at time travel than others.",
			 "sometimes I am scared by all my wisdom.",
			 "trees are immortal so you can't surprise them.",
			 "the fact i think about these big questions is proof the universe has a consciousness.",
			 "the planet is older than you think.",
			 "these thoughts are immortal.",
			 "there ain't room in this oxygen chamber for two.",
			 "This is what a profound tweet looks like.",
			 "trees don't know how to be sad.",
			 "trees would run away if they could.",
			 "UFOs.",
			 "UFOs can see us too.",
			 "understanding still leaves you standing.",
			 "unlock the Large Hadron Collider in your mind.",
			 "we are all the same age because atoms don't age.",
			 "why do  police enforce speed limits when the earth is moving at a million miles an hour?",
             "why do we go to school again?",
             "you can't fail something you don't believe in.",
             "you can't force something that isn't real.",
             "why read something you can experience?",
             "your 140 characters can't contain me.",
             "you sound like you still think mirrors are real.",
             "you should experience more.",
			 "you'd be too scared to talk to a real tree.",
			 "we are all time travellers.",
			 "we are never not looking in a mirror.",
			 "we only have one planet...for now.",
			 "what do you think the aliens watching us make of all your hatin?",
			 "why do i need a passport if i was born on this planet?",
			 "why read something you can experience?",
			 "yeah i've been to space. what do you think this planet is floating in?",
			 "Yo."]
			 
  thirdphraselist = [ 
             "← If You Cant Handle this kind of raw power and emotion please unfollow me.",
			 "← very powerful thought right here.",
			 "[Drops Mic]",
			 "a tree just whispered that to me in my sleep.",
			 "And no, I didn't learn that in ''school''...obviously.",
			 "and no, my twitter has not been hacked.", 
			 "be realer.",
			 "Coachella.",
			 "cosmic.",
			 "Damn, that's some mind-blowing wisdom.",
			 "deleting twitter now.",
			 "drink nothing but distilled water for a month and you'll see what i mean.",
			 "either you get it or you don't.",
			 "epic.",
			 "hashtag jupiter.",
			 "I bet no one has ever said that before.",
			 "I can't say much more because I'm *literally* about to transcend.",
			 "I know this from first hand experience.",
			 "If you don't understand. Maybe that's the point.",
			 "It's super obvious when you think about it.",
			 "Jaden out.",
			 "Keanu Reeves.",
			 "kendall gets it and maybe one day you will too.",
			 "now, if you excuse me, i have to go have an out-of-body experience.",
			 "now, if you excuse me, I have to go stare in the mirror and cry.",
			 "now, if you excuse me, I have to go watch Donnie Darko again",
			 "on an unrelated note, has anyone seen the new Seth Rogan film? ",
			 "PS. I am now inside your head",
			 "particles, man.",
             "Peace.",
			 "peace out.",
			 "radical.",
			 "Remember this.",
			 "Shia LaBeouf",
			 "sorry if that's too ''real'' for your human brain.",
			 "This is why nobody gets me.",   
			 "That is tight.",
			 "this is my art ladies and gentlemen.",
			 "this is my art ladies and gentlemen. Peace.",
			 "This may be my best tweet ever.",
			 "think about that for a second.",
			 "Tight.",
			 "Totally unrelated, I just saw Day After Tomorrow again. Shit is dope.",
			 "Watch Donnie Darko again and you'll see what i mean.",
			 "Willow knows what I'm talking about.",
			 "you are now excused.",
			 "you can have that one for free.",
			 "You're welcome."]

  quotes.extend(firstphraselist)
  quotes.extend(secondphaselist)
  quotes.extend(thirdphraselist)

  return quotes

# timeline = api.GetUserTimeline(screen_name='jaden', count=250)
# for t in timeline:
#     if not t.text.startswith("RT") and t.text.find('https://t.co') == -1 and t.text.find('@') == -1:
#         quotes.append(t.text)
#         print(t.text)


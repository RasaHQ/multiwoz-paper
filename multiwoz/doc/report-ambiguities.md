# Ambiguities in MultiWOZ stories

Why does core not learn much from the 800 parsed MultiWOZ stories (parsed with aggregated actions)?
I write the `story_tree.py` script to explore if stories are consistent.
In particular, we want to know if there are sequences of turns that result in a branch point, where some stories go one way and others go another way despite all pervious actions, slots, and intents being identical.
If this is the case, then core cannot possibly learn a consistent policy, and we'll have to adjust the parser.

## Inference from plain text

After looking at a dozen or so stories, I conclude that the plain text is useless to distinguish between different wizard actions.
In other words, there is no significant difference in the preceding utterances that could account for the different reaction of the wizard.

## Possible ways to improve the stories

First, the parser output has to be made deterministic. 
Due to the use of sets, some ordering is random, which makes it hard to compare different versions.
This was fixed with commit 918765061455b43aeff8d492993cc39e22f1c6b4.

1. Aggregate actions even more and fill slots instead, e.g. instead of `request_area_price_hotel` we could have

    - inquire_hotel
    - slot{"bot_requests": {'hotel_area', 'hotel_price'}} 

   Such slots may need to be reset after the next user utterance, however, and this reduced the complexity of the task significantly.
Ideally, we want to maintain the complexity of the data set.

2. (!) To deal with the difference between `request_type_attraction` and `inform_type_attraction` (`request` is a question and `inform` is listing options to the user), etc., we could do this: 

    - check_attraction
    - slot{"need_more_info_attraction": True}
    - request_..._attraction

   and `inform_..._attraction` if `"need_more_info_attraction"` is `False`. 

3. It might make sense to combine `recommend` and `inform`. 

4. It looks like I should order "request..." and "inform...", because there are instances where

    inform_choice_food_restaurant
    request_price_restaurant

   and other instances where

    request_area_price_restaurant
    inform_choice_food_restaurant

   Still, there is no way to distinguish between `_price_` and `_area_price_`. Not even from the plain dialog text.

5. (!) We could use a **latent variable** ("personaloty slot") to account for different branches.
6. (!) Dialogues that start with chitchat should just be deleted from the data set.
7. Augment chitchat with the domain that occurs next, e.g. `say_hotel` instead of `chitchat`
8. Augment `inform` user utterances with domain, e.g. `inform_hotel{...}`, though this would not reduce ambiguity

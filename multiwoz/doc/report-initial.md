# Initial tests of Transformer policy with MultiWOZ

I trained the transformer policy with **80 stories** from the MultiWOZ data set and tested it against itself, as well as against a **test set of 20 stories**.
I decided to use such a small sample as an initial test, because it trains within an hour and a low training f1-score could indicate high labeling noise. 
Specifically, I used the following configuration for Rasa Core:
    
    # Configuration for Rasa Core.
    # https://rasa.com/docs/rasa/core/policies/
    policies:
      - name: EmbeddingPolicy
        max_history: 6
        transformer: true
        epochs: 500
        batch_size: [32, 64]
        attn_shift_range: 5
        num_neg: 20
        similarity_type: 'inner'
        scale_loss_by_action_counts: true
        evaluate_every_num_epochs: 10
        evaluate_on_num_examples: 10
      - name: FormPolicy

## Training set

### Metrics

                                      precision    recall  f1-score   support
                           micro avg       0.93      0.93      0.93      2166
                           macro avg       0.88      0.86      0.87      2166
                        weighted avg       0.94      0.93      0.93      2166
    					
                   action_book_hotel       0.96      1.00      0.98        22
              action_book_restaurant       0.95      1.00      0.98        21
                    action_book_taxi       1.00      1.00      1.00        16
                   action_book_train       1.00      1.00      1.00        17
                       action_listen       0.96      0.97      0.96       601
                  utter_book_booking       1.00      1.00      1.00         1
              utter_book_day_booking       1.00      0.60      0.75         5
             utter_book_name_booking       0.80      1.00      0.89         8
           utter_book_people_booking       1.00      1.00      1.00         8
              utter_book_ref_booking       0.98      1.00      0.99        42
             utter_book_stay_booking       1.00      1.00      1.00         6
             utter_book_time_booking       1.00      1.00      1.00         7
                   utter_bye_general       0.95      0.97      0.96        74
                 utter_greet_general       0.89      0.53      0.67        15
        utter_inform_addr_attraction       0.88      0.88      0.88        24
             utter_inform_addr_hotel       1.00      1.00      1.00         7
        utter_inform_addr_restaurant       0.89      0.80      0.84        10
        utter_inform_area_attraction       0.93      0.96      0.94        26
             utter_inform_area_hotel       1.00      1.00      1.00        15
        utter_inform_area_restaurant       1.00      0.79      0.88        19
            utter_inform_arrive_taxi       1.00      1.00      1.00         1
           utter_inform_arrive_train       0.96      0.93      0.94        27
                utter_inform_booking       1.00      0.95      0.97        39
               utter_inform_car_taxi       0.94      1.00      0.97        17
      utter_inform_choice_attraction       0.95      0.86      0.90        21
           utter_inform_choice_hotel       1.00      0.93      0.96        28
      utter_inform_choice_restaurant       0.91      0.81      0.86        26
           utter_inform_choice_train       1.00      0.94      0.97        17
            utter_inform_day_booking       1.00      1.00      1.00         1
              utter_inform_day_train       1.00      0.88      0.93         8
            utter_inform_depart_taxi       1.00      0.75      0.86         4
           utter_inform_depart_train       0.89      1.00      0.94        16
              utter_inform_dest_taxi       1.00      1.00      1.00         2
             utter_inform_dest_train       1.00      0.94      0.97        16
         utter_inform_fee_attraction       0.94      0.80      0.86        20
        utter_inform_food_restaurant       0.81      0.91      0.86        23
                  utter_inform_hotel       0.00      0.00      0.00         2
               utter_inform_id_train       1.00      0.91      0.95        23
         utter_inform_internet_hotel       0.91      0.91      0.91        11
             utter_inform_leave_taxi       1.00      1.00      1.00         3
            utter_inform_leave_train       0.96      0.92      0.94        24
        utter_inform_name_attraction       0.84      0.84      0.84        31
           utter_inform_name_booking       1.00      1.00      1.00         2
             utter_inform_name_hotel       1.00      0.95      0.98        22
        utter_inform_name_restaurant       0.96      0.96      0.96        28
          utter_inform_parking_hotel       1.00      1.00      1.00        12
         utter_inform_people_booking       0.25      1.00      0.40         2
       utter_inform_phone_attraction       1.00      0.68      0.81        19
            utter_inform_phone_hotel       1.00      1.00      1.00         7
       utter_inform_phone_restaurant       1.00      0.83      0.91         6
             utter_inform_phone_taxi       1.00      1.00      1.00        17
        utter_inform_post_attraction       1.00      0.93      0.96        14
             utter_inform_post_hotel       1.00      1.00      1.00         5
        utter_inform_post_restaurant       1.00      1.00      1.00         7
            utter_inform_price_hotel       1.00      0.87      0.93        15
       utter_inform_price_restaurant       0.83      0.88      0.86        17
         utter_inform_ref_restaurant       1.00      1.00      1.00         1
              utter_inform_ref_train       1.00      1.00      1.00         1
            utter_inform_stars_hotel       1.00      1.00      1.00        12
           utter_inform_stay_booking       1.00      1.00      1.00         1
           utter_inform_ticket_train       0.92      0.73      0.81        15
           utter_inform_time_booking       1.00      1.00      1.00         1
             utter_inform_time_train       1.00      0.80      0.89        10
        utter_inform_type_attraction       0.90      0.86      0.88        21
             utter_inform_type_hotel       1.00      1.00      1.00        21
                utter_nobook_booking       0.75      0.90      0.82        10
            utter_nobook_day_booking       1.00      1.00      1.00         4
         utter_nobook_people_booking       1.00      1.00      1.00         1
           utter_nobook_stay_booking       0.67      0.50      0.57         4
           utter_nobook_time_booking       1.00      1.00      1.00         1
       utter_nooffer_addr_attraction       0.00      0.00      0.00         0
       utter_nooffer_area_attraction       1.00      1.00      1.00         4
            utter_nooffer_area_hotel       1.00      1.00      1.00         1
       utter_nooffer_area_restaurant       1.00      1.00      1.00         3
            utter_nooffer_attraction       1.00      0.50      0.67         2
       utter_nooffer_food_restaurant       1.00      1.00      1.00         6
                 utter_nooffer_hotel       0.00      0.00      0.00         2
        utter_nooffer_internet_hotel       1.00      1.00      1.00         1
           utter_nooffer_leave_train       1.00      1.00      1.00         1
       utter_nooffer_name_attraction       1.00      1.00      1.00         1
       utter_nooffer_name_restaurant       0.00      0.00      0.00         1
           utter_nooffer_price_hotel       1.00      1.00      1.00         1
      utter_nooffer_price_restaurant       1.00      1.00      1.00         3
           utter_nooffer_stars_hotel       0.50      1.00      0.67         2
       utter_nooffer_type_attraction       0.80      0.80      0.80         5
            utter_nooffer_type_hotel       1.00      1.00      1.00         3
        utter_offerbook_arrive_train       1.00      1.00      1.00         2
        utter_offerbook_choice_train       1.00      1.00      1.00         1
        utter_offerbook_depart_train       0.00      0.00      0.00         0
         utter_offerbook_leave_train       1.00      1.00      1.00         1
          utter_offerbook_time_train       0.00      0.00      0.00         0
               utter_offerbook_train       1.00      0.92      0.96        24
      utter_offerbooked_arrive_train       1.00      1.00      1.00         3
      utter_offerbooked_depart_train       1.00      1.00      1.00         1
        utter_offerbooked_dest_train       1.00      1.00      1.00         1
          utter_offerbooked_id_train       0.67      0.50      0.57         4
       utter_offerbooked_leave_train       1.00      1.00      1.00         3
      utter_offerbooked_people_train       0.80      1.00      0.89         4
         utter_offerbooked_ref_train       0.89      0.89      0.89        18
      utter_offerbooked_ticket_train       1.00      0.92      0.96        12
     utter_recommend_addr_attraction       1.00      0.75      0.86         4
          utter_recommend_addr_hotel       1.00      1.00      1.00         2
          utter_recommend_area_hotel       1.00      1.00      1.00         6
     utter_recommend_area_restaurant       1.00      1.00      1.00         2
        utter_recommend_choice_hotel       1.00      1.00      1.00         1
      utter_recommend_fee_attraction       1.00      1.00      1.00         5
     utter_recommend_food_restaurant       1.00      0.50      0.67         2
               utter_recommend_hotel       0.00      0.00      0.00         1
      utter_recommend_internet_hotel       0.75      1.00      0.86         3
     utter_recommend_name_attraction       1.00      0.94      0.97        16
          utter_recommend_name_hotel       1.00      1.00      1.00        14
     utter_recommend_name_restaurant       1.00      1.00      1.00         9
       utter_recommend_parking_hotel       1.00      1.00      1.00         3
    utter_recommend_phone_attraction       1.00      1.00      1.00         1
         utter_recommend_phone_hotel       1.00      1.00      1.00         2
     utter_recommend_post_attraction       1.00      1.00      1.00         3
         utter_recommend_price_hotel       1.00      1.00      1.00         3
    utter_recommend_price_restaurant       0.00      0.00      0.00         0
         utter_recommend_stars_hotel       1.00      1.00      1.00         2
     utter_recommend_type_attraction       1.00      1.00      1.00         2
          utter_recommend_type_hotel       1.00      1.00      1.00         1
               utter_reqmore_general       0.89      0.98      0.93       128
       utter_request_area_attraction       1.00      0.83      0.91         6
            utter_request_area_hotel       1.00      0.94      0.97        16
       utter_request_area_restaurant       0.83      0.71      0.77         7
           utter_request_arrive_taxi       1.00      1.00      1.00         7
          utter_request_arrive_train       1.00      1.00      1.00         3
           utter_request_day_booking       1.00      0.73      0.84        11
             utter_request_day_train       0.72      1.00      0.84        13
           utter_request_depart_taxi       1.00      1.00      1.00         2
          utter_request_depart_train       1.00      0.89      0.94         9
             utter_request_dest_taxi       1.00      1.00      1.00         2
            utter_request_dest_train       0.92      1.00      0.96        12
       utter_request_food_restaurant       0.60      0.69      0.64        13
        utter_request_internet_hotel       1.00      1.00      1.00         1
            utter_request_leave_taxi       1.00      0.91      0.95        11
           utter_request_leave_train       0.88      0.94      0.91        16
       utter_request_name_attraction       1.00      1.00      1.00         1
            utter_request_name_hotel       1.00      1.00      1.00         1
       utter_request_name_restaurant       0.33      0.50      0.40         2
         utter_request_parking_hotel       1.00      1.00      1.00         1
        utter_request_people_booking       1.00      0.75      0.86         8
          utter_request_people_train       1.00      1.00      1.00         5
           utter_request_price_hotel       0.80      0.89      0.84         9
      utter_request_price_restaurant       0.70      0.78      0.74         9
           utter_request_stars_hotel       1.00      1.00      1.00         5
          utter_request_stay_booking       0.92      1.00      0.96        12
          utter_request_time_booking       1.00      0.80      0.89         5
       utter_request_type_attraction       0.67      0.89      0.76         9
            utter_request_type_hotel       1.00      1.00      1.00         1
             utter_select_area_hotel       1.00      1.00      1.00         3
        utter_select_area_restaurant       1.00      1.00      1.00         1
             utter_select_attraction       1.00      1.00      1.00         4
      utter_select_choice_restaurant       0.00      0.00      0.00         0
                  utter_select_hotel       1.00      0.50      0.67         2
            utter_select_leave_train       1.00      1.00      1.00         1
            utter_select_price_hotel       1.00      1.00      1.00         1
       utter_select_price_restaurant       0.00      0.00      0.00         1
             utter_select_restaurant       1.00      0.60      0.75         5
            utter_select_stars_hotel       0.00      0.00      0.00         0
                  utter_select_train       1.00      1.00      1.00         1
        utter_select_type_attraction       1.00      1.00      1.00         4
             utter_select_type_hotel       1.00      1.00      1.00         1
               utter_welcome_general       0.78      0.93      0.85        45

### Failure modes

It has not learned to not use the same action twice in a row, but it does get the domain and action type right:

    * chitchat
        - utter_inform_name_restaurant
        - utter_inform_price_restaurant   <!-- predicted: utter_inform_name_restaurant -->

Sometimes it predicts `utter_reqmore_general` instead of `action_listen`:

        - action_listen   <!-- predicted: utter_reqmore_general -->

Occasionally, the bot asks for information that is already known. 
For example, in `story MUL2305` the `request_type` should not be necessary, since the type is known:

    ## story_MUL2305
    * inform{"attraction_type": "entertainment"}
        - slot{"attraction_type": "entertainment"}
        - utter_inform_choice_attraction   <!-- predicted: utter_inform_name_attraction -->
        - utter_request_area_attraction   <!-- predicted: utter_request_type_attraction -->
        - utter_inform_type_attraction
        
If the user starts the conversation with chitchat, then any informative action would be correct. 
This leads to noise:

    ## story_MUL2321
    * chitchat
        - utter_greet_general   <!-- predicted: utter_request_food_restaurant -->
        - utter_request_name_restaurant   <!-- predicted: utter_request_dest_train -->
        
Sometimes the bot is not quite as informative as it was supposed to be, but that is ok, too:

    * inform{"restaurant_name": "maharajah tandoori restaurant"}
        - slot{"restaurant_name": "maharajah tandoori restaurant"}
        - utter_inform_price_restaurant
        - utter_inform_food_restaurant
        - utter_inform_area_restaurant
        - utter_inform_name_restaurant
        - utter_inform_phone_restaurant   <!-- predicted: action_listen -->

Sometimes the bot ends the conversation differently, but perhaps acceptable:

    * bye
        - utter_bye_general
        - utter_welcome_general   <!-- predicted: utter_reqmore_general -->
        
Sometimes the bot tells the user that a place is not available, even though it is. Of course, the bot had no access to the look-up databases. 

    ## story_MUL1045
    * inform{"attraction_type": "nightclub", "attraction_area": "south"}
        - slot{"attraction_area": "south"}
        - slot{"attraction_type": "nightclub"}
        - utter_inform_name_attraction   <!-- predicted: utter_nooffer_addr_attraction -->
        
Sometimes the bot asks very reasonable questions, even though the human didn't:

    ## story_SNG01936
    * inform{"hotel_name": "city centre north b and b"}
        - slot{"hotel_name": "city centre north b and b"}
        - utter_inform_booking   <!-- predicted: utter_inform_people_booking -->
    * inform{"hotel_stay": "5", "hotel_day": "friday", "hotel_people": "1"}
    
There seems to be a somewhat redundant label `recommend` for `inform`:

    ## story_MUL2320
    * inform{"attraction_type": "theatre"}
        - slot{"attraction_type": "theatre"}
        - utter_recommend_name_attraction   <!-- predicted: utter_inform_name_attraction -->
    
Does the action `utter_offerbook_depart_train` exist? What does it mean?

        - utter_offerbook_train   <!-- predicted: utter_offerbook_depart_train -->


### Summary

The most typical mistakes are **repeated actions** and **wrongly predicting or not predicting `action_listen`**.
Overall, except for the two problems just mentioned, the bot **makes reasonable predictions** on the training set.
Therefore, I think that the labeling noise is sufficiently small for it to make sense to train the policy on a larger data set.


## Test set

The situation is different when the trained bot is tested on the test data. 

### Metrics

                                     precision    recall  f1-score   support
    								 
                          micro avg       0.45      0.45      0.45       501
                          macro avg       0.22      0.22      0.21       501
                       weighted avg       0.43      0.45      0.42       501
    				
             action_book_restaurant       0.80      0.80      0.80         5
                   action_book_taxi       0.57      0.57      0.57         7
                  action_book_train       1.00      1.00      1.00         4
                      action_listen       0.67      0.78      0.72       139
             utter_book_day_booking       0.00      0.00      0.00         2
            utter_book_name_booking       0.00      0.00      0.00         2
          utter_book_people_booking       1.00      1.00      1.00         2
             utter_book_ref_booking       0.80      0.80      0.80         5
            utter_book_time_booking       0.25      1.00      0.40         1
                  utter_bye_general       0.79      0.88      0.83        17
                utter_greet_general       0.00      0.00      0.00         8
       utter_inform_addr_attraction       0.29      0.33      0.31         6
            utter_inform_addr_hotel       0.00      0.00      0.00         2
       utter_inform_addr_restaurant       0.00      0.00      0.00         6
       utter_inform_area_attraction       0.20      0.17      0.18         6
            utter_inform_area_hotel       0.00      0.00      0.00         0
       utter_inform_area_restaurant       1.00      0.40      0.57         5
          utter_inform_arrive_train       0.00      0.00      0.00         6
               utter_inform_booking       0.50      0.25      0.33         8
              utter_inform_car_taxi       0.86      0.86      0.86         7
     utter_inform_choice_attraction       0.00      0.00      0.00         5
          utter_inform_choice_hotel       0.67      0.67      0.67         3
     utter_inform_choice_restaurant       0.56      0.50      0.53        10
          utter_inform_choice_train       0.11      0.33      0.17         3
             utter_inform_day_train       0.00      0.00      0.00         1
           utter_inform_depart_taxi       0.00      0.00      0.00         1
          utter_inform_depart_train       0.40      1.00      0.57         2
            utter_inform_dest_train       0.50      0.25      0.33         4
        utter_inform_fee_attraction       0.00      0.00      0.00         6
       utter_inform_food_restaurant       0.10      0.17      0.12         6
              utter_inform_id_train       1.00      0.33      0.50         9
        utter_inform_internet_hotel       0.00      0.00      0.00         0
            utter_inform_leave_taxi       0.00      0.00      0.00         1
           utter_inform_leave_train       0.17      0.14      0.15         7
       utter_inform_name_attraction       0.20      0.25      0.22         8
          utter_inform_name_booking       0.00      0.00      0.00         0
            utter_inform_name_hotel       0.00      0.00      0.00         1
       utter_inform_name_restaurant       0.19      0.50      0.27         6
      utter_inform_phone_attraction       0.00      0.00      0.00         2
           utter_inform_phone_hotel       0.00      0.00      0.00         2
      utter_inform_phone_restaurant       0.00      0.00      0.00         4
            utter_inform_phone_taxi       0.86      0.86      0.86         7
       utter_inform_post_attraction       0.00      0.00      0.00         4
            utter_inform_post_hotel       0.00      0.00      0.00         0
       utter_inform_post_restaurant       0.00      0.00      0.00         4
           utter_inform_price_hotel       0.00      0.00      0.00         1
      utter_inform_price_restaurant       0.20      0.67      0.31         3
           utter_inform_stars_hotel       0.00      0.00      0.00         3
          utter_inform_ticket_train       0.12      0.33      0.18         3
          utter_inform_time_booking       0.00      0.00      0.00         0
            utter_inform_time_train       0.25      0.33      0.29         3
       utter_inform_type_attraction       0.25      0.20      0.22         5
            utter_inform_type_hotel       0.67      0.50      0.57         4
               utter_nobook_booking       1.00      1.00      1.00         1
      utter_nooffer_addr_attraction       0.00      0.00      0.00         0
      utter_nooffer_area_restaurant       0.00      0.00      0.00         1
           utter_nooffer_attraction       0.00      0.00      0.00         1
      utter_nooffer_food_restaurant       0.00      0.00      0.00         3
     utter_nooffer_price_restaurant       0.00      0.00      0.00         1
           utter_nooffer_type_hotel       0.00      0.00      0.00         0
          utter_offerbook_day_train       0.00      0.00      0.00         1
         utter_offerbook_dest_train       0.00      0.00      0.00         1
           utter_offerbook_id_train       0.00      0.00      0.00         1
        utter_offerbook_leave_train       0.00      0.00      0.00         0
              utter_offerbook_train       0.00      0.00      0.00         9
     utter_offerbooked_people_train       0.00      0.00      0.00         1
        utter_offerbooked_ref_train       0.60      0.75      0.67         4
     utter_offerbooked_ticket_train       1.00      0.75      0.86         4
    utter_recommend_area_attraction       0.00      0.00      0.00         1
         utter_recommend_area_hotel       1.00      1.00      1.00         1
    utter_recommend_area_restaurant       0.00      0.00      0.00         0
     utter_recommend_fee_attraction       0.00      0.00      0.00         1
    utter_recommend_food_restaurant       0.00      0.00      0.00         2
     utter_recommend_internet_hotel       0.00      0.00      0.00         1
    utter_recommend_name_attraction       0.67      0.67      0.67         3
         utter_recommend_name_hotel       0.00      0.00      0.00         1
    utter_recommend_name_restaurant       0.67      0.50      0.57         4
      utter_recommend_parking_hotel       0.00      0.00      0.00         0
    utter_recommend_post_attraction       0.00      0.00      0.00         1
        utter_recommend_price_hotel       0.00      0.00      0.00         1
        utter_recommend_stars_hotel       1.00      1.00      1.00         1
    utter_recommend_type_attraction       0.00      0.00      0.00         1
         utter_recommend_type_hotel       0.00      0.00      0.00         1
              utter_reqmore_general       0.24      0.32      0.27        25
      utter_request_area_attraction       0.00      0.00      0.00         1
           utter_request_area_hotel       0.50      0.50      0.50         2
      utter_request_area_restaurant       0.00      0.00      0.00         7
          utter_request_arrive_taxi       0.00      0.00      0.00         1
         utter_request_arrive_train       0.00      0.00      0.00         1
          utter_request_day_booking       0.00      0.00      0.00         2
            utter_request_day_train       0.50      0.50      0.50         2
          utter_request_depart_taxi       0.00      0.00      0.00         3
         utter_request_depart_train       0.50      0.14      0.22         7
            utter_request_dest_taxi       0.50      0.20      0.29         5
           utter_request_dest_train       0.25      0.50      0.33         2
      utter_request_food_restaurant       0.57      0.57      0.57         7
           utter_request_leave_taxi       1.00      0.50      0.67         2
          utter_request_leave_train       0.11      0.25      0.15         4
      utter_request_name_attraction       0.00      0.00      0.00         0
      utter_request_name_restaurant       0.00      0.00      0.00         0
       utter_request_people_booking       0.00      0.00      0.00         3
         utter_request_people_train       0.00      0.00      0.00         0
          utter_request_price_hotel       0.00      0.00      0.00         1
     utter_request_price_restaurant       0.00      0.00      0.00         3
         utter_request_stay_booking       0.00      0.00      0.00         0
         utter_request_time_booking       0.00      0.00      0.00         2
      utter_request_type_attraction       0.00      0.00      0.00         0
            utter_select_attraction       0.00      0.00      0.00         2
                 utter_select_hotel       0.00      0.00      0.00         1
       utter_select_name_restaurant       0.00      0.00      0.00         3
      utter_select_price_restaurant       0.00      0.00      0.00         1
            utter_select_restaurant       0.00      0.00      0.00         2
       utter_select_type_attraction       0.00      0.00      0.00         1
              utter_welcome_general       0.33      0.25      0.29         8
		  
### Failed stories

**All stories in the test set have failed**, and usually every story contains many mistakes.
Take, for example, the first story:

    ## story_PMUL2703
    * inform{"attraction_type": "college", "attraction_area": "centre"}
        - slot{"attraction_area": "centre"}
        - slot{"attraction_type": "college"}
        - utter_inform_choice_attraction   <!-- predicted: utter_nooffer_addr_attraction -->
        - utter_greet_general   <!-- predicted: utter_request_type_attraction -->
        - action_listen   <!-- predicted: utter_request_type_attraction -->
    * chitchat
        - utter_inform_name_attraction
        - utter_reqmore_general   <!-- predicted: utter_inform_addr_attraction -->
        - utter_inform_post_attraction   <!-- predicted: utter_inform_addr_attraction -->
        - utter_inform_addr_attraction
    * chitchat
        - utter_inform_fee_attraction   <!-- predicted: utter_inform_name_attraction -->
    * inform{"hotel_name": "express by holiday inn cambridge"}
        - slot{"hotel_name": "express by holiday inn cambridge"}
        - utter_inform_addr_hotel   <!-- predicted: utter_inform_stars_hotel -->
        - utter_inform_booking   <!-- predicted: utter_inform_area_hotel -->
    * chitchat
        - utter_inform_stars_hotel   <!-- predicted: utter_reqmore_general -->
        - utter_inform_type_hotel   <!-- predicted: action_listen -->
    * bye
        - utter_inform_type_attraction   <!-- predicted: utter_bye_general -->

First, the bot says the place's address is not available, even though it is. 
This is not surprising, because the bot does not have access to the databases. 
Then, the **bot asks for the type of attraction, even though the user just declared the type**. 
This is not good, and we already saw this in the test with the training set.
Also, as we have also seen in the training set, the bot predicts `utter_request_type_attraction` instead of `action_listen`.
The bot goes on to **reply twice with the same action** (`utter_inform_addr_attraction`) to chit chat, which is also bad. 
After another chit chat from the user, the bot predicts `utter_inform_name_attraction` instead of `utter_inform_fee_attraction`, which is reasonable.
Another set of reasonable but false replies happen immediately afterwards. 

This particular story contains a lot of chitchat, so perhaps it is not the best example.
Thus, here is another example story with fewer chitchat.

    ## story_PMUL0745
    * chitchat
        - utter_request_food_restaurant
        - action_listen   <!-- predicted: utter_request_name_restaurant -->
    * inform{"restaurant_food": "italian"}
        - slot{"restaurant_food": "italian"}
        - utter_request_price_restaurant   <!-- predicted: utter_request_area_restaurant -->
        - utter_inform_food_restaurant   <!-- predicted: action_listen -->
        - utter_request_area_restaurant   <!-- predicted: utter_request_price_restaurant -->
        - utter_inform_choice_restaurant   <!-- predicted: action_listen -->
    * inform{"restaurant_pricerange": "moderate", "restaurant_area": "south"}
        - slot{"restaurant_area": "south"}
        - slot{"restaurant_pricerange": "moderate"}
        - utter_inform_addr_restaurant   <!-- predicted: utter_inform_name_restaurant -->
        - utter_inform_choice_restaurant   <!-- predicted: utter_inform_food_restaurant -->
        - utter_inform_price_restaurant   <!-- predicted: action_listen -->
        - utter_inform_name_restaurant   <!-- predicted: action_listen -->
    * inform{"restaurant_people": "7", "restaurant_day": "friday", "restaurant_time": "19:30", "restaurant_name": "pizza hut cherry hinton"}
        - slot{"restaurant_day": "friday"}
        - slot{"restaurant_name": "pizza hut cherry hinton"}
        - slot{"restaurant_people": "7"}
        - slot{"restaurant_time": "19:30"}
        - action_book_restaurant   <!-- predicted: utter_request_time_booking -->
        - slot{"restaurant_name": "pizza hut cherry hinton"}
        - slot{"restaurant_reference": "JUMD2Q6K"}
        - utter_book_ref_booking
        - utter_reqmore_general
        - action_listen   <!-- predicted: utter_book_time_booking -->
    * inform{"train_destination": "cambridge", "train_arriveBy": "12:00"}
        - slot{"train_arriveBy": "12:00"}
        - slot{"train_destination": "cambridge"}
        - utter_request_day_train
        - utter_request_depart_train   <!-- predicted: action_listen -->
    * inform{"train_day": "friday", "train_departure": "kings lynn"}
        - slot{"train_day": "friday"}
        - slot{"train_departure": "kings lynn"}
        - utter_offerbook_train   <!-- predicted: utter_request_leave_train -->
        - utter_inform_id_train   <!-- predicted: utter_inform_arrive_train -->
        - action_listen   <!-- predicted: utter_inform_ticket_train -->
    * inform{"train_people": "9"}
        - slot{"train_people": "9"}
        - action_book_train
        - slot{"train_trainID": "TR9102"}
        - slot{"train_reference": "YTTF2L2U"}
        - utter_offerbooked_ticket_train   <!-- predicted: utter_offerbooked_ref_train -->
        - utter_offerbooked_ref_train   <!-- predicted: utter_reqmore_general -->
    * bye
        - utter_bye_general

We can safely ignore the mistake after the uninformative utterance of the user (chitchat).
Then the bot swaps the questions about area and price, which is ok, but then **predicts `action_listen` twice**, instead of informing the user about `food` and `choice`.
After the user specified the price and location, the bot wrongly suggests a restaurant name and food-type (that's ok), but then predicts `action_listen` twice again.
The user fills in a lot of slots, but the **bot asks for a slot that was already given** (`utter_request_time_booking`).
The remaining mistakes are similar to those already mentioned.

Other stories look similar to this one, and I have not seen other types of mistakes. 
We can hope that increasing the size of the training data set may help.


## Comparison with LSTM policy

I trained the LSTM policy on the same data set of 80 stories.
The LSTM's scores are actually better than the transformer scores for the training set, but the transformer policy seems to generalize better, as its f1-score for the test set is higher.

Training set, LSTM:

                                     precision    recall  f1-score   support
                       micro avg       0.95      0.95      0.95      2166
                       macro avg       0.91      0.88      0.89      2166
                    weighted avg       0.95      0.95      0.95      2166

Training set, Transformer:

                                     precision    recall  f1-score   support
                       micro avg       0.93      0.93      0.93      2166
                       macro avg       0.88      0.86      0.87      2166
                    weighted avg       0.94      0.93      0.93      2166

Test set, LSTM:

                                     precision    recall  f1-score   support
                      micro avg       0.40      0.40      0.40       501
                      macro avg       0.22      0.23      0.21       501
                   weighted avg       0.37      0.40      0.38       501

Test set, Transformer:

                                     precision    recall  f1-score   support
                      micro avg       0.45      0.45      0.45       501
                      macro avg       0.22      0.22      0.21       501
                   weighted avg       0.43      0.45      0.42       501
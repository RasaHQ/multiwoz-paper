## dlg-1e291047-1d99-4590-b96b-eb154b1b8b26
* Hey i need tickets to the _name.movie_
    - okay i can do that
* alright
    - for when
* the opening at _time.start_
    - looks like they are booked
* okay how about _name.movie_ _time.start_?
    - general: for when   <!-- predicted: auto_repair.auto_repair: Okay, please wait a moment while I check _auto_repair.auto_repair_ times. -->
* _time.start_
    - movie_ticket.time.start: theyre booked all _time.start_   <!-- predicted: movie_ticket.time.start_movie_ticket.time.start.reject: Okay , they have tickets available _time.start_ , and _time.start_. -->
* oh alright
    - general: any other movies   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.type.seating.accept: Ok it looks like they have have that time slot available _type.seating_ at _name.restaurant_ I will reserve that time slot. -->
* how about _time.start_?
    - let me check
* okay
    - looks like they are booked
* dang nevermind then
    - okay no ticket?
* no
    - okay
* thanks
    - no problem


## dlg-1e304262-fd39-46b7-92b8-d1161510055c
* Hello, can I get a _name.drink_ with _coffee_ordering.preference_.
    - general: Sure. What location are you ordering to?   <!-- predicted: coffee_ordering.name.drink: Sure, they have _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, and _name.drink_. -->
* To the Starbucks on _location.store_.
    - coffee_ordering.name.drink: OK, very good. What size would you like for your _name.drink_?   <!-- predicted: general: I agree. What should I order? -->
* Id like a _size.drink_.
    - coffee_ordering.name.drink_coffee_ordering.name.drink.accept_coffee_ordering.size.drink.accept: _name.drink_size.drink_. Is that a _name.drink_?   <!-- predicted: coffee_ordering.type.milk: What kind of creamer? Theyve got _type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_. -->
* Yes, thats right.
    - coffee_ordering.preference: Great. Would you like _coffee_ordering.preference_?   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* Let me ask my friend, because its for her. Hold on a moment?
    - Sure, no problem.
* OK, she does want _coffee_ordering.preference_.
    - general: OK, got it.   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* _preference.accept_coffee_ordering.preference_ though?
    - coffee_ordering.preference.accept: _preference.accept_, absolutely. Anything else?   <!-- predicted: general: I hear you.. is there something else youd like? -->
* No, I think that will do it.
    - OK then, your order will be ready in _number_ minutes.
* Great, thank you.
    - And the receipt has already been sent to your phone.n
* Perfect, thanks. Oh, before I forget could I get an extra straw with that?
    - Absolutely. Thanks again and have a good day.


## dlg-1e379d6d-2924-4447-babd-fb564db3c9a2
* Hello, I would like to order a _pizza_ordering.pizza_ordering_name.store_location.store_.
    - general: Okay, I would be happy to assist you. Is this for today?   <!-- predicted: pizza_ordering.type.topping.reject: Ok, please give me a moment while I confirm the details of your order. Im sorry, the restaurant is out of _type.topping_. -->
* Yes, I would like to order for right now.
    - general: Okay, what would you like?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* I want a _size.pizza_ pizza.
    - pizza_ordering.size.pizza: Okay, got it, a _size.pizza_ pizza. What toppings would you like?   <!-- predicted: general: What toppings would you like? -->
* I think Ill just have _type.topping_ and _type.topping_.
    - Okay, anything else to add?
* _type.topping_pizza_ordering.preference_.
    - pizza_ordering.preference_pizza_ordering.size.pizza_pizza_ordering.type.topping: Okay, so one _size.pizza_ pizza with _type.topping_ and _type.topping_pizza_ordering.preference_type.topping_. Is that okay?   <!-- predicted: pizza_ordering.preference.reject_pizza_ordering.type.topping: _type.topping_preference.reject_ on the crust. -->
* Yes, thats great.
    - pizza_ordering.location.store_pizza_ordering.name.store_pizza_ordering.type.topping.reject: _location.store_name.store_ is all out of _._type.topping_   <!-- predicted: general: Okay the total will be _price_ and itll be ready for pickup in _number_ minutes. -->
* Oh thats too bad. Well in that case Ill order a _size.pizza_ _name.pizza_.
    - pizza_ordering.name.pizza_pizza_ordering.size.pizza_pizza_ordering.type.topping.accept: Okay, one _size.pizza_name.pizza_size.pizza_ with _type.topping_, _type.topping_ and bacon. Is that correct?   <!-- predicted: general: okay good choice i will text you the payment -->
* Yes, that will be fine.
    - pizza_ordering.name.pizza.accept_pizza_ordering.name.store.accept_pizza_ordering.size.pizza.accept: Okay, let me put that through. Okay, I have confirmed your order for one _size.pizza_ _name.pizza_ from _name.store_ I will send the receipt to your mobile device via text message.   <!-- predicted: general: Okay. The total of the order comes to _price_ Is there anything else you would like to add? -->
* Sounds great. When will it be ready?
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ It has been a pleasure serving you.   <!-- predicted: general: The fried calamari is _price_ and the _number_ buffalo wings are _price_ making your total so far _price_ before tax. -->
* Thank you.
    - Youre welcome, have a great day.
* You too.
    - general: Thank you. Good bye.   <!-- predicted: action_listen: action_listen -->


## dlg-1e3cf921-e2d0-4c36-a639-4c3e3778cd9a
* Hi! I need to order a standard car from Lyft.
    - Where is the pick-up point?
* _location.from_
    - And where do you need to go?
* My drop off will be _location.to_.
    - general: How long are you able to wait?   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* I have an important meeting this afternoon. I need a ride within the next _time.pickup_.
    - general: Let me see what is available.   <!-- predicted: uber_lyft.duration.estimate_uber_lyft.price.estimate.accept_uber_lyft.time.pickup_uber_lyft.type.ride: Ok. I am looking it up now. Ok. There is an suv driver or _type.ride_ available for $_price.estimate_duration.estimate_time.pickup_ -->
* I am awaiting your response.
    - uber_lyft.location.from_uber_lyft.location.to_uber_lyft.time.pickup.accept_uber_lyft.time.pickup.reject_uber_lyft.type.ride: There are currently no _type.ride_location.to_location.from_ within _time.pickup_   <!-- predicted: general: Your drivers name is Derek and his plate number is . -->
* Are there other vehicle types available?
    - uber_lyft.type.ride_uber_lyft.type.ride.accept: Yes, I could order you a _type.ride_.   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* What the cost?
    - uber_lyft.price.estimate_uber_lyft.price.estimate.accept: Currently the anticipated cost is between _price.estimate_ total.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Thats not too bad. Go ahead and order the _type.ride_.
    - uber_lyft.location.from_uber_lyft.time.pickup_uber_lyft.type.ride.accept: Place an order for a _type.ride_ ride at _location.from_ Anticipated wait time is less than _time.pickup_.   <!-- predicted: uber_lyft.time.pickup: Ok. So _time.pickup_ -->
* Thank you so much.
    - uber_lyft.location.from.accept: Your ride is on its way to _location.from_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Ill be here.
    - Details of this transaction have been sent to your mobile phone.


## dlg-1e3f4ef9-bb49-4740-a0d0-30486d43c5b0
* Hello! I would like to book a dinner _restaurant_reservation.restaurant_reservation_ for this Friday _time.reservation_.
    - Sure, which restaurant would you like to dine at?
* I would like to go to _name.restaurant_.
    - How many people will be attending?
* We will need a table for _num.guests_, preferably _type.seating_. It is supposed to be a nice evening.
    - restaurant_reservation.restaurant_reservation: What time would you like the _restaurant_reservation.restaurant_reservation_ for?   <!-- predicted: general: What time are you looking for? -->
* I would like a _time.reservation_ reservation.
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests_restaurant_reservation.restaurant_reservation_restaurant_reservation.time.reservation_restaurant_reservation.type.seating: Ok, I will check on a _restaurant_reservation.restaurant_reservation_ for a party of _num.guests_ at _time.reservation_ _type.seating_ at _name.restaurant_.   <!-- predicted: general: Sorry, there are no openings for that time. -->
* yes please, for this Friday evening.
    - restaurant_reservation.name.restaurant_restaurant_reservation.restaurant_reservation_restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: Im sorry, they do not have any seating available _type.seating_ at all, and there are no _restaurant_reservation.restaurant_reservation_ available at _name.restaurant_ for _time.reservation_.   <!-- predicted: restaurant_reservation.num.guests_restaurant_reservation.time.reservation: Yes sir. I see they have a table open tomorrow at _time.reservation_ but its only for _num.guests_ -->
* Thats too bad!
    - general: Would you like to try another restaurant?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Hmm I meant _time.reservation_, not _time.reservation_... can you do _number_ instead? -->
* How about _name.restaurant_? A table for _num.guests_ _type.seating_ at _time.reservation_.
    - general: Yes, I will check. Still for this Friday evening?   <!-- predicted: restaurant_reservation.type.seating: Okay, well I just checked  they said the _type.seating_ is first come, first served only. -->
* Yes, same date and time.
    - restaurant_reservation.num.guests_restaurant_reservation.restaurant_reservation_restaurant_reservation.time.reservation: Im sorry. They do not have any _restaurant_reservation.restaurant_reservation_ available for that time. The only reservation for a party of _num.guests_ is at _time.reservation_.   <!-- predicted: general: Okay. It looks like you can choose the general area you can sit. Were you looking for a seat near the front, middle, or back? -->
* No, that will be too late for us.
    - general: Would you like to try another restaurant.   <!-- predicted: restaurant_reservation.reservation.accept: Okay, _reservation.accept_, sir. -->
* No, we will make plans for another evening at a later date.
    - Im sorry I could not help you today.
* Thats okay, must be a busy evening everywhere this Friday!
    - Have a good day!


## dlg-1e437066-40e0-4738-abde-37628a40e757
* I would like to book reservation for _name.restaurant_ on Wednesday.
    - Ok what time? How many people?
* _time.reservation_., _num.guests_ people.
    - general: Is there a specific seating your prefer?   <!-- predicted: restaurant_reservation.time.reservation: Okay great we have the option for a bottle of wine or roses at longhorns and availability at _time.reservation_ and a _price_ charge for wine or roses. -->
* Id like a _type.seating_
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating.reject: They dont have any _type.seating_ available at _time.reservation_.   <!-- predicted: general: Any special diet restriction? -->
* oh really what about at _time.reservation_ or _time.reservation_
    - general: No they dont have that either do you want to try a different restaurant.   <!-- predicted: restaurant_reservation.time.reservation: They do, they have one at _time.reservation_ and one at _time.reservation_. -->
* Yes lets try _name.restaurant_
    - Ok Ill give it a try.
* Thank You
    - youre welcome
* so what is it looking like
    - restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: _name.reservation_name.restaurant_ has a _type.seating_ avaialble for _time.reservation_   <!-- predicted: general: No thankyou. -->
* Its that the only thing they have that would be convenient for me
    - No, should I book it
* Yes go ahead
    - restaurant_reservation.reservation.accept: _reservation.accept_   <!-- predicted: general: You driver is drving a silver Toyota Camry and will be there in two minutes. -->
* I appreciate it.
    - Im glad I could help is their anything else you need?
* No
    - action_listen: action_listen   <!-- predicted: general: thank you for using chat bot -->


## dlg-1e4ddfd6-381a-4681-b516-0d202329181c
* Hey Sue. Can you make a reservation for _num.guests_ at the _name.restaurant_ restaurant for this Friday night the _number_th at _time.reservation_. Also we want _type.seating_ seating. Its going to be beautiful out.
    - Sure, no problem. Which one ?
* The one on _location.restaurant_
    - OK. Anything else you want ?
* No. That should do it. Thanks !
    - general: OK. I will call right now.   <!-- predicted: restaurant_reservation.name.restaurant.accept: Certainly! We have the _name.restaurant_ that serves amazing variety. They stand out for their great Mexican dishes and fine beer. -->
* Thanks so much Sue !!!
    - restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating.reject: I called. They do not have _time.reservation_ available. And they dont have _type.seating_ seating available.   <!-- predicted: restaurant_reservation.reservation.accept: Okay, _reservation.accept_, sir. -->
* OK. Please try the same for the _name.restaurant_.
    - restaurant_reservation.time.reservation_restaurant_reservation.type.seating: OK. I will. Still _time.reservation_ with _type.seating_ seating ?   <!-- predicted: general: Any special diet restriction? -->
* Yes please. Thanks !
    - general: You are welcome. I will give them a call now.   <!-- predicted: restaurant_reservation.reservation.accept: Okay, _reservation.accept_, sir. -->
* Thanks so much again !
    - restaurant_reservation.time.reservation_restaurant_reservation.type.seating.reject: So they have _time.reservation_ available, but not for _type.seating_ seating.   <!-- predicted: general: No problem! Enjoy your evening. -->
* Oh my gosh. Everyone must be taking advantage of this Fridays good weather.
    - Yes, I suppose so. What would you like me to do ?
* I am going to have to say no to both of them and just cancel.
    - OK. I wont book anything then.
* Sorry for your trouble Sue.
    - Its not problem. Thats why I am here.
* Thanks again !!!
    - action_listen: action_listen   <!-- predicted: general: Bye see you tomorrow -->


## dlg-1e65668f-cc8c-4e12-a587-732f5139da62
* Hello, Im in the mood for pizza for dinner tonight, would you mind placing an order with _name.store_ for me?
    - Pizza for dinner sounds great! I would be happy to place your order!
* Great! I will definitely need a _size.pizza_. Im thinking _type.topping_ and _type.topping_ would be perfect.
    - pizza_ordering.size.pizza_pizza_ordering.type.topping: Ok so that is one _size.pizza_ pizza with _type.topping_ and _type.topping_ is that correct?   <!-- predicted: general: Great. What toppings would you like on the first pizza? -->
* Yep, thats it!
    - general: Is there anything else you would like for me to order?   <!-- predicted: pizza_ordering.location.store_pizza_ordering.name.store_pizza_ordering.type.topping.reject: _name.store_location.store_ is out of _. Would yo_type.topping_to change your order? -->
* No, I think thats going to be all for today.
    - I will get your order placed right now and be back with you in just a minute.
* Thank you!
    - pizza_ordering.type.topping_pizza_ordering.type.topping.reject: You are very welcome! Unfortunately they are out of _type.topping_ at the moment. Is there something else you would be interested in along with the _type.topping_?   <!-- predicted: general: Was there anything else I can do for you? -->
* I guess I will do _type.topping_ instead.
    - pizza_ordering.size.pizza_pizza_ordering.type.topping: Ok so thats one _size.pizza_ _type.topping_ and _type.topping_ pizza, is that correct?   <!-- predicted: general: Okay, Ill put you on hold for a moment while I call and order. -->
* Yes, thats correct.
    - pizza_ordering.name.store.accept_pizza_ordering.pizza_order.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Great! _pizza_order.accept_ for one _size.pizza_ _type.topping_ and _type.topping_ pizza from _name.store_.   <!-- predicted: general: Awesome! It will be _price_ total. -->
* Thank you!
    - You are very welcome! They have already billed your account and you will receive a text message shortly via your mobile device confirming your order and payment.
* Thank you so much!
    - You are very welcome! Your pizza will be ready for pickup in about _number_ minutes. Is there anything else I can do for you today?
* No, I believe thats all for now. Thank you for your help.
    - It was my pleasure! I hope you have a great evening and enjoy your pizza!
* Thank you, I hope you have a great evening as well. Goodbye.
    - Goodbye.


## dlg-1e65945b-a202-419d-ae56-3555cab52a8d
* I would like to see _name.movie_
    - Where would you like to see the movie?
* _location.theater_name.theater_.
    - OK, what day and time?
* I want to see it on Friday around _time.start_.
    - movie_ticket.location.theater.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept_movie_ticket.type.screening.accept: There is one showing in _type.screening_ at _time.start_name.theater_location.theater_   <!-- predicted: general: Okay, let me check ticket availability for that showing. -->
* OK, please book that showing.
    - general: Yes, of course, how many tickets do you need?   <!-- predicted: movie_ticket.time.start_movie_ticket.time.start.reject: Okay , they have tickets available _time.start_ , and _time.start_. -->
* I need _num.tickets_ tickets please.
    - What are the ages of the ticket holders?
* _num.tickets_, age _number_
    - movie_ticket.num.tickets.accept: OK, I will purchase _num.tickets_.   <!-- predicted: general: Do you need any accessibility devices tonight? -->
* thank you.
    - general: How would you like to receive your tickets?   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* What are my options?
    - general: You can have them emailed, texted or willcall.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* I would like them texted to my cell phone.
    - OK, tickets are being text now.
* Thank you.
    - Is there anything else I can assist you with?
* No thank you.
    - action_listen: action_listen   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->


## dlg-1e8d0ad2-d95a-4b85-b8a3-39d2f95e544f
* I need a car
    - Where are you?
* Im at _location.from_time.pickup_
    - Where to?
* To _location.to_time.dropoff_time.pickup_
    - How many passengers?
* _num.people_
    - uber_lyft.type.ride: Will that be _type.ride_ or _type.ride_?   <!-- predicted: general: Uber offers a couple options, do you have a preference? -->
* _type.ride_ is fine
    - Okay let me put that in for you
* Okay great,
    - uber_lyft.price.estimate.accept: Ive found a car, it should be _price.estimate_   <!-- predicted: general: Do you want me to arrange the Uber then? -->
* Thanks how long
    - uber_lyft.duration.estimate.accept_uber_lyft.time.pickup.accept: _duration.estimate_time.pickup_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Thanks for that
    - Ive also sent a conformation over to your phone.
* Just got it, appreciate that
    - general: No worries, enjoy your ride   <!-- predicted: uber_lyft.ride_booking.accept_uber_lyft.time.pickup.accept: Lets see, I just sent the payment through and...Itll be a black _number_ Toyota Camry. _ride_booking.accept_ _time.pickup_. -->
* Will do!
    - action_listen: action_listen   <!-- predicted: general: no i have all your information here. -->


## dlg-1b083c71-f098-4145-99ec-01df18700650
* I need to make a dinner reservation.
    - restaurant_reservation.time.reservation: For _time.reservation_?   <!-- predicted: general: Do you already know where you want to eat? -->
* Yes.
    - For where?
* _name.restaurant_.
    - Ok. How man people will be attending you?
* _num.guests_. I also need a _type.seating_.
    - restaurant_reservation.type.seating.reject: This establishment does not have _type.seating_   <!-- predicted: general: Okay -->
* Darn. Ok, I will just bring one, I guess.
    - What time were you thinking?
* _time.reservation_. is fine.
    - general: They dont have anything available for you after that time.   <!-- predicted: restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Okay, they have a _type.seating_ tomorrow at _time.reservation_. _reservation.accept_ -->
* ERRR. Well then how about _name.restaurant_
    - restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating: I see they do have _type.seating_ available but no opens _time.reservation_   <!-- predicted: general: Yes, that is possible. -->
* This really sucks.
    - This certainly is unfortunate.
* Forget it. I dont think I want to make a reservation anymore.
    - Not anywhere?
* No.
    - general: Well ok.   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_ -->


## dlg-1e8f0aa4-b796-4d1b-af78-a4b62cc4154f
* Hi, can you buy me tickets for the movie _name.movie_
    - movie_ticket.name.movie.accept: _name.movie_, where do you live   <!-- predicted: general: Hi! What kind of movie do you like to watch? -->
* Kennett Square
    - What State is that in?
* Pennsylvania
    - Zip code?
* _number_
    - movie_ticket.location.theater_movie_ticket.location.theater.accept_movie_ticket.name.theater.accept: _location.theater_name.theater_, is that ok?   <!-- predicted: general: What showing would you like to see? -->
* _location.theater_!
    - movie_ticket.name.movie.accept_movie_ticket.time.start_movie_ticket.time.start.accept_movie_ticket.time.start.reject: The available movies time for _name.movie_ are, _time.start_ which one do you want tickets for?   <!-- predicted: general: When do you want to see it? -->
* How about the _time.start_
    - movie_ticket.price.ticket: The tickets are _price.ticket_or adults and _number_ for kids, how many of each would you like?   <!-- predicted: general: Is your friend an adult or senior? In case they have a senior discount. -->
* _num.tickets_ for adults please.
    - Your total is _number_, would you like me to charge the card you have on file?
* Thats fine
    - The card is ending in XXXX, would you like to confirm?
* Yes
    - Would you like a receipt with your purchase?
* No thats fine.
    - Great, your tickets will be sent to your phone via text message!
* Thanks!
    - action_listen: action_listen   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->


## dlg-1e954022-dafa-4290-bc19-13749c30b5df
* I am in dire need of a car appointment !!
    - Okay, that is fine I can set that up for you
* Thank you i need it badly
    - auto_repair.name.store_auto_repair.name.store.accept: I can set it up with you at _name.store_   <!-- predicted: general: I can certainly help you with that. What sort of car are you interested in? -->
* Yes that would work just fine for me
    - Okay great i just need a few details about your
* what do you need for details
    - general: what is the make and model and year of your car   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* _name.vehicle_ _year.vehicle_ BLACK
    - general: what seems to be the issue with your car?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* my car has a _reason.appt_
    - okay ill contact them and let them know
* okay great
    - general: what is the name and number you want under   <!-- predicted: auto_repair.time.appt: Upon checking, it looks like _time.appt_ is available. Is _number_ a.m. okay? -->
* _name.customer_ (_number_-_number_-_number_)
    - general: Okay great, Ill call them and let them know   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* great
    - what time works for you
* _date.appt_time.appt_
    - general: Ill call and ask   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* great
    - auto_repair.time.appt.accept: the time for your appointment is _time.appt_   <!-- predicted: auto_repair.time.appt: Upon checking, it looks like _time.appt_ is available. Is _number_ a.m. okay? -->
* thank you
    - action_listen: action_listen   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->


## dlg-1ebfb30b-3599-4698-93de-1e51a1d69884
* Hi, Id like to order a pizza please!
    - Yes sure, what would you like to order ?
* Can I have a _size.pizza_, _type.crust_ with _pizza_ordering.preference_ to start with?
    - general: Not a problem, any sauce would you like to add ?   <!-- predicted: pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Yes, so you want a _size.pizza_ instead of _size.pizza_? -->
* Can I have a _pizza_ordering.preference_ please ?
    - Ok, how much sauce do you want ?
* Just a little is fine.
    - How many toppings you would like to add ?
* May I have two please?
    - Of course, what would you want them to be ?
* Can I have a topping of _type.topping_ and _type.topping_.
    - pizza_ordering.type.topping.reject: Unfortunately, we ran out of our _type.topping_ for today, can I get you something else instead ?   <!-- predicted: general: Sure, anything else? -->
* _type.topping_pizza_ordering.preference_ instead.
    - Yes sure, do you want to add any veggies ?
* What options do I have ?
    - pizza_ordering.type.topping: We have _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, and _type.topping_   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* Ill pick _type.topping_, and _type.topping_ please.
    - pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping.accept: Alright, so your order would be a _size.pizza_, _type.crust_ with _preference.accept_ with toppings of _type.topping_ and _type.topping_, your choices of veggies are _type.topping_, and _type.topping_. Would that be all ?   <!-- predicted: general: Would you like something else instead? -->
* Yes, thatd be all for today.
    - Great, your pizza will be ready for pickup in approximately _number_ minutes. Your receipt number is _number_ and it will be sent to your phone.
* Thank you, have a good one.
    - Thank you, bye.


## dlg-1ecb4883-8606-4ead-b426-9f90658dd402
* Hey Buddy. I need to ask you to do something for me this morning.
    - Alright, what that?
* Could you go on-line and order a _coffee_ordering.coffee_ordering_ for me?
    - coffee_ordering.coffee_ordering: Sure thing. Who did you want the _coffee_ordering.coffee_ordering_ from.   <!-- predicted: general: Hello Id be happy to do that. What location would you like me to order from? -->
* Id like try _coffee_ordering.coffee_ordering_. _location.store_
    - general: Okay. What should I order for you?   <!-- predicted: coffee_ordering.name.drink: Alright, thats simple enough. You said you wanted a _name.drink_? -->
* Ive heard a lot about their _name.drink_ so go ahead and order that for me.
    - coffee_ordering.size.drink: Alright, what size, _size.drink_?   <!-- predicted: general: Im not sure, let me finish entering the details and Im sure I can let you know. -->
* Just a _size.drink_. _coffee_ordering.preference_ _preference.accept_
    - Got it. Anything else?
* Yeah, definitely use _type.milk_. I know its more calories but you only live once, right?
    - general: I agree. When did you want to pick it up?   <!-- predicted: coffee_ordering.size.drink: Good choice, shall we stick with _size.drink_? -->
* In about _number_ minutes. Im heading out the door now and thats about how long itll take before I get there.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Let me double check. You want the _name.drink_, _size.drink_ size, _preference.accept_ and youll be there in about _number_ minutes.   <!-- predicted: general: thank you so much i am going to text you all the info and the directions to the shop i hope it all gets fixed up -->
* Thats all correct.
    - Okay. It should be there ready for you.
* Cool. Thanks for your help. Go ahead and order _num.drink_ for yourself if youd like, on me. Ill bring it in to work when I come.
    - Thanks Ill see you a little later.
* Okay, see you later.
    - Bye.


## dlg-1ed24ab9-1619-4bc2-8d75-89b7d20dfa1d
* Hey, Assistant. I need a Lyft across town.
    - Okay, where are you?
* Im at _location.from_.
    - general: Where are you headed?   <!-- predicted: uber_lyft.location.from: OK, your pick up location is _location.from_ Where are you going? -->
* I need to get _location.to_.
    - general: Okay, what type of Lyft would you like?   <!-- predicted: uber_lyft.location.to: Should I go ahead and set up the car ride _location.to_ right now? -->
* Id like a _type.ride_.
    - uber_lyft.time.pickup_uber_lyft.type.ride: Okay, a _type.ride_ has a wait time of _time.pickup_ Is this okay?   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* No.
    - uber_lyft.type.ride: Would you like an _type.ride_ car type?   <!-- predicted: general: What is the minimum star rating would you like? -->
* Sure, Ill take an _type.ride_.
    - uber_lyft.price.estimate_uber_lyft.time.pickup_uber_lyft.type.ride: Okay, an _type.ride_ has a wait time of _time.pickup_ and will cost _price.estimate_. Is this okay?   <!-- predicted: general: Which Uber service do you prefer? -->
* No, thats still too long.
    - uber_lyft.type.ride: Okay, would you like a _type.ride_?   <!-- predicted: general: Your drivers name is Derek and his plate number is . -->
* Yes.
    - uber_lyft.price.estimate.accept_uber_lyft.time.pickup.accept_uber_lyft.type.ride.accept: Okay, a _type.ride_ car has a wait time of _time.pickup_ and costs _price.estimate_ Is this okay?   <!-- predicted: general: you can check further details and track the arrival via the app on your phone -->
* Yes.
    - uber_lyft.ride_booking.accept_uber_lyft.type.ride: _ride_booking.accept_.  You may check the status of it on your phone.  Would you like to reserve anothe_type.ride_ft?   <!-- predicted: general: you can check further details and track the arrival via the app on your phone -->
* No, thanks.
    - No problem.


## dlg-1ed3e401-9210-45c1-82ad-982f55247000
* AI can you call _name.store_ on _location.store_?
    - I can do that; I have connected with the store.
* AI I would like a _name.pizza_. How much is it?
    - pizza_ordering.name.pizza: A _name.pizza_ is _price_; should I order it?   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* Yes please order one.
    - pizza_ordering.name.pizza: I have one _name.pizza_.   <!-- predicted: pizza_ordering.pizza_ordering: What type of _pizza_ordering.pizza_ordering_ do you want to order? -->
* AI could you see if they have Caesar Wings?
    - I can check please standby; they have them and they are _price_
* Good I will take a order of Caesar wings also.
    - pizza_ordering.name.pizza: I have one _name.pizza_ and one order of Caesar wings is there anything else?   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.reject: _coffee_ordering.preference_preference.reject_ available. Would you like to remove it or choose something else? -->
* AI please order one _number_-liter bottle of Pepsi.
    - pizza_ordering.name.pizza: I have one _number_-liter bottle of Pepsi, one _name.pizza_ and one order of Caesar wings; Is there anything else?   <!-- predicted: general: Your total will be _price_ and your receipt will be texted to you. -->
* AI can I get a subtotal on that order.
    - general: Yes, your subtotal is _price_   <!-- predicted: pizza_ordering.name.pizza_pizza_ordering.type.topping: Yes, I can order you a _name.pizza_ with _type.topping_ as your topping. Would you like anything else on top of the pizza? -->
* AI can you add one bottle of water and give a new subtotal?
    - One bottle of water has been added and the new subtotal is _price_
* AI could you checkout and give me the total.
    - pizza_ordering.name.pizza.accept: Yes, I have one _name.pizza_, one order of Caesar wings, one _number_-liter Pepsi and one bottle of water with a total of _price_   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Good you may place the order and standby for delivery instructions.
    - Order has been placed and I am ready to receive delivery instructions.
* AI have pizza delivered to _number_ Main St. Fresno, Ca _number_
    - I have the delivery address is there anything else?
* Yes, add a note to ask for Sam when the delivery is made.
    - I have noted to ask for Sam when deliver is made to _number_ Main St. Fresno, Ca. _number_
* Good; that is all you make disconnect.
    - Order has been placed and disconnecting and finalizing communications. I am out.


## dlg-1ed45bf4-7263-4be8-960b-33dbb394aed6
* I have you heard anything about the _name.drink_ at starbucks?
    - coffee_ordering.location.store.accept: Yes I have would you like me to order you one theres _location.store_   <!-- predicted: general: Yea sure can. -->
* Yes I would I need to pick it up and deliver to the office please
    - Why certainly thats my entire existence has to serve you
* How do I get paid the big bucks
    - Ill need to know the size please any other details you need taken care of with this order
* _size.drink_name.drink_
    - general: Very well is that just for you or do you care about other people in your office   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.accept: _coffee_ordering.preference_preference.accept_? -->
* No actually I dont care about them at all just send me _num.drink_
    - That is as I suspected
* That great so how long will it be
    - Im going to put the order in now
* Give me an update on my order please
    - coffee_ordering.coffee_order.reject: This is outstanding your order will be ready in _number_ minutes _coffee_order.reject_   <!-- predicted: general: Here Ill turn up the volume so you can hear yourself. Ask something. -->
* Thats great appreciate the effort of not Valerian like you said youre going to
    - I aim to please
* Night while you have a good day and I will not see you at the office tomorrow
    - Awesome place while I hope you have a good day to you sir
* Bye
    - general: Bye-bye   <!-- predicted: action_listen: action_listen -->


## dlg-1ee019eb-e14b-42cd-9835-f6c40537147e
* tom i really need your help buddy
    - auto_repair.name.customer: hey _name.customer_ whats wrong?   <!-- predicted: general: Sure thing. From where to where? -->
* so i am driving down the I-_number_ and _reason.appt_.
    - oh wow i think i can hear it over the call. what do you need me to do?
* i need you to get with my car guy. he works at _name.store_.
    - ok sure i can do that. how bad is it?
* its pretty bad _reason.appt_
    - what kind of car is it?
* its a _year.vehicle_ _name.vehicle_
    - general: ok when did this problem start?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* about _number_ mins ago on my drive home.
    - auto_repair.time.appt: ok so i am talking with them down at the shop and he says he can see you _time.appt_. unless you need it towed.   <!-- predicted: general: Ok - while Im out in that area is there anything else you need? -->
* see thats the thing with the way traffic is in the morning i might need to have it towed.
    - general: yeah i see your point what should i do?   <!-- predicted: auto_repair.time.appt: Yes, there is an appointment slot for _time.appt_. -->
* tell him i can be there in _time.appt_ so at _time.appt_ _date.appt_ if i can get there can he take a look?
    - hold on i will ask... so yes as long as you promis you can make it.
* awesome yes i will be there.
    - auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: ok so i just want to re cap you have a appointment _date.appt_ at _time.appt_ with _name.store_ for _reason.appt_ on your _year.vehicle_ _name.vehicle_. is all that correct?   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* yes it is thank you so much.
    - auto_repair.name.customer.accept: you are welcom i will text you directions and all the info. goodbye _name.customer_.   <!-- predicted: general: thank you so much i am going to text you all the info and the directions to the shop i hope it all gets fixed up -->


## dlg-1ee24ab5-ce88-4d66-a41a-7258e8682dc0
* Hey Jan I need you to book an appointment at the shop for my car for me.
    - auto_repair.name.customer: Ok _name.customer_, where you you like me to make it at?   <!-- predicted: general: Sure, no problem. I will set up an appointment for you. What is your name, please? -->
* _name.store_
    - general: Ok when you you like this for? And what is wrong with it?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: They will take it at _time.appt_ otherwise they cant take it until _date.appt_. -->
* I would like it for later _date.appt_ if possible. And _reason.appt_
    - general: And what kind of car is it, and the year?   <!-- predicted: auto_repair.date.appt_auto_repair.date.appt.accept_auto_repair.date.appt.reject_auto_repair.time.appt: It seems like they are out of available appointments _date.appt_. They have an opening at _time.appt_ _time.appt_. Would that work? -->
* It is a _name.vehicle_, _year.vehicle_ with a six cylinder
    - general: Ok I will call them and get back to you asap   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* sounds good, thanks
    - general: no problem   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* Phone rings. Hello
    - auto_repair.name.customer.accept: Hey _name.customer_, I made an appointment for you   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: _name.customer_name.store_ _date.appt_time.appt_ure taking in your _year.vehicle_name.vehicle_reason.appt_e phone number I have listed it _number_-_number_ Is all of that information correct? -->
* Great, when for?
    - auto_repair.date.appt.accept_auto_repair.time.appt.accept: I got it for you _date.appt_ at _time.appt_   <!-- predicted: auto_repair.reason.appt.accept: _reason.appt_, is there anything else. -->
* Excellent. Could you meet me there when I drop it off, and give me a ride to the office?
    - general: Sure I can do that.   <!-- predicted: uber_lyft.time.pickup.accept_uber_lyft.type.ride.accept: Yes. Ill arrange an _type.ride_ for you back to your home in _time.pickup_. -->
* Great, sounds good
    - No problem.
* Allright Jan I will see you in the _time.appt_ them
    - Sounds good sir. See you then


## dlg-1ee7ef18-db24-4a32-bdc8-129a69bf8672
* I would like a ride to _location.restaurant_ to go and eat a a restaurant for a date with my wife this weekend January _number_th.
    - Would you like me to order you a ride from your business on Long Island and take you two directly to New York City?
* Yes that would be wonderful. I am looking for a quality restaurant, upscale.
    - restaurant_reservation.location.restaurant: Well there are many upscale restaurants in _location.restaurant_? What type of food would you and your wife enjoy?   <!-- predicted: general: Ok, What time do you want me to make the reservation for? -->
* I think a steakhouse would be the best for us to eat.
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: Can I recommend a steakhouse called _name.restaurant_ on _location.restaurant_. It is known for its long history of serving delicious steaks.   <!-- predicted: general: You are looking for a French Resturant? What area are you looking for one in? -->
* That sounds delicious. Please set this table up for _time.reservation_.
    - Bad news! I just got off the phone with them and they are fully booked for this Saturday. However this may be to your advantage because although they have great food, this will not be a romantic date between you and your wife as there is no good view or romantic setting. May I recommend another restaurant perhaps more romantic?
* I would prefer something that has _type.seating_. Where we can eat and look out at the beautiful surroundings.
    - restaurant_reservation.location.restaurant.accept_restaurant_reservation.name.restaurant: May I recommend the restaurant _name.restaurant_. It is located on _location.restaurant_ and has a beautiful view of the Manhattan skyline.   <!-- predicted: general: No, they do not do that, but there is a splendid African restaurant about _number_ miles from here. They serve great East and West African dishes. -->
* That sounds lovely, what type of menu will it have?
    - restaurant_reservation.name.restaurant.accept: _name.restaurant_ has a contemporary and modern menu by Executive Chef Cyril Renaud. They do offer a Wagyu beef steak that I think you would enjoy.   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* I like what I hear and would like to book this restaurant.
    - Very well, I will make reservations. What time would you like to dine?
* I would like to go out for drinks after our meal so not too late. Book the reservation for _time.reservation_. I also need you to book a _type.seating_ as possible.
    - restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating_restaurant_reservation.type.seating.accept: Excellent, I will book a reservation for your table of _num.guests_ for _time.reservation_. I will also ask for a _type.seating_.   <!-- predicted: restaurant_reservation.time.reservation: yes, Shall I confirm reservation for _time.reservation_ ? -->
* Thank you. One last thing. I would like a bottle of champagne chilled and waiting for us on the table immediately when we arrive.
    - I will like them know of your request and Im sure this will be no problem. Would you like a car service home as well?
* That will not be necessary. I plan on staying over at a hotel close by however I will book these accommodations.
    - restaurant_reservation.location.restaurant: May you have a lovely time in _location.restaurant_ and I am glad I can assist you with your plans.   <!-- predicted: general: How would you like the invitations? How about we do a theme get together, make it fun spice things up. -->


## dlg-1b16077f-87d0-4843-87a2-7722578f5771
* Hi, Good morning Jane.
    - Good morning Maam.
* I need you to book me a restaurant reservation for _time.reservation_.
    - Ok, sounds good. Where am I setting up reservations.
* Im thinking either _name.restaurant_ or _name.restaurant_ in _location.restaurant_. Lets try Patina first. They do Vallet.
    - And what time should I set up reservations.
* Hmmm, lets do _time.reservation_.
    - general: And how many people   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_ -->
* Its a party of _num.guests_.
    - restaurant_reservation.time.reservation.reject: Well Im checking the website now, and they dont have a _time.reservation_.   <!-- predicted: general: What time do you want the reservation for? -->
* Well what time slots do they have?
    - restaurant_reservation.time.reservation: You can do _time.reservation_ or _time.reservation_.   <!-- predicted: general: Yes, they have a fully stocked sit down bar with premium wines and liquors. -->
* Lets check _name.restaurant_ reservations real quick. Maybe they have a _time.reservation_
    - No, problem. Give me a second.
* Have you found anything?
    - They dont even have reservations available for tonight.
* Ok, then lets do _name.restaurant_ at _time.reservation_.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: Alright, _name.restaurant_ at _time.reservation_ for a party of _num.guests_.   <!-- predicted: general: Any special diet restriction? -->
* Thank you, Jane.
    - Youre welcome Maam. Have a nice night.


## dlg-1eec7ca7-2281-47a9-a477-44b5218abf9d
* Hi, can you give me a hand setting up an appointment to bring my car in to see a mechanic.
    - Sure, no problem. Where are you looking to take it.
* I want to send it over to _name.store_.
    - Okay. Which car are you going to be bringing over there.
* Its going to be my _year.vehicle_ _name.vehicle_.
    - general: Okay. And whats the reason for the appointment.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* I _reason.appt_.
    - auto_repair.reason.appt.accept: Okay, _reason.appt_?   <!-- predicted: general: That sounds scary. Do you want me to see if I can make an appointment for you to bring it in? -->
* Yes. Please.
    - auto_repair.name.customer.accept: Okay. And put it under your name? _name.customer_?   <!-- predicted: general: Is the car otherwise functioning normally? -->
* Yes.
    - And youre phone number..._number_-_number_-_number_?
* Yes to all of the above.
    - Okay. Any specific time?
* Ask them if I can drop it off _time.appt_ and Ill pick it up sometime tomorrow.
    - Okay. Will do.
* Thank you.
    - auto_repair.time.appt.accept: Okay, I have it set up for you to drop it off _time.appt_ and pickup tomorrow afternoon. Its under your name and they have your phone number.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* Thank you.
    - general: Youre welcome.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->


## dlg-1ef438dd-9f0f-4a80-b959-6b0186ad657f
* Good Morning! Can you order me a coffee for pickup at peets?
    - Sure! what location and time?
* The location off of _location.store_.
    - Great! Okay, I can order here online, what would you like?
* _name.drink_
    - What size?
* _size.drink_, _coffee_ordering.preference_
    - general: Ok.   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* OH! and can you have them add some _type.milk_.
    - Sure, I can do that. Anything else you need?
* You know what, can you just add a Chicken Chorizo Flatbread.
    - general: Sure!   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* When will that be ready?
    - It looks like it will be ready for pick up in _number_ minutes.
* Sounds great, can you repeat what I ordered?
    - coffee_ordering.name.drink_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: _size.drink_, _preference.accept_, _type.milk_ _name.drink_ and a Chicken Chorizo Flatbread.   <!-- predicted: general: sounds good, anything else? pastries -->
* Perfect! Thank you so much.
    - No Problem! My pleasure, Ok, Ive got your payment confirmation. The receipt should show up on your phone soon.
* Wonderful, I really appreciate your help!
    - Of course! Have a great day! Goodbye.


## dlg-1efc782d-481c-4ccc-9dd9-d413e4c9bd3c
* Im going to need Jeff and Ted to work late tonight. Think showing up with pizzas will soften the blow?
    - Absolutely. Youll have a hard time getting them to leave.
* Thats what I wanted to hear. Pull up the menu for _name.store_ and Ill pick it up.
    - Youve got it. Pulling it up now. What would you like?
* Do they have anything new? I havent eaten there in a while.
    - Nothing that jumps out. Wait! They do.
* What do they have?
    - pizza_ordering.type.crust: It looks like they added a _type.crust_ option.   <!-- predicted: general: Yea they have a couple small sized dough but its whole wheat dough -->
* Huh. Is it an add on?
    - Yes it is.
* How much?
    - _price_ Im seeing nothing but good reviews for it on the site.
* Lets do it then.
    - You have to tell me what kind of pizza you want first.
* Oh yeah. _size.pizza_ _name.pizza_ on the _type.crust_.
    - pizza_ordering.name.pizza_pizza_ordering.size.pizza_pizza_ordering.type.crust: You said _size.pizza_ _name.pizza_ on _type.crust_. Is that right.   <!-- predicted: general: Got it. Do you want to change the sauce or cheese from the default choices? -->
* Thats right. Does that come with _type.topping_?
    - general: No it doesnt .   <!-- predicted: pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Okay so _number_ _size.pizza_ pizzas. One with _type.crust_ and _type.topping_, _type.topping_ and _preference.accept_. The other with _type.crust_ and _type.topping_, _type.topping_, _type.topping_ and _type.topping_. Plus _number_ _preference.accept_ and _preference.accept_? -->
* Switch out the _type.topping_ for _type.topping_ then alright?
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept_pizza_ordering.type.topping.reject: Let me repeat that one more time to be sure. _size.pizza_ _name.pizza_ on _type.crust_ and Im substituting the _type.topping_ for _type.topping_. Correct.   <!-- predicted: pizza_ordering.type.crust_pizza_ordering.type.topping.accept: Got it, two pizzas with _type.topping_ and _type.topping_, do you want _type.crust_ crust or _type.crust_ crust? -->
* Thats correct. How long will it be. Im about a half hour away?
    - It will be ready for pick up in about _number_ minutes. You should get a text with the details any moment now.
* Excellent. Thanks a bunch. Ill be back to the shop in a little bit.
    - general: Your welcome. Well see you in a minute.   <!-- predicted: pizza_ordering.location.store_pizza_ordering.name.store_pizza_ordering.preference.accept_pizza_ordering.size.pizza_pizza_ordering.type.crust.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Great. So to confirm your order, you want two _size.pizza_ pizzas, both _type.crust_ with _preference.accept_. You want _type.topping_, _type.topping_, _type.topping_, and _type.topping_ on the first, and _type.topping_, _type.topping_, and black olives on the second, and you want to pick them up at the _name.store_ location on _location.store_. Does that all sound right? -->


## dlg-1f1564c8-8946-4899-b1dc-23f15d0f68a8
* I want to book a _type.seating_ at _name.restaurant_ in _location.restaurant_
    - Okay, how many people will be dining?
* It will be _num.guests_.
    - general: What day and time would you like for this meal?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* We want to go next Friday evening between _time.reservation_ and _time.reservation_.
    - general: Do you have any requests for where youd like to sit?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: I apologize, but they dont have any _type.seating_ available on that date at _time.reservation_. -->
* We want to be near the chef so that we can see the meal preparation.
    - Sounds great. Let me check the availability.
* Thanks, let me know.
    - restaurant_reservation.name.restaurant.reject: I have bad news for you. Next Friday evening is all booked up at _name.restaurant_.   <!-- predicted: general: Let me just confirm with the restaurant -->
* Is there any availability on that Saturday, the evening after?
    - Im sorry, there is nothing free on that day either.
* Well lets try to book a _type.seating_ at _name.restaurant_ in _location.restaurant_ then.
    - restaurant_reservation.num.guests: Excellent. Will this be for just _num.guests_ still?   <!-- predicted: general: OK I will contact them. -->
* Yes, it will be just us _num.guests_.
    - Which day would you prefer, Friday or Saturday?
* We really would like to stick to Friday evening.
    - restaurant_reservation.time.reservation.accept: There is an open slot. How about Friday at _time.reservation_?   <!-- predicted: restaurant_reservation.type.seating.accept: Theres one that looks interesting -- a farm to table restaurant where everyone sits at _type.seating_ in an orchard! -->
* That is perfect, lets book it.
    - Your booking is confirmed. Have a great meal.
* Thanks for your assistance.
    - action_listen: action_listen   <!-- predicted: general: Thanks for choosing us. -->


## dlg-1f207b9c-8bb7-4a78-b484-5974e68616d9
* hello, good morning.
    - good morning sir.
* you have to do one thing to me.
    - general: sure sir, what will i do to you sir.   <!-- predicted: pizza_ordering.name.store: Sure !! Yes _name.store_ is available nearby _number_ miles -->
* book the appointment for me at an _name.store_ auto repair shop.
    - the appointment time and date sir?
* it must be with in two days.
    - k sir and they will ask the details of the car.
* _name.vehicle_, _year.vehicle_
    - any other information sir?
* what to you mean by any other information.
    - its like our mobile number, and name.
* _reason.appt_
    - k sir, now you can here me.
* yeah, you will give my mobile number and name.
    - i will do that sir.
* do you know the name of the shop.
    - auto_repair.name.store.accept: yeah sir you already told me that is _name.store_   <!-- predicted: general: Let me know what the password is. -->
* good. that is best the real time auto repair shop
    - i also heard about that shop sir.
* it more urgent.
    - general: i saw the results via an online interface   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt.accept: Okay, I have you scheduled for _date.appt_ at _time.appt_ -->
* k tell me about the available time
    - a later day is available sir
* k that time is convenient to me.
    - auto_repair.time.appt.accept: appointment time is _time.appt_, and the fee is _price_   <!-- predicted: general: Just let me know what you want to do -->
* k you will go to that time at the shop.
    - sure sir.
* k thanks, bye.
    - thank you sir.


## dlg-1f37b4ff-466d-4db3-9581-1e2f919dbf26
* Will you please order me a ride from _location.from_ to _location.to_
    - uber_lyft.type.ride: Sure, would you like Uber, _type.ride_, or a _type.ride_?   <!-- predicted: uber_lyft.location.to: Which _location.to_? -->
* _type.ride_ would be best.
    - Perfect. Would you like a premium or economy Uber?
* What are my options?
    - uber_lyft.type.ride: The _type.ride_ has room for many people.   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* That does not really suit me. I am alone.
    - general: Are you carrying Skis?   <!-- predicted: uber_lyft.time.pickup.accept_uber_lyft.type.ride_uber_lyft.type.ride.reject: Thank you. First, in the Uber department for _time.pickup_ tonight, they dont have an _type.ride_ but they do have an _type.ride_, is that ok? -->
* Nope.
    - uber_lyft.type.ride.accept: The _type.ride_ is probably the best option then.   <!-- predicted: general: OK, I am booking the ride. -->
* Ok. I will take it. What is the price?
    - uber_lyft.price.estimate.accept: _price.estimate_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Wow! thats a good price.
    - What is the pickup point?
* I will be at the _location.from_
    - OK. What color are you wearing.
* I am wearing a red shirt.
    - Ok. I will put that in the notes.
* Perfect. I am waiting.
    - uber_lyft.ride_booking.accept: _ride_booking.accept_ You can check the status on your personal phone.   <!-- predicted: general: Ok your ride should be there soon, anything else? -->
* Thanks
    - You are welcome.


## dlg-1f4284e4-21d0-41de-a8ea-71a5b6da894e
* Hi I need assistance
    - what can I help you with?
* I am having car issues
    - general: what kind of issue?   <!-- predicted: uber_lyft.location.to.accept: Ah, yes. _location.to_, correct? -->
* _reason.appt_
    - would you like to take it somewhere?
* yes
    - auto_repair.name.store.accept: _name.store_ can help you   <!-- predicted: general: What is the minimum star rating would you like? -->
* I want an appointment
    - what time?
* I want a morning appointment
    - auto_repair.time.appt: can you do _time.appt_?   <!-- predicted: general: Im sorry to hear that, would you like me to schedule an appointment to bring it in? -->
* can it be earlier?
    - auto_repair.time.appt: Yes, _time.appt_ is available   <!-- predicted: general: He is coming in a white honda civic. -->
* I will do _time.appt_
    - Okay, I have you bookes
* Thanks
    - general: you will get a confirmation message on your mobile phone   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: _name.customer_name.store_ _date.appt_time.appt_ure taking in your _year.vehicle_name.vehicle_reason.appt_e phone number I have listed it _number_-_number_ Is all of that information correct? -->
* Thanks
    - Good bye


## dlg-1f4a0a16-e9ad-498a-8537-0535a2794ced
* Hi, could you get me some movie tickets?
    - Sure, for when?
* Tonight!
    - Okay, which theater?
* _name.movie_ in _location.theater_.
    - Okay, can do. What movie?
* That new horror film, _name.movie_!
    - movie_ticket.num.tickets: Okay, that looks great! Just _num.tickets_ or _num.tickets_?   <!-- predicted: general: Bummer. It is not playing at that theater. -->
* _num.tickets_.
    - Okay, awesome. What time?
* What times are available?
    - Theres an _time.start_ and an _time.start_.
* Oh, lets do _time.start_, itll be scarier late at night!
    - general: Got it!   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* Does this movie have a _type.screening_ option?
    - No, it doesnt look like it.
* Oh, okay.
    - movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: So, Ive got _num.tickets_ to see _name.movie_ at _time.start_ at the _name.theater_ in _location.theater_. Anything else?   <!-- predicted: movie_ticket.name.movie_movie_ticket.num.tickets_movie_ticket.time.start_movie_ticket.time.start.reject: The late show wasnt until _time.start_ so that might have been a little too late. But, they do have _num.tickets_ tickets for the _time.start_ showing of _name.movie_ tonight, March _number_th. -->
* Nope!
    - general: Awesome! Youll get a text message on your phone with the tickets. Have fun!   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_ and have been sent to your mobile device as a text message -->
* Thanks, bye!
    - action_listen: action_listen   <!-- predicted: general: I just need some more information. -->


## dlg-1f4dbb29-88ae-4b1b-a6ad-16e69102417f
* I want to book a reservation at a restaurant.
    - Okay. Which restaurant would you like to go to?
* _name.restaurant_
    - What time and date would you like to book your reservation?
* This _time.reservation_.
    - restaurant_reservation.name.restaurant: Sorry, _name.restaurant_ is currently fully booked at that time. What other time would you be okay with?   <!-- predicted: restaurant_reservation.time.reservation: Okay great we have the option for a bottle of wine or roses at longhorns and availability at _time.reservation_ and a _price_ charge for wine or roses. -->
* How about _time.reservation_?
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject: Sorry, _name.restaurant_ is currently fully booked for that time. Would you like to check out a different restaurant?   <!-- predicted: restaurant_reservation.time.reservation: I see _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_ and _time.reservation_ as available. -->
* Yes. Ill just go to _name.restaurant_.
    - general: Okay. What time and date would you like your reservation?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* This _time.reservation_.
    - general: That is available. How many people is this for?   <!-- predicted: movie_ticket.name.theater: Okay, would you like them booked through Atom or _name.theater_ directly? -->
* _num.guests_.
    - restaurant_reservation.type.seating: Will you need a _type.seating_ for your child?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* No, my kids a teenager.
    - Do you have any seating requests?
* Anywhere is fine.
    - Is there anything else you want to add?
* No, thats all.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.time.reservation.accept: Okay. Your reservation has been booked at _name.restaurant_ for this _time.reservation_   <!-- predicted: pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping.accept: _type.crust_size.pizza_ with _, _name.pizza_preference.accept_type.topping_preference.accept_type.topping_type.topping_type.topping_type.topping_type.topping_ -->


## dlg-1f6473dc-7b34-4078-b2e0-45ca34d1113e
* Hi can you order me a drink from Starbucks please?
    - Hello Id be happy to do that. What location would you like me to order from?
* The Starbucks at _location.store_.
    - general: Okay and what drink do you want?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* Id like a _name.drink_ please?
    - coffee_ordering.size.drink: Sure and can I ask what size youd like - _size.drink_, _size.drink_, _size.drink_, or _size.drink_?   <!-- predicted: general: Okay. Would that be iced or hot? -->
* I think Id like a _size.drink_ please.
    - Okay and what type of milk would you like in it?
* Order _type.milk_ please.
    - general: Sure and are there any special requestsdirections for the order?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ok, _num.drink_ _preference.accept_, _, _size.drink_ a_type.milk_type.milk_preference.accept_ -->
* No just a _name.drink_ with _type.milk_ please.
    - general: Okay and what time do you want it ready for?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ok, _num.drink_ _preference.accept_, _, _size.drink_ a_type.milk_type.milk_preference.accept_ -->
* Id say in about _number_ minutes I will pick it up.
    - coffee_ordering.coffee_order.accept: Okay _coffee_order.accept_ and have it charged to your account.   <!-- predicted: general: Okay great. Do you want me to order that now? -->
* Sounds perfect thank you.
    - You are welcome, let me order and I will confirm for you.
* Okay.
    - coffee_ordering.name.drink.accept: I have ordered your _name.drink_ and it will be ready for pick up in _number_ minutes.   <!-- predicted: coffee_ordering.name.drink_coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.size.drink_coffee_ordering.size.drink.accept: Im at Starbucks ordering. _num.drink_ _size.drink_ _name.drink_ to go, on your account. -->
* Thanks so much.
    - Sure, confirmation of your order has been sent to your cell phone via text message.
* I just received the text, thanks!
    - general: Youre welcome, have a good day.   <!-- predicted: action_listen: action_listen -->
* You too.


## dlg-1b1f70cd-83b0-41a4-bbe0-1438fb39bdb5
* Hi I was wondering if you were showing _name.movie_ tonight?
    - general: Thank you for calling, may I ask which of our locations you planned on attending tonight?   <!-- predicted: movie_ticket.num.tickets: How many people will be joining you, just _num.tickets_? -->
* Ill be around the _location.theater_ tonight
    - movie_ticket.location.theater.accept_movie_ticket.name.theater.accept: We have an _name.theater_ _location.theater_.Is there a specific time frame you were looking to book for?   <!-- predicted: general: Okay, I show several theaters close by. Do you have a preference on which one you would like to go to? -->
* I was hoping to visit after dinner tonight.
    - movie_ticket.time.start: We have a showing at _time.start_ and _time.start_ will either of these times work for you?   <!-- predicted: general: Okay, which movie? -->
* _time.start_ would be fantastic please.
    - movie_ticket.price.ticket.accept: Wonderful, the ticket prices are _price.ticket_ and will be charged to your account, is that okay?   <!-- predicted: movie_ticket.price.ticket: Adult tickets are _price.ticket_ Child tickets are _price.ticket_. How many tickets would you like? -->
* Perfect, thank you very much.
    - How many tickets would you like me to book you for tonight Sir?
* _num.tickets_ please. Thank you.
    - movie_ticket.type.screening.reject: This has been booked for you Sir, please be advised they are not showing this movie in _type.screening_.   <!-- predicted: movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: I just purchased _num.tickets_name.movie_name.theater_ f_time.start_ -->
* Are there any dinner options available at this theater?
    - general: We have a concession stand but do not offer full course dinner options.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Thank you anyways.
    - Would there be anything else I can answer for you before you go Sir?
* That is all for today, thank you again.
    - Thank you for calling Sir, you will receive a confirmation text message containing your ticket information
* Thank you for your help, goodbye.
    - general: Goodbye Sir, if you need any further assistance we will be here.   <!-- predicted: action_listen: action_listen -->


## dlg-1f6a4703-808c-4130-befc-996eaadd5676
* I want to order a pizza from _name.store_ for pickup.
    - What time would you like it pick it up?
* As soon as possible.
    - Okay. What is your order.
* I want a _size.pizza_ _name.pizza_ but _preference.reject_.
    - pizza_ordering.name.store.accept: _name.store_ does not allow substitutions.   <!-- predicted: pizza_ordering.size.pizza: Do you want that _size.pizza_? -->
* Do they have the _size.pizza_ _name.pizza_
    - pizza_ordering.name.pizza: _name.pizza_ comes in individual size only.   <!-- predicted: general: Sure, that works. Please let me know what two toppings you would like to add. -->
* Okay I will have two _name.pizza_ and six dough balls.
    - Do you need drinks?
* Yes, Two medium diet cokes.
    - pizza_ordering.name.pizza_pizza_ordering.name.pizza.accept: Okay. _number_ _name.pizza_ _number_ dough balls and _number_ medium Diet Cokes.   <!-- predicted: general: Alright can I get you anything else tonight? -->
* Yes.
    - Diet Coke is not available. Is Diet Pepsi okay?
* Yes that is fine.
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ It will be ready in _number_ minutes.   <!-- predicted: general: Okay the total will be _price_ and itll be ready for pickup in _number_ minutes. -->
* What is the total cost.
    - Your total is _price_
* I want to leave a _number_% tip on the bill.
    - Okay. I will do that. The receipt will be sent to you by text message.
* Thanks. Bye.
    - action_listen: action_listen   <!-- predicted: general: Bye see you tomorrow -->


## dlg-1f75dec1-cd69-46c5-bc88-2b761f181435
* Hi Sara I am looking for an Italian Restaurant in the area with good reviews
    - Okay what is a good review and how much are you looking to spend.
* I want a restaurant with at least _number_ stars and no more than _price_ per person.
    - general: I will look for some restaurants for you in the city   <!-- predicted: restaurant_reservation.time.reservation: NO PROBLEM. I WILL SCHEDULE YOUR RESERVATION FOR _time.reservation_. WILL IT BE FOR TOMORROW? -->
* Thank you Sara I can always depend on you
    - There are about _number_ different restaurants in the city that fit your requirements we are going to have to eliminate some of them.
* Can you pull up some menus that have chicken alfredo on them, the person I am dining with loves it
    - general: I was able to call or find all the menus online, by your restriction there are about _number_ resteraunts left   <!-- predicted: coffee_ordering.name.drink: Sure, they have _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, and _name.drink_. -->
* Okay, since there are so many resteraunts left can you arrange them on popularity
    - general: There seems to be _number_ different restaurants that are currently rated _number_ stars and extremely popular   <!-- predicted: restaurant_reservation.location.restaurant.accept: _location.restaurant_ Ive also included there telephone number for your convenience. -->
* We should try to find the best restaurant for me that would have a private dining experience
    - Since we can not narrow down to one restaurant should I just call all three of the restaurants and find which one will the least busy
* Yes Sara I would like that I can have the best dining expereince
    - Before I call what day where you thinking about going?
* I want to go out to eat this saturday
    - general: I made a few calls and I found out that there are two restaurants that would work for you   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: _name.theater_num.tickets_name.theater_time.start_name.movie_location.theater_ -->
* Are there any differences between the two restaurants?
    - general: Restaurant A is about half the price as restaurant B   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Since the first restaurant is so much cheaper can you make a reservation for it
    - restaurant_reservation.time.reservation.accept: I have made the reservation you will be having dinner at restaurant a on Saturday at _time.reservation_   <!-- predicted: general: Yes, we do have American selections like hamburgers, steak and chicken. -->
* Thank you Sara you are always helpcome
    - general: You are welcome let me know if you need anymore help.   <!-- predicted: action_listen: action_listen -->


## dlg-1f7ec5e2-07df-4a29-b0c7-7ecd3d2f7a82
* Can you buy two tickets for _name.movie_ at a theater in _location.theater_?
    - movie_ticket.location.theater_movie_ticket.name.theater: Sure! Let me help you with that. How does _name.theater_ in _location.theater_, sound?   <!-- predicted: movie_ticket.name.movie: Ok, I can see where _name.movie_ is play. Do you have a city you would like to see it in? -->
* Thats great. Get me _num.tickets_ for _name.movie_ in _type.screening_, please.
    - movie_ticket.name.movie_movie_ticket.type.screening_movie_ticket.type.screening.reject: Im sorry. _type.screening_ is not available for this show. Would you like to get tickets for the _type.screening_ showing of _name.movie_ instead?   <!-- predicted: general: Bummer. It is not playing at that theater. -->
* No. What other movies are playing right now?
    - movie_ticket.name.movie: Several movies are playing today. Based on your interests, you might like the movie _name.movie_.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* What is _name.movie_?
    - movie_ticket.name.movie: _name.movie_ is a superhero origin story. The movie is part of the DC cinematic universe and introduces the character. Would you like to hear more?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* No. Can you get me _num.tickets_ for _name.movie_ _time.start_, at the _name.theater_ in _location.theater_? I want tickets to a _type.screening_ showing.
    - movie_ticket.name.movie_movie_ticket.time.start_movie_ticket.type.screening: The only _type.screening_ showing for _name.movie_ is at _time.start_. Would that work?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Do they have a _time.start_ showing for _name.movie_?
    - movie_ticket.name.movie_movie_ticket.name.theater_movie_ticket.time.start_movie_ticket.type.screening: Yes. There is a _time.start_ showing for _name.movie_ in their _name.theater_. However, it is a _type.screening_ showing. Would you like me to buy tickets to this showing?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* No, thank you.
    - movie_ticket.name.theater_movie_ticket.time.start: Would you like to know more about other movies playing tonight at _name.theater_? There are several movies starting around _time.start_.   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* Are any of them playing in _type.screening_?
    - movie_ticket.time.start_movie_ticket.type.screening_movie_ticket.type.screening.reject: None of the shows starting around _time.start_ are in _type.screening_. Would you like me to look at other showtimes?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* No, thank you.
    - movie_ticket.location.theater_movie_ticket.name.movie: Would you like me to look for _name.movie_ or _name.movie_ tickets at other theaters in _location.theater_?   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* No thank you. I dont need tickets anymore.
    - general: Okay. Is there anything else I can assist you with today?   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* No, thank you.
    - general: My pleasure.   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->


## dlg-1f7f48de-ccc6-4dd0-bf94-36736bb4539f
* Can I book a table for party of _num.guests_
    - general: When   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* Tonight
    - What time
* _time.reservation_
    - restaurant_reservation.time.reservation.accept_restaurant_reservation.time.reservation.reject: We dont have availability at _time.reservation_. How about _time.reservation_number_   <!-- predicted: general: Sorry, there are no openings for that time. -->
* Sure
    - Any special requirement? Any disabled person in your party?
* No
    - Any kids?
* No
    - Anyone with allergy
* Yes, I have peanut allergy
    - ok. I will make sure menu doesnt have anything with peanut. Would you like to receive the menu via email
* Sure
    - Your email address?
* Poly
    - OK. I will email the menu now. Do you have loyalty card
* Yes, my account number _number_
    - OK. You have _number_ point available to be redeemed
* Thanks
    - Is there anything else I can help with
* Yes. Do you have free car park?
    - Yes, you can park your car to _number_ Main St. parking lot and validate parking ticket in our restaurant
* Thank you. Can you also email me your vine list
    - Sure
* Also, can I bring my own wine?
    - Sure. There will be _price_ corkage fee
* Thanks
    - Thanks for choosing us.


## dlg-1f94d9a4-30d4-4e5a-a4af-bd80f813f1f1
* _reason.appt_. you need to sort me out.
    - how can i be of assistance
* schedule an _auto_repair.auto_repair_location.store_name.store_
    - whats the problem?
* _reason.appt_
    - auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_   <!-- predicted: general: I see I can get an appointment setup for you -->
* how soon can i bring it in?
    - auto_repair.date.appt_auto_repair.time.appt: _date.appt_, at _time.appt_   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* no, i need to be seen _date.appt_
    - auto_repair.date.appt_auto_repair.date.appt.accept_auto_repair.time.appt: you can come in _date.appt_, at _time.appt_   <!-- predicted: general: Im sorry to hear that, would you like me to schedule an appointment to bring it in? -->
* what sort of inspection fee do theycharge?
    - they will wave the initial inspection fee
* thats cool
    - auto_repair.name.customer.accept: ive booked the reservation under _name.customer_   <!-- predicted: general: Okay. I need what address and phone number you would like me to list here. -->
* good od
    - they can reach you at _number_ _number_
* because the cars acting up
    - general: yes   <!-- predicted: auto_repair.name.customer.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Ok, thats an appointment for _name.customer_ phone number _number_-_number_-_number_ with a _year.vehicle_ _name.vehicle_ that is having a _reason.appt_ at _time.appt_ Is that correct? -->
* okay
    - auto_repair.appointment.accept_auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: _appointment.accept_ arrival at _date.appt_ at _name.store_reason.appt_you drop off the car. ill remind you at six oclock   <!-- predicted: general: Goodbye -->


## dlg-1f959bc3-e202-4165-80b7-dac88e4ad7e1
* Hi, I would like to order a Starbucks drink please.
    - Sure. What can I order for you?
* I would like a _name.drink_.
    - coffee_ordering.name.drink: What size _name.drink_ would you like?   <!-- predicted: pizza_ordering.preference_pizza_ordering.preference.reject: _pizza_ordering.preference_preference.reject_? -->
* I would like a _size.drink_ please.
    - general: Got it. What kind of milk would you like?   <!-- predicted: coffee_ordering.preference.reject: Any _preference.reject_ -->
* I would like _type.milk_ please.
    - general: Okay. Would you like to add anything else to your drink?   <!-- predicted: coffee_ordering.preference.reject: Any _preference.reject_ -->
* I would like to _coffee_ordering.preference_ please.
    - Okay. _coffee_ordering.preference_. Which location would you like to pick up at?
* I would like to pick up at _location.store_
    - general: I just want to confirm your order.   <!-- predicted: coffee_ordering.preference.reject: Unfortunately we do not have _preference.reject_ available. Would you like to make any adjustments? -->
* Okay. go ahead.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: You want a _size.drink_ _name.drink_ with _type.milk_ and _preference.accept_.   <!-- predicted: coffee_ordering.preference: Would you like any _coffee_ordering.preference_? -->
* Correct. Can I also _preference.accept_?
    - Yes.
* Thank you.
    - coffee_ordering.location.store.accept: Your drink will be ready in twenty minutes at _location.store_.   <!-- predicted: general: Would you like this order for pick-up? -->
* Thank you
    - Youre welcome. Goodbye.


## dlg-1f9bb6aa-2ec0-475e-8506-8814954b0c1e
* Hi there, I would like to book some movie tickets.
    - Awesome, let me check my notes first.
* Already, take your time.
    - What movie do you plan to watch?
* I would like to watch the movie _name.movie_.
    - How many people are going?
* Only _num.tickets_. We will meet there at the theater.
    - Sounds great, what is the name of the theater?
* The name of the theater is _name.theater_
    - Thank you. What is the address?
* _location.theater_.
    - general: Thank you again.   <!-- predicted: movie_ticket.name.movie_movie_ticket.name.theater: i show the _name.movie_ playing at _name.theater_ tonight. is that ok? -->
* No problem.
    - What is the time frame?
* _time.start_ at _time.start_.
    - Let me check. Sorry that time is not available.
* That is fine. How about _time.start_
    - general: No sorry again, that time is full.   <!-- predicted: movie_ticket.time.start.reject: there is no _time.start_ show -->
* Try _time.start_ and let me know.
    - That time is available.
* Is there _type.screening_ available for this movie?
    - movie_ticket.type.screening.reject: No, there is no _type.screening_ available for this film.   <!-- predicted: general: Yes, they have valet parking. -->
* That is all I need.
    - The tickets are being sent to your mobile device as a text message.
* Thank you!
    - You are welcome!


## dlg-1fbb571d-0f3b-41ac-998d-40dd24c15116
* Hello i would like some information on an uber ride from _location.from_ to _location.to_ then to _location.to_ then _location.to_.
    - Okay I can help you with that, what city do you live in?
* _location.from_
    - Okay let me look it up
* Okay
    - Okay give me _number_ seconds to see what I can find.
* Okay great
    - uber_lyft.type.ride_uber_lyft.type.ride.accept: _type.ride_ can take you at that time, let me get the route info for you, its _type.ride_ no other passengers so they can focus on you. I know you prefe Uber but no cars are available at that time.   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* Okay great, Ill wait for the info. Lyft is okay
    - uber_lyft.duration.estimate.accept_uber_lyft.location.from_uber_lyft.location.to_uber_lyft.location.to.accept: _location.to_location.from_ to _location.to_duration.estimate_   <!-- predicted: general: The driver picking you up is a male. -->
* Okay great then to what store?
    - uber_lyft.duration.estimate.accept_uber_lyft.location.to_uber_lyft.location.to.accept: Then to _location.to_ estimated time is _duration.estimate_   <!-- predicted: general: They said you have used SAE _number_W-_number_ in the past. -->
* Okay great, then will they wait and drive me home?
    - uber_lyft.duration.estimate.accept_uber_lyft.location.to.accept_uber_lyft.price.estimate.accept: Yes then back to _location.to_ estimated time is _duration.estimate_, and total fare is _price.estimate_   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Great thanks so much.
    - general: Will you be using paypal or credit card?   <!-- predicted: uber_lyft.time.pickup.accept: Your uber will be arriving in _time.pickup_. Is there anything else I can do? -->
* Credit Card please
    - Yes its under your name and it should be ready to go, is there anything else I can do?
* Thats perfect, thank you so much for your help.
    - general: Thank you and have a lovely day   <!-- predicted: uber_lyft.location.from.accept_uber_lyft.location.to.accept_uber_lyft.time.pickup.accept_uber_lyft.type.ride.accept: Ok Leonard Hofstadter, Ill end the conversation by confirming that your _type.ride_ ride is ready for you Friday, April _number_th at _time.pickup_location.from_location.to_ and will take you to your residence at _location.to_. and that you can check the status on your phone at anytime. -->


## dlg-1fe04590-7689-44c8-894f-810826be99e4
* I need book a ride with Lyft
    - Where are you at and what is your destination
* I am at _location.from_ and want to book a ride on Lyft to _location.to_
    - Okay how many passengers are there.
* There are _num.people_ passengers and I want to book _type.ride_
    - uber_lyft.location.from_uber_lyft.location.to_uber_lyft.num.people_uber_lyft.type.ride: Okay, I will look for a _type.ride_ for _num.people_ passengers from _location.from_ to _location.to_   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* Thanks, Let me know how long it will be for pickup.
    - uber_lyft.type.ride.reject: There are currently no _type.ride_ available from your location to the requested destination.   <!-- predicted: general: Youll need to connect a payment source to it, then just tap the request ride option in the app and the rest is self explanatory. -->
* Just book a _type.ride_ for _num.people_ passages on Lyft
    - uber_lyft.location.from_uber_lyft.location.to_uber_lyft.num.people_uber_lyft.type.ride: I will look for a _type.ride_ for _num.people_ people using Lyft from _location.from_ to _location.to_   <!-- predicted: general: What time do you want to go? -->
* Great how long will that take
    - uber_lyft.duration.estimate.accept_uber_lyft.time.pickup: It is a _time.pickup_ wait and an _duration.estimate_ travel time   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Great that will work.
    - Are you ready for pickup now
* Yes, please book.
    - uber_lyft.location.from.accept_uber_lyft.location.to.accept_uber_lyft.num.people.accept_uber_lyft.type.ride.accept: There is a _type.ride_ car available for _num.people_ people from _location.from_ to _location.to_   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_ and is on the way. You can check the status on your phone. -->
* Thats great
    - uber_lyft.time.pickup.accept: Your vehicle will arrive in approximately _time.pickup_   <!-- predicted: general: you can check further details and track the arrival via the app on your phone -->
* Great, please bill that to my account.
    - This has been booked to your Lyft account.


## dlg-1fe13650-486b-4849-9174-fb44a2bbf602
* Hi, I need to book an appointment for an _reason.appt_, please.
    - Ok, where would you like to go?
* Can you book an appointment at _name.store_?
    - auto_repair.name.store: Got it. Im searching for an appointment at _name.store_. What time would you like to schedule an appointment?   <!-- predicted: general: yes can i get your name and telephone number -->
* Is there anything available this _time.appt_?
    - auto_repair.time.appt: There is an appointment available at _time.appt_.   <!-- predicted: auto_repair.time.appt_auto_repair.time.appt.accept: They have an opening _time.appt_ or _time.appt_, at _time.appt_. -->
* Great, book that please.
    - general: Ok. Can you tell me the make and model of your vehicle?   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Ive checked _name.store_ schedule. Times available _date.appt_ are _time.appt_, _time.appt_, _time.appt_, and _time.appt_. Which would you like? -->
* Its a _name.vehicle_.
    - Great. Can you tell me the year of your vehicle?
* _year.vehicle_.
    - general: Ok, thanks. What name would you like to book the appointment for?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _name.customer_.
    - Ok. What is your phone number?
* Its _number_-_number_-_number_
    - auto_repair.name.store.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: Ok. Ive confirmed an appointment for an _reason.appt_ this _time.appt_ at _name.store_.   <!-- predicted: auto_repair.name.customer.accept: Okay _name.customer_, the phone number was _number_-_number_-_number_ correct? -->
* Ok thanks.
    - Do you need anything else?
* No, thats it.
    - Thank you, you are all set.


## dlg-1b211be5-14b1-43d8-a5bd-21d1c3cb23d4
* I would like _restaurant_reservation.restaurant_reservation_ _time.reservation_ for something french.
    - You are looking for a French Resturant? What area are you looking for one in?
* _location.restaurant_
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: _name.restaurant_ seems like it would be a perfect fit. It has _number_ stars and is _location.restaurant_.   <!-- predicted: general: What exact restaurant do you want to make a reservation? -->
* Thats pretty good, lets book a table there.
    - Ok, how many people is the table going to be for?
* _num.guests_ people.
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject_restaurant_reservation.num.guests: A table at _name.restaurant_ for _num.guests_ people? I am sorry, the Bistro does not reserve tables for that large of a party.   <!-- predicted: general: Okay, how many people will be dining? -->
* Ok, well is there any place that does?
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests: _name.restaurant_ allows reservations for up to _num.guests_ people, would you like to try there? They have a _number_ star rating with glowing reviews.   <!-- predicted: restaurant_reservation.time.reservation: Unfortunately we do have live music. They dont start until _number_pm though, so if youd like to come in by _time.reservation_ you should be finished by the time they start. -->
* Yes, lets try there. Do they have _type.seating_?
    - restaurant_reservation.type.seating: Yes, they do have _type.seating_, would you like to have the table booked _type.seating_?   <!-- predicted: general: Sounds awesome; Valerie just called and asked about the dinner...is she part of the party? -->
* Yes, that would be wonderful!
    - general: What day and time is the reservation going to be?   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* It will be for Saturday at _time.reservation_.
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Saturday at _time.reservation_ is all booked up. There is an opening at _time.reservation_, would you like that time instead?   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* _time.reservation_? Thats a little late, we have other plans after _number_pm.
    - general: I am sorry to hear that, would you like to try another resturant?   <!-- predicted: restaurant_reservation.reservation.accept: Okay, _reservation.accept_, sir. -->
* No, thats ok. Ill just ask around with the people I am going to be with and see what they want to do now. Thanks for your help.
    - Not a problem, if you decide to book a table, let me know and I will help.


## dlg-1fe30975-b20d-478b-a6a1-f38a60f420fd
* Can I have a ticket for _name.movie_ Movie
    - When
* Today
    - What time
* _time.start_
    - movie_ticket.time.start_movie_ticket.time.start.reject: No session at _time.start_. Would you like _time.start_?   <!-- predicted: general: Okay, let me check ticket availability for that showing. -->
* Yes please
    - movie_ticket.num.tickets: _num.tickets_ ticket?   <!-- predicted: general: Do you want the tickets sent to your phone or held at willcall? -->
* yes
    - general: How would you like to pay?   <!-- predicted: movie_ticket.time.start_movie_ticket.time.start.reject: I am sorry, at _time.start_ the showing is all sold out as well. Would you like to try a movie showing at _time.start_? -->
* Credit card
    - Card number?
* _number_
    - Expiration date?
* _number_-_number_
    - Security code
* _number_
    - Do you have loyalty card?
* Yes
    - Can you give me your account number?
* Danny_number_
    - Your birth date for verification?
* _number__number__number_
    - Thanks. You have _number_ point
* OK
    - Would you like to use your points to get _price_ discount
* Yes please
    - movie_ticket.price.ticket.accept: OK. Ticket is _price.ticket_. You will pay _price_ after redeeming point   <!-- predicted: general: Do you want me to arrange the Uber then? -->
* Great. Please go agead
    - movie_ticket.ticket_booking.accept: _ticket_booking.accept_ and emailed to your email address   <!-- predicted: uber_lyft.ride_booking.accept: Ok. _ride_booking.accept_. If there is anything else you need, please feel free to ask. -->


## dlg-1fea3a25-ad63-4e2d-b3d4-db487bab5b7e
* Hey Google, can you order me a coffee drink from starbucks?
    - Yes, in what place?
* In _location.store_
    - coffee_ordering.location.store_coffee_ordering.location.store.accept: Is that _location.store_?   <!-- predicted: general: I agree. What should I order? -->
* Yes
    - what drink would you love to have?
* _name.drink_ with _coffee_ordering.preference_.
    - coffee_ordering.name.drink_coffee_ordering.preference: Ok is that _name.drink_ with _coffee_ordering.preference_?   <!-- predicted: general: Anything else with that? Food? -->
* yes
    - general: Perfect. What Milk should we add their?   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* _type.milk_
    - What size of the drink?
* _size.drink_
    - coffee_ordering.name.drink_coffee_ordering.preference_coffee_ordering.size.drink_coffee_ordering.type.milk: Ok got it _size.drink_ _name.drink_ with _coffee_ordering.preference_ and _type.milk_ added to it. What else would you love to add?   <!-- predicted: general: Should I charge it to the company card? -->
* Nothing thats just perfectly fine.
    - coffee_ordering.location.store_coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ok _name.drink_ with _preference.accept_ and _type.milk_ _size.drink_ will be ready in _location.store_ in about _number_ minutes from now.   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ok so _num.drink_ _size.drink_ _name.drink_, _type.milk_, _preference.accept_, _preference.accept_, and _preference.accept_, correct? -->
* Thank you google.
    - No probelm Kevin, Your drink will be ready for pick up in _number_ minutes and your receipts will be sent via text message.
* Oh sweet, Thanks google
    - Enjoy your Coffee kevin.


## dlg-1feae5f7-48d1-40fb-a98e-678a3828f874
* Hey, can I get a _pizza_ordering.pizza_ordering_ from _name.store_?
    - yes, what size do you want?
* what sizes are there?
    - pizza_ordering.size.pizza: there is _size.pizza_ _size.pizza_ _size.pizza_ _size.pizza_ and _size.pizza_   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* get me the _size.pizza_ that sounds amazing!
    - general: okay, what do you want on it?   <!-- predicted: pizza_ordering.name.pizza.reject: I am sorry, were currently out of the _name.pizza_. Is there anything else youd like instead? -->
* I want _type.topping_, _type.topping_, and _type.topping_.
    - pizza_ordering.type.topping.reject: Im sorry, it looks like they dont carry _type.topping_   <!-- predicted: general: Okay. Do you want any appatizers? -->
* oh, okay, what about _type.topping_?
    - pizza_ordering.type.topping: yes, they have _type.topping_.   <!-- predicted: general: we only have coke, sprite, dr pepper, and mountain dew. -->
* I want those then.
    - pizza_ordering.size.pizza_pizza_ordering.type.topping: okay, so you want a _size.pizza_ with _type.topping_, _type.topping_, and _type.topping_?   <!-- predicted: pizza_ordering.preference.reject_pizza_ordering.type.topping: _type.topping_preference.reject_ on the crust. -->
* yes, Oh and add add _type.topping_
    - pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: okay, a _size.pizza_ with _type.topping_, _type.topping_, _type.topping_, and _type.topping_   <!-- predicted: general: Would you like something else instead? -->
* yes, I already have an account there.
    - pizza_ordering.pizza_order.accept: I see that, so _pizza_order.accept_ and it will be ready in _number_ minutes   <!-- predicted: general: When do you plan to pick it up? Do you want me to order it right now? -->
* thanks
    - your receipt will be texted to you.
* Thank you.
    - youre welcome.


## dlg-1febaef7-9070-4954-af3b-b8f1a8a0b614
* Hello, do you have a _name.restaurant_
    - We do
* Id like to amke a reservation for _num.guests_ on Thursday February _number_ at _time.reservation_
    - Im sorry, we do not have any _type.seating_ available for that time slot
* OK, what times do you have avaiable?
    - restaurant_reservation.num.guests_restaurant_reservation.time.reservation_restaurant_reservation.type.seating: We do not have any avaiable _type.seating_ for _num.guests_ until _time.reservation_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Is there a bar area that we could seat ourselves
    - general: There is, however, those tend to fill up early   <!-- predicted: movie_ticket.name.movie: Are you a fan of _name.movie_ came out a few months ago, and it was really good! -->
* Ok, id like to make a reservation for _num.guests_ at _time.reservation_
    - ok
* But if there is a problem with our other party can I call this number to cancel?
    - Yes this would be the number to call
* ok, than please make that reservation
    - Can I have a name and number please?
* _name.reservation_ _number_
    - restaurant_reservation.name.reservation.accept: Confirmaing thats for _name.reservation_ _number_   <!-- predicted: uber_lyft.ride_booking.accept: Okay, _ride_booking.accept_. -->
* Thank you
    - restaurant_reservation.time.reservation.accept: Youre welcome We will see you on Thursday February _number_ at _time.reservation_   <!-- predicted: general: Is there anything else you require? -->
* Good bye
    - Good bye


## dlg-1ff1817f-7a66-46d1-b340-99dd22ec5d0b
* Something is wrong with my car. I need to have it looked at.
    - auto_repair.name.store.accept: The new service were using is _name.store_   <!-- predicted: general: Great and you? Flight home yesterday went well I assume? -->
* Whats the difference between this one and the last?
    - general: One of the biggest differences is a real time online interface so youll have access when you need it.   <!-- predicted: uber_lyft.type.ride: _type.ride_, _type.ride_, _type.ride_, _type.ride_, _type.ride_, _type.ride_, _type.ride_, -->
* Okay. What do you need from me to schedule an appointment?
    - Im going to need the make, model, year and timeframe you want the appointment scheduled.
* It is a _year.vehicle_ _name.vehicle_ and Id like to schedule an appointment before _time.appt_ _date.appt_.
    - auto_repair.reason.appt: Oh, Im sorry _reason.appt_   <!-- predicted: general: Alright, I will contact the shop. Is there a time that works best for me to schedule the appointment. -->
* _reason.appt_
    - general: Give me just a moment while I put your info in.   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_. -->
* Fine. Just let me know.
    - general: Everything was able to take just fine. Except...   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: Alright, Ill put you in for _time.appt_ _date.appt_. -->
* Whats wrong?
    - general: I got all of your info entered but the shop doesnt take vehicles on such short notice.   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* When can I get the car taken care of then?
    - auto_repair.date.appt_auto_repair.time.appt: The earliest is _date.appt_ as long as the vehicle is on site by _time.appt_.   <!-- predicted: general: Well, you did spend over a month in intensive care. -->
* Does something happen after _time.appt_?
    - general: Usually shops are overrun with people after they open and this is a means for them to get to your car within the first wave.   <!-- predicted: auto_repair.time.appt: Yes, the have a slot available around _time.appt_. Would you like me to book that? -->
* Thats understandable so where are we now?
    - auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know.   <!-- predicted: general: Could I also have your phone number? -->


## dlg-1ff31a92-768b-4a23-b477-029a8cb358d7
* HEY. CAN YOU SCHEDULE AN APPOINTMENT FOR ME?
    - SURE. WHAT KIND OF APPOINTMENT?
* AUTO REPAIR. AT _name.store_
    - SURE
* ITS A _year.vehicle_ _name.vehicle_
    - general: OK   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* NAME IS _name.customer_ AND NUMBER IS _number_
    - general: OK   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt.accept: Okay. Scheduled now. You should be there by _time.appt_ at the latest _date.appt_. -->
* _reason.appt_
    - general: COOL   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_. -->
* OH, I THINK _reason.appt_
    - general: OK. WHAT TIME DO YOU WANT IT SCHEDULED?   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_. -->
* NOW.
    - OK. LET RUN IT THROUGH
* THANKS
    - general: IT GONNA COST _price_   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* GREAT
    - auto_repair.date.appt.accept_auto_repair.time.appt.accept: I SCHEDULED FOR _time.appt_ _date.appt_   <!-- predicted: general: would you be paying in office -->
* EVEN BETTER
    - COOL


## dlg-20030462-487a-44f6-9f9f-9dac92a5c5e9
* Do you have any pizza specials tonight?
    - Yes, we have buy one, get one half off and _number_% off breadsticks. Would you like to try one of these?
* No thank you. How much is a _size.pizza_ _name.pizza_?
    - A _size.pizza_ is _price_ but for just _price_ more, you can make it a _size.pizza_.
* OK, I will have a _size.pizza_ _name.pizza_ please.
    - pizza_ordering.type.topping.reject: Alrighty, so, after tax, it looks like your total will be...oh wait. Theyre telling me we are out of the _type.topping_ for your pizza.   <!-- predicted: pizza_ordering.type.topping_pizza_ordering.type.topping.reject: Alright, let me find their number. Ah, here we go. I guess they are out of the _type.topping_. Do you want _type.topping_ instead? -->
* Bummer. Do you have any newer specialty pizzas worth trying?
    - pizza_ordering.name.pizza: We have the _name.pizza_ and the _name.pizza_ that seem to be crowd favorites.   <!-- predicted: general: Yeah theres none Im not a fan of haha -->
* Ooh, what is on the _name.pizza_?
    - pizza_ordering.preference.accept_pizza_ordering.type.topping.accept: That one has _type.topping_, _type.topping_, a _type.topping_preference.accept_type.topping_,   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* Oh wow. That sounds delicious. Is that the same price as the _name.pizza_?
    - general: Yes mam, and if youd like, I can add on an order of breadsticks.   <!-- predicted: pizza_ordering.name.pizza_pizza_ordering.preference_pizza_ordering.size.pizza_pizza_ordering.type.crust: Absolutely, that is a _size.pizza_name.pizza_type.crust_ with _pizza_ordering.preference_, _pizza_ordering.preference_, and _pizza_ordering.preference_ Is there anything else I can get for you? -->
* No thank you. I will have a _size.pizza_ _name.pizza_ please.
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept: Ok, so one _size.pizza_ _name.pizza_. Is there anything else you would like?   <!-- predicted: pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping.accept: Ok, just confirming Ill order one _size.pizza_ pizza, _type.crust_, classic sauce, with _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, and _type.topping_ for lunch today, using your cell phone, and they have your credit card on file? -->
* After tax, you total will be _price_
    - general: Thank you very much. My card should be saved in your system.   <!-- predicted: pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Okay so _number_ _size.pizza_ pizzas. One with _type.crust_ and _type.topping_, _type.topping_ and _preference.accept_. The other with _type.crust_ and _type.topping_, _type.topping_, _type.topping_ and _type.topping_. Plus _number_ _preference.accept_ and _preference.accept_? -->
* You are correct. Would you like to include a tip?
    - Yes, you can add _price_ onto my bill.
* Ok thank you. That brings your total to _price_ Your order will be ready for pickup in thereabouts of _number_ minutes.
    - Ok. Thank you and see you soon!


## dlg-2004438d-a50e-4a0c-8e1a-e3aac4d4d11f
* Id like to _restaurant_reservation.restaurant_reservation_.
    - restaurant_reservation.name.restaurant: _name.restaurant_ is a great one that you would enjoy.   <!-- predicted: general: How many locations are there? -->
* I like that place. Can I get a _type.seating_ _type.seating_ for _num.guests_ at _time.reservation_?
    - restaurant_reservation.time.reservation.reject: A _time.reservation_ table for tonight, Ill see what they have and will get back to you.   <!-- predicted: restaurant_reservation.type.seating: Excellent, would you prefer a _type.seating_ or _type.seating_? -->
* Ok, cool.
    - restaurant_reservation.type.seating: Right now they do not have a _type.seating_ _type.seating_ for the time you requested.   <!-- predicted: restaurant_reservation.reservation.accept: Okay, _reservation.accept_, sir. -->
* Do they have any _type.seating_ available _type.seating_ at all?
    - They do, they have one at _time.reservation_ and one at _time.reservation_.
* Ill take the _time.reservation_ one. That is a _type.seating_ for _num.guests_ right?
    - restaurant_reservation.num.guests: Yes, that is a table for _num.guests_. What name will it be under?   <!-- predicted: restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: _name.restaurant_name.reservation_ for _ people at _, and it_num.guests_looks like _time.reservation_o have a _. Your reservation ha_type.seating_n set. Anything else? -->
* You can put it under _name.reservation_. Do you need a credit card or anything?
    - restaurant_reservation.restaurant_reservation: Yes, I need a card to hold the _restaurant_reservation.restaurant_reservation_. There is a fee if wait too late to cancel.   <!-- predicted: general: I may stop for a pizza myself on my way home -->
* Sounds good. Use my chase card that I have on file.
    - general: I have put in all the information and you are set. Is there anything else I can do for you?   <!-- predicted: restaurant_reservation.name.restaurant_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation: Okay then. So to confirm, you want a table for _num.guests_ at _time.reservation_ at _name.restaurant_. -->
* No, that is all I wanted for now.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating_restaurant_reservation.type.seating.accept: Let me go over this. You have a _type.seating_ for _num.guests_ _type.seating_ at _name.restaurant_ for tonight at _time.reservation_.   <!-- predicted: pizza_ordering.pizza_order.accept: okay _pizza_order.accept_ -->
* That is perfect. Thank you!
    - Youre welcome
* Bye for now.
    - Bye!


## dlg-200482b2-cbdb-49e0-b84a-d60d5135099f
* I need a favor. Will you please set me up an appointment at the mechanic shop called _name.store_?
    - Sure! Should I call or email them.
* Actually you can go right to their website and see the appointment availability in real-time. Just Google it.
    - general: Ohh thats awesome. Ok I got it. It wants to know what kind of car you have?   <!-- predicted: auto_repair.name.customer: Sure _name.customer_, let me check it for you. -->
* Its a _name.vehicle_
    - Ok and what year?
* Oh sorry its a _year.vehicle_.
    - Great got it. It wants to know whats wrong with it?
* _reason.appt_.
    - general: Uh oh. Ok I got it put in. What time slots should I put as your availability.   <!-- predicted: auto_repair.time.appt.accept: Oh dear. Let me see there is one at _time.appt_, can you make that? -->
* Just put all of them so I can see whats available quickest. Id like something in the _time.appt_ though.
    - auto_repair.date.appt_auto_repair.time.appt: Ok got it. It says that the first slot available is _date.appt_ at either _time.appt_ or _time.appt_.   <!-- predicted: auto_repair.time.appt: Yes, there is an appointment slot for _time.appt_. -->
* Sounds good. Put me in for the _time.appt_.
    - auto_repair.reason.appt: Ok just so you know it also says that the _reason.appt_ costs _price_   <!-- predicted: general: It appears so, we have the special partnership with the company. -->
* Ok got it.
    - auto_repair.date.appt_auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: So youre all scheduled for a _reason.appt_ at _name.store_ for _time.appt_, at _. Anythi_time.appt_se I can help you with?   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* No that will be it for now. Thank you.
    - Youre quite welcome. If you need anything else, call me.
* I will, thank you. Talk to you soon.
    - Ok bye.


## dlg-202a05ef-c14b-4686-9a8b-a9d91949f444
* Can you find out about a car repair appointment for me at _name.store_?
    - Where is the car right now and where do you want to take it?
* The car is parked at my house at _number_ Elm St..
    - general: Can you start the car?   <!-- predicted: coffee_ordering.location.store_coffee_ordering.location.store.accept: Okay. I am heading toward the Starbucks on _location.store_, should be there soon. -->
* _reason.appt_.
    - Do you need a tow truck?
* Yes. Ill need it towed to the shop.
    - What kind of car is it?
* Its a _year.vehicle_ _name.vehicle_.
    - general: When do you want to take it in?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* I want to take it in right now. Find out how quickly I can get an appointment?
    - auto_repair.date.appt_auto_repair.date.appt.reject_auto_repair.time.appt: The shop said they can look at the car _date.appt_ _time.appt_.   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_. -->
* Tell _name.store_ that I need them to look at it _date.appt_. I cant be without the car for long.
    - auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: _name.store_ said to bring it in by _time.appt_ and they can look at it _date.appt_.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: They cant get you in until _time.appt_. Is that okay? -->
* Thats good. Go ahead and make the appointment.
    - general: Do you need anything else?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: Ok. Today is _date.appt_. Can you come in _date.appt_ _time.appt_ -->
* Yes, How much is it going to cost to look at the car.
    - The inspection fee is _price_
* Thats fine.
    - auto_repair.appointment.accept_auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Ok, to confirm, _appointment.accept_ for _time.appt_ _date.appt_ for your _year.vehicle_ _name.vehicle_ to see _reason.appt_. _name.store_ will charge _price_ for the inspection.   <!-- predicted: auto_repair.appointment.accept_auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: so _appointment.accept_ at _name.store_ _date.appt_ at _time.appt_ for _reason.appt_. is there anything else? -->
* Ok. Got it.
    - action_listen: action_listen   <!-- predicted: general: Oh yeah, and preliminary inspection will cost _price_. -->


## dlg-1b2229fc-e011-455f-b067-95bdf91b37a3
* I would like to order a pizza from _name.store_ on _location.store_
    - general: Sure, what would you like?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* I want their _name.pizza_.
    - pizza_ordering.name.pizza: Do you mean the _name.pizza_?   <!-- predicted: pizza_ordering.type.topping.reject: Okay, just a seck. They say they are _type.topping_ You could either have it without or order something else. -->
* Yes.
    - pizza_ordering.size.pizza: What size would you like? It is available in _size.pizza_ and _size.pizza_ sizes.   <!-- predicted: pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.type.topping.accept: Ok.. _name.pizza_preference.accept_type.topping_preference.accept_type.topping_..what size? -->
* Let me order the _size.pizza_.
    - pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Sure thing. Unfortunately, they do not have _size.pizza_, but you can get the _size.pizza_.   <!-- predicted: general: can i get you any thing else can io offer you any drinks or sides we got great fried ravoli -->
* OK, how much is the _size.pizza_?
    - pizza_ordering.size.pizza: The _size.pizza_ is _price_   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* Do they allow additional toppings?
    - general: Although this is a specialty pizza, additional toppings can be added at _price_ for each topping.   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* I want _type.topping_ and _type.topping_ as well.
    - general: OK, is that all?   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->
* Yes, go ahead and order the pizzas.
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: OK, two _size.pizza_ _name.pizza_ with _type.topping_ and _type.topping_ will be ordered. Is that correct?   <!-- predicted: pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping.accept: A _type.crust_ _size.pizza_ size _type.topping_, _type.topping_type.topping_size.pizza_ pizza will cost _price_ plus tax. Would you like to order anything else? -->
* Yes.
    - general: OK, the pizzas have been ordered.   <!-- predicted: pizza_ordering.location.store_pizza_ordering.name.store_pizza_ordering.preference.accept_pizza_ordering.size.pizza_pizza_ordering.type.crust.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Great. So to confirm your order, you want two _size.pizza_ pizzas, both _type.crust_ with _preference.accept_. You want _type.topping_, _type.topping_, _type.topping_, and _type.topping_ on the first, and _type.topping_, _type.topping_, and black olives on the second, and you want to pick them up at the _name.store_ location on _location.store_. Does that all sound right? -->
* Send me the receipt.
    - The receipt will be sent to you via a text message to your mobile number on file.


## dlg-20350b85-fe63-47e8-aed7-cd10375e0883
* i wanna book a uber taxi for me , can you help me for this?
    - yeah, sure , whats your picking up point ?
* i am from _location.from_
    - general: okay good and whats your dropping location   <!-- predicted: uber_lyft.location.from: That is _location.from_ right? -->
* my dropping location is _location.to_
    - okay fine , how many persons are there with you ?
* there are _num.people_
    - okay fine , wait i will check it and tell you the information
* yeah , sure
    - what kind of ride do you want ? you have any idea about it
* yeah , i need _type.ride_ drive and its enough for us
    - sounds good, wait i will check it and i will show up you the information
* yeah sure , i will wait for it
    - uber_lyft.num.people.accept_uber_lyft.price.estimate.accept_uber_lyft.type.ride.accept: for _type.ride_ ride it takes _price.estimate_ for _num.people_ persons based on your far , is this okay for you ?   <!-- predicted: uber_lyft.time.pickup: _time.pickup_ if you want it now. -->
* it was good to hear, that was okay for me , can you please book a ride for us
    - yeah sure , wait i will confirm your booking
* yeah sure, and tell me arrival of the taxi time
    - uber_lyft.time.pickup.accept: your ride was booked and your drive will arrive within a _time.pickup_   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* thanks for your help ,have a nice day
    - you too have a safe ride , thank you using your assistant


## dlg-203edcf7-f6cc-4dfe-a836-f380e8ee0480
* _reason.appt_ - can you book an appointment to get my car fixed?
    - Of course, where would you like to have it fixed?
* _auto_repair.auto_repair_name.store_, please.
    - general: Great, when would you like the appointment?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _time.appt_. What is the earliest appointment?
    - auto_repair.date.appt_auto_repair.time.appt: It looks like the earliest appointment is _date.appt_ at _time.appt_   <!-- predicted: auto_repair.time.appt_auto_repair.time.appt.accept: They have an opening _time.appt_ or _time.appt_, at _time.appt_. -->
* Thats too late for me, I need to go to work. Can I drop the car off ahead of time?
    - Yes, you can. Do you need shuttle service to your office?
* Yes please.
    - general: Great, now what is the make, model and year of your car?   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Ive checked _name.store_ schedule. Times available _date.appt_ are _time.appt_, _time.appt_, _time.appt_, and _time.appt_. Which would you like? -->
* _year.vehicle_ _name.vehicle_
    - general: Ok, great, and what number can they call you at to confirm the appointment?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _number_-_number_-_number_
    - Ok great, and whose name should I put as the contact, you or your partner?
* Give them my name, _name.customer_.
    - general: Ok, Great.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Actually, hang on, could I drop the car off tonight instead?
    - Yes, I can arrange that.
* _reason.appt_?
    - I will add that to the work request.
* Ok great.
    - auto_repair.appointment.accept_auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: _name.store_appointment.accept_ for an _ appointment _. Yo_time.appt_t them to do _date.appt_reason.appt_yll cont_year.vehicle_y_name.vehicle_ at _number_-_number_-_number_ to _name.customer_e appointment. _ will cost _price_reason.appt_r hour diagnostic fees for the overheating problem.   <!-- predicted: auto_repair.time.appt: Upon checking, it looks like _time.appt_ is available. Is _number_ a.m. okay? -->
* Ok great! Thanks.
    - Youre welcome


## dlg-203f5b5d-9c06-4161-b707-d07a03a80de5
* Hey, Assistant. I need a lunch reservation.
    - restaurant_reservation.time.reservation: For _time.reservation_?   <!-- predicted: general: What film do you want to watch? -->
* Yes.
    - What time?
* _time.reservation_
    - Where would you like to have lunch?
* _name.restaurant_
    - How many will be dining with you?
* We have a group of _num.guests_ coming.
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests_restaurant_reservation.time.reservation: _name.restaurant_ has tables for _num.guests_ at _time.reservation_. Do you have any special requests?   <!-- predicted: restaurant_reservation.type.seating: Ok sir. Are you looking for _type.seating_ or _type.seating_ sitting -->
* Wed like to be served by Alice.
    - restaurant_reservation.name.restaurant: Im sorry, there is currently no server by the name of Alice at the _name.restaurant_ Would you like a different server?   <!-- predicted: restaurant_reservation.type.seating: They both have a _type.seating_ available, anything else? -->
* No, I changed my mind.
    - restaurant_reservation.type.seating: Do you still want to book a _type.seating_ for lunch?   <!-- predicted: general: Alright, youre all set. Enjoy your dinner! -->
* Yes, but at a different restaurant.
    - Which restaurant?
* _name.restaurant_
    - Would you like the same requests for this reservation?
* Yes.
    - Would you like to specify a server this time?
* No.
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating: Im sorry, but the _name.restaurant_ doesnt have any _type.seating_ available for _num.guests_ at _time.reservation_. Would you like to try a different time?   <!-- predicted: general: thank you for using chat bot -->
* No, Ill figure something else out.
    - Is there anything else I can help you with?
* No, thank you.
    - action_listen: action_listen   <!-- predicted: general: thank you for using chat bot -->


## dlg-2043f34f-0896-4836-a893-d8f204da46fc
* could you make an appointment at an _name.store_?
    - which city do you want?
* in _location.store_
    - when do you want your appointment?
* i want at _time.appt_ _date.appt_.
    - auto_repair.date.appt.accept_auto_repair.time.appt_auto_repair.time.appt.accept: it is not available. _time.appt_ is available _date.appt_ _time.appt_.   <!-- predicted: general: Im sorry to hear that, would you like me to schedule an appointment to bring it in? -->
* it is okay.
    - general: what is your cars model?   <!-- predicted: auto_repair.time.appt: Yes, the have a slot available around _time.appt_. Would you like me to book that? -->
* _name.vehicle_
    - what is your cars year?
* _year.vehicle_
    - general: what is your cars problem.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _reason.appt_
    - general: can you drive your car?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: It looks have your vehicle seen _time.appt_. You would need to drop it off and allow them to keep it overnight. -->
* yes. there are _reason.appt_.
    - general: can i get your number and name   <!-- predicted: auto_repair.time.appt: Upon checking, it looks like _time.appt_ is available. Is _number_ a.m. okay? -->
* _name.customer_ _number_
    - auto_repair.location.store.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: okay. your appointment for _reason.appt_ is at _location.store_ at _time.appt_ do you confirm it?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* yes please. thank you
    - general: your welcome   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: _name.customer_name.store_ _date.appt_time.appt_ure taking in your _year.vehicle_name.vehicle_reason.appt_e phone number I have listed it _number_-_number_ Is all of that information correct? -->


## dlg-20596b56-8819-4002-a8e4-f5779c10e294
* hi, can you get me _movie_ticket.movie_ticket_ for _name.movie_ _time.start_?
    - sure, what city would you like to see that in?
* i am in _location.theater_
    - movie_ticket.location.theater: is that in _location.theater_?   <!-- predicted: general: Okay, I show several theaters close by. Do you have a preference on which one you would like to go to? -->
* yes. _location.theater_
    - movie_ticket.name.movie: how many tickets for _name.movie_ would you like?   <!-- predicted: general: Okay, and when do you want to see the movie? -->
* _num.tickets_
    - movie_ticket.location.theater_movie_ticket.name.movie.reject: i dont show _name.movie_ playing in _location.theater_ today. would you like to see something else?   <!-- predicted: movie_ticket.time.start_movie_ticket.time.start.reject: Okay , they have tickets available _time.start_ , and _time.start_. -->
* is _name.movie_ playing anywhere?
    - movie_ticket.name.movie.accept: what time would you like to see _name.movie_?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* _time.start_ would be great
    - movie_ticket.time.start: there is a showing at _time.start_, would that be o.k.?   <!-- predicted: general: Do you need any accessibility devices tonight? -->
* is there an earlier showing than that?
    - movie_ticket.time.start.accept: i have a showing starting at _time.start_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* That would be better. lets do that one.
    - movie_ticket.location.theater.accept_movie_ticket.name.theater.accept: ok. it is playing at the _name.theater_ in _location.theater_. is there anything else?   <!-- predicted: movie_ticket.time.start: ok great, i have tickets booked for _time.start_, would you like reserved seating? -->
* no that will do it thank you.
    - movie_ticket.ticket_booking.accept: ok. _ticket_booking.accept_ shortly.   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* is that what i use for my tickets?
    - yes, you can just show it on the way in.
* thank you very much
    - you are welcome. enjoy your movie.
* goodbye
    - general: goodbye   <!-- predicted: action_listen: action_listen -->


## dlg-2072e527-2264-4c94-af58-cd8a49bbf5f6
* Hi there. I want to take _num.guests_ out for dinner. Can you make a reservation for me??
    - Sure. Where would you like to go?
* We are in _location.restaurant_. I have been wanting to go to _name.restaurant_ in _location.restaurant_.
    - general: Ok I will make a reservation. Is this for today? what time? How many   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* Yes for today, _time.reservation_. And there are _num.guests_. _num.guests_.
    - restaurant_reservation.num.guests: _num.guests_ Got that.   <!-- predicted: general: Great, let me check on that for you? -->
* Thanks!
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh boy. _time.reservation_ is all booked. How about and earlier time _time.reservation_??   <!-- predicted: restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: Youre welcome. We have that date and time available, but no _type.seating_ seating. Is there a different date you would prefer? -->
* Ok lets try that time.
    - restaurant_reservation.time.reservation.reject: Uhm, just tried that and _time.reservation_ just sold out.   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* Owch! What else can we do then?
    - restaurant_reservation.name.restaurant_restaurant_reservation.time.reservation: _name.restaurant_ is available for _time.reservation_ or _time.reservation_   <!-- predicted: general: No sir, the bar is first come first serve and it is mostly adult beverages. -->
* Ok lets go for _time.reservation_.
    - general: Ok booking now.   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* Great! How are we doing.
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: So I have a _time.reservation_ reservation for you at _name.restaurant_num.guests_time.reservation_ people.   <!-- predicted: general: The entire restaurant is a smoke-free establishment. -->
* Sounds great! Ive seen _name.restaurant_ before, but I dont think my daughter has.
    - Should be good for your family then. Have fun!
* Thanks we sure will! See you tomorrow!
    - general: See you tomorrow! Have a great night!   <!-- predicted: restaurant_reservation.location.restaurant.accept: It looks like _location.restaurant_, so itll be mall parking -->
* Thanks!
    - action_listen: action_listen   <!-- predicted: general: Youre welcome. Anything else I can assist you with? -->


## dlg-207f209c-4eef-4609-bac3-7b4c0b31faec
* Hello, I would like to place an order for pickup.
    - Okay, what would you like?
* I would like a _size.pizza_ _name.pizza_.
    - pizza_ordering.type.topping_pizza_ordering.type.topping.reject: Currently we are out of _type.topping_ for the pizza. We have _type.topping_, or _type.topping_ can be substituted for another vegetable.   <!-- predicted: pizza_ordering.type.topping.reject: Sorry we just ran out of _type.topping_, anything else interest you? -->
* _type.topping_ is fine.
    - general: Okay. Is there anything else you would like?   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->
* Yes, can I also get an order of chicken wings?
    - Okay, what size would you like?
* A small please.
    - Okay great. What sauce would you like on those?
* Mild sauce, please.
    - Any side sauces?
* Yes, Blue cheese sauce please.
    - Great. Anything else?
* Yes, I have a coupon for a personal pizza for free with any _size.pizza_ pizza purchase. Can I use that?
    - general: Yes of course. That comes with up to two toppings.   <!-- predicted: pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Yes, so you want a _size.pizza_ instead of _size.pizza_? -->
* Can I have _type.topping_ and _type.topping_?
    - Of course. Anything else?
* No, thats all.
    - Okay great. Do you have an account with us?
* Yes, I do. Under Jane Doe.
    - Okay great. Can we use the payment information on the account today?
* Yes, that works.
    - Great. Ill get that order in and processed for you, just one moment.
* Okay, Thank you.
    - Okay, that is all put in for you.
* Great. How long will it take?
    - Your order should be ready for pickup in about _number_ minutes
* Okay, thank you very much!
    - Have a great day.


## dlg-208f3643-131a-471e-a34b-1c8091091aa3
* Hello, can you please order me a pizza for tonight?
    - Hello! Yes, I would be happy to do so!
* Great, I would like to order a _size.pizza_ pizza.
    - pizza_ordering.size.pizza: All right, I can order a _size.pizza_ pizza for you. Where would you like me to place the order?   <!-- predicted: pizza_ordering.type.topping.reject: Ok, please give me a moment while I confirm the details of your order. Im sorry, the restaurant is out of _type.topping_. -->
* Please order it from _name.store_, in _location.store_.
    - pizza_ordering.location.store_pizza_ordering.name.store: Got it. _name.store_, in _location.store_. What is the street address, please?   <!-- predicted: general: Sure, let me check for availability, it make take a few minutes. Please be patient. -->
* It is located on _location.store_.
    - pizza_ordering.location.store.accept_pizza_ordering.name.pizza.accept_pizza_ordering.name.store.accept_pizza_ordering.size.pizza: All right, so you want a _size.pizza_name.pizza_name.store_ , at _location.store_. Is that correct?   <!-- predicted: pizza_ordering.pizza_ordering_pizza_ordering.type.topping_pizza_ordering.type.topping.reject: The location that you are picking up a _pizza_ordering.pizza_ordering_ from doesnt have _type.topping_, would you like another kind of pepper? -->
* Yes, thats right!
    - What would you like to order on your pizza?
* I would like _type.topping_ and _type.topping_, please.
    - pizza_ordering.size.pizza_pizza_ordering.type.topping: Okay, so thats a _size.pizza_ pizza with _type.topping_ and _type.topping_. Anything else on the pizza?   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* You know what, I think I would like _pizza_ordering.preference_, as well.
    - pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Great. I am ordering the _size.pizza_ pizza, with _type.topping_ and _type.topping_ and _preference.accept_ for you.   <!-- predicted: general: The fried calamari is _price_ and the _number_ buffalo wings are _price_ making your total so far _price_ before tax. -->
* Yes, thats it, exactly.
    - pizza_ordering.pizza_order.accept: Okay! _pizza_order.accept_ and will be ready for pick-up  in _number_ minutes!   <!-- predicted: general: Please hold while I place the order. -->
* Fantastic!
    - Your receipt will be sent to your mobile device as a text message.
* Thank you for your help!
    - My pleassure, have a nice night!


## dlg-20909f50-043e-400f-aee7-8f5243e16254
* Hi, Id like to book a table for _num.guests_name.restaurant_name.reservation_ in _location.restaurant_ this _time.reservation_
    - OK, how many total guests?
* Id like a table for _num.guests_ adults
    - general: Do you have any special requests?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* Yes, I would like a table on the _type.seating_.
    - restaurant_reservation.type.seating.reject: Im sorry, but _type.seating_ is not available for your requested daytimeparty   <!-- predicted: restaurant_reservation.type.seating.accept: I will add a _type.seating_ to your request -->
* OK, can I get a table in the _type.seating_?
    - restaurant_reservation.type.seating.reject: Im sorry, but _type.seating_  is not available for your requested daytimeparty   <!-- predicted: general: I may stop for a pizza myself on my way home -->
* OK, Id like to try a different restaurant
    - What restaurant would you like to reserve?
* _name.restaurant_ in _location.restaurant_
    - Would you like to try with the same options as previously requested?
* Yes
    - restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests_restaurant_reservation.type.seating_restaurant_reservation.type.seating.accept: Good news! _name.restaurant_num.guests_name.reservation_type.seating_   <!-- predicted: general: Alright, youre all set. Enjoy your dinner! -->
* Yes, I would like to reserve it
    - Excellent, _reservation.accept_. Would you like a confirmation text sent to your mobile phone?
* Yes, please send me a confirmation via text
    - general: Your confirmation has been sent. Would you like to make another reservation at this time?   <!-- predicted: pizza_ordering.type.topping.accept: _type.topping_ are available. I will add that as soon as possible. -->
* No thanks, maybe another time
    - OK, thank you for reserving through us. Have a good night!


## dlg-20926825-f8a4-4986-a02e-68bbed0b5046
* Hello, I would like to order a _size.pizza_ pizza.
    - general: Hello there, I can help you with that.   <!-- predicted: pizza_ordering.type.topping.reject: Ok, please give me a moment while I confirm the details of your order. Im sorry, the restaurant is out of _type.topping_. -->
* Sure, thanks!
    - No problem.
* I would like to order a _size.pizza_ _name.pizza_
    - Sounds good, I will include that in the order.
* I would like to add two different toppings.
    - general: What would these toppings be?   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* I would like to add _type.topping_ and _type.topping_.
    - Great, let me check them for you.
* Sure, thanks!
    - pizza_ordering.type.topping.reject: Youre welcome. Sorry, _type.topping_ are not available at the moment.   <!-- predicted: general: Restaurant A is about half the price as restaurant B -->
* No worries, what else is available?
    - pizza_ordering.type.topping: Other things are available like _type.topping_, _type.topping_, and etc.   <!-- predicted: general: They have several desserts available including chocolate lava cake. -->
* Sure, please add _type.topping_ as a substitute.
    - Awesome, that works. Anything else?
* No that is all for today.
    - You are welcome.
* When will order be ready?
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ and the pizzas will be ready for pickup in about _number_ minutes.   <!-- predicted: general: It will take _number_ minutes for pick-up. -->


## dlg-1b2f17f7-c42c-4b6c-bdea-d5c10403a735
* Could you please call me an Uber?
    - Sure, where would you like them to pick you up from?
* _location.from_
    - Okay, no problem. And where will they be dropping you off at?
* _location.to_
    - Okay great! What kind of fair are you wanting to use today?
* What are my options again?
    - uber_lyft.type.ride_uber_lyft.type.ride.accept_uber_lyft.type.ride.reject: You can ride _type.ride_, _type.ride_, _type.ride_, and _type.ride_.   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* How much would it be for _type.ride_?
    - uber_lyft.price.estimate: That would be _price.estimate_   <!-- predicted: uber_lyft.price.estimate.accept: The max price would be about _price.estimate_ before tip -->
* Oh wow. Okay. How much is just the _type.ride_?
    - uber_lyft.price.estimate.accept: That would be _price.estimate_.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Okay, I think I will go with that.
    - general: Okay great. Do you want me to order that now?   <!-- predicted: uber_lyft.ride_booking.accept: No problem dear customer. _ride_booking.accept_. The driver should be there shortly. -->
* Yes please. As soon as possible.
    - uber_lyft.ride_booking.accept: _ride_booking.accept_   <!-- predicted: general: Is there anythin else I can do? -->
* Thank you.
    - general: They will be there shortly.   <!-- predicted: uber_lyft.time.pickup.accept: Your uber will be arriving in _time.pickup_. Is there anything else I can do? -->
* Thank you very much. Have a nice day.
    - general: You too. Enjoy your pizza.   <!-- predicted: uber_lyft.time.pickup.accept: Your ride will be there in _time.pickup_. The details have been to your phone. Enjoy your stay at Charlotte -->


## dlg-209792a9-1891-4673-aea0-1cd40c50be27
* Hey can you schedule an appointment for my car?
    - Yes, with who?
* _name.store_. I think its having some _reason.appt_.
    - Okay, do you need a replacement?
* Im not sure, I just want to get it checked out?
    - general: Whats happening to it?   <!-- predicted: coffee_ordering.coffee_order.accept_coffee_ordering.location.store.accept: Okay sounds good. _coffee_order.accept_ and is being made now. You can pick it up at the Starbucks on _location.store_ in a few minutes. You should be receiving your receipt through text now. -->
* _reason.appt_ recently.
    - auto_repair.reason.appt: Are you sure its not the _reason.appt_?   <!-- predicted: general: That sounds scary. Do you want me to see if I can make an appointment for you to bring it in? -->
* Yes, I had someone look at it and they were pretty sure _reason.appt_.
    - general: Okay, which make is the car?   <!-- predicted: auto_repair.name.store: Will do!-- later-- _name.store_ just spoke with me, bring the car in right now; but -->
* It is a _name.vehicle_.
    - general: What year?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: Okay they have an opening _date.appt_ at _time.appt_. -->
* _year.vehicle_
    - general: And what day would you like to book?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _time.appt_ this week. what days do they have?
    - auto_repair.date.appt: they have openings pretty much all week _date.appt_ thru _date.appt_.   <!-- predicted: general: He is coming in a white honda civic. -->
* I need _date.appt_ _time.appt_?
    - they dont have any til _time.appt_
* okay i guess thats fine
    - auto_repair.name.vehicle.accept_auto_repair.reason.appt_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: okay so thats an _reason.appt_year.vehicle_time.appt_ _name.vehicle_orrect?   <!-- predicted: general: Is the car otherwise functioning normally? -->
* yes, how much is it?
    - Okay, the initial inspection will be _price_
* Okay thanks.
    - just put your full name?
* Yeah, _name.customer_
    - general: Okay Got it and which phone number   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _number_-_number_-_number_ thanks
    - auto_repair.date.appt.accept_auto_repair.time.appt.accept: no problem, its scheduled, _date.appt_ _time.appt_   <!-- predicted: general: Thank you so much i can send you a recipt via text message or email whaich do you prefer -->
* Thanks so much! Bye
    - bye


## dlg-209856e2-3ec2-464c-bbc5-f6013d138ebb
* Im feeling kinda fishy!
    - Huh?
* Whats that fancy fish place I told you to remember I liked?
    - restaurant_reservation.name.restaurant: _name.restaurant_ and _name.restaurant_   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* Wow your good. Will you book me a table _time.reservation_ for _num.guests_ at _name.restaurant_? That was the one in _location.restaurant_ right?
    - general: Yes, and of course.   <!-- predicted: restaurant_reservation.type.seating: Ok sir. Are you looking for _type.seating_ or _type.seating_ sitting -->
* Thank you, and have a good night!
    - restaurant_reservation.name.restaurant.reject: One second.. Sorry but theres no openings at all tomorrow night at _name.restaurant_. I could possible call and put you on a standby, but youd be waiting in doorway bench for unknown amount of time   <!-- predicted: restaurant_reservation.location.restaurant: It is about _location.restaurant_r. -->
* No! _time.reservation_?
    - Im sorry, but nothing for tomorrow at all. Theres a festival coming to the Red Barons stadium, theyre sold out until Monday.
* Crap, well thats lame. What about _name.restaurant_ for tomorrow?
    - restaurant_reservation.location.restaurant_restaurant_reservation.location.restaurant.reject_restaurant_reservation.name.restaurant.reject: _location.restaurant_name.restaurant_ booked but theres several openings _location.restaurant_ Location.   <!-- predicted: general: They have several desserts available including chocolate lava cake. -->
* That works, Im actually picking her up from _location.restaurant_, hadnt thought of that one.
    - restaurant_reservation.location.restaurant.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: Awesome, confirmed for tomorrow night at _name.restaurant_ in _location.restaurant_ at _time.reservation_, table of _num.guests_.   <!-- predicted: restaurant_reservation.time.reservation: Also Im looking at the current reservations, is it possible to move to _time.reservation_? -->
* Amazing, how did you do that so quickly?
    - I just turn on google voice text and read you the answers from the screen it used your voice to search for.
* Laughs, no serious. How?
    - general: Here Ill turn up the volume so you can hear yourself. Ask something.   <!-- predicted: restaurant_reservation.time.reservation: I see _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_ and _time.reservation_ as available. -->
* WHos your daddy?
    - Google search voice. Technically speaking, that would be Bill Gates, founder of Microsoft.


## dlg-20a9db4d-c596-4ec0-9202-b2e899e19259
* Hi Julia! Could you help me buy a ticket for the movie _name.movie_?
    - Sure thing. Which city is the movie plan in?
* It is playing in _location.theater_.
    - movie_ticket.name.movie_movie_ticket.time.start: Okay. I see _name.movie_ playing at _time.start_.   <!-- predicted: movie_ticket.location.theater_movie_ticket.name.theater: I see it is playing at the _name.theater_ in _location.theater_. -->
* Thats great. Is it _type.screening_?
    - It sure is! Do you want to buy It?
* Yes, but can you buy _num.tickets_ of them?
    - Sure thing. However, do you want to go to the dine in movie theater?
* Let me think about that.
    - It is only about half a mile from the other theater.
* That sounds like a good plan.
    - general: Yeah, that way you dont have to find a place to eat.   <!-- predicted: movie_ticket.name.movie.accept_movie_ticket.time.start.accept: I will do. Setting a reminder _number_ hour before _time.start_ for the _name.movie_ Movie. -->
* Ok, lets go with that.
    - movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept: Ok, I will buy _num.tickets_ tickets for _name.movie_ at the _name.theater_.   <!-- predicted: general: OK, just confirmed with your driver. -->
* It is at _time.start_ right?
    - movie_ticket.price.ticket_movie_ticket.price.ticket.accept: That is correct. It will cost _price.ticket_ each ticket.   <!-- predicted: general: It appears so, we have the special partnership with the company. -->
* Whoa! That is a lot.
    - movie_ticket.type.screening.accept: Yes sir, _type.screening_ tickets are more expensive.   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Okay, you can use my online account to earn rewards.
    - general: I will do that. Okay. I have purchased the tickets. You should get a text message with you tickets.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Thank you very much. I have received them.
    - general: You are welcome.   <!-- predicted: auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_ will cost around _price_ _reason.appt_ costs _price_ -->
* Have a great day!
    - general: You too.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->


## dlg-20ab0cf1-e613-48da-b786-a94c33c09f11
* I need a Lyft.
    - Picking up from?
* _location.from_.
    - Going to?
* _location.to_.
    - How soon would you like a ride?
* ASAP.
    - uber_lyft.type.ride: You have two options _type.ride_ and _type.ride_.   <!-- predicted: general: Uber offers a broad range of prices. -->
* How much is the _type.ride_ option?
    - uber_lyft.price.estimate_uber_lyft.type.ride: The _type.ride_ option costs _price.estimate_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* How many other pickups?
    - Maximum of _number_ or _number_
* How soon can they get here?
    - uber_lyft.time.pickup: _time.pickup_.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* What about the _type.ride_ option?
    - uber_lyft.time.pickup.accept: Youll be picked up in _time.pickup_   <!-- predicted: general: they can reach you at _number_ _number_ -->
* How much?
    - uber_lyft.price.estimate.accept: Cost is _price.estimate_.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Ill take the _type.ride_ option.
    - okay.
* Thanks!
    - Anything else?
* No.
    - Got it!


## dlg-20aeb7f6-a1f4-40cf-be55-9403257f79c7
* Will you please order me lunch?
    - Sure thing.
* Thanks
    - What do you have in mind?
* I am thinking pizza.
    - That sounds delicious.
* I agree. I am very hungry.
    - Which pizza place.
* The _name.store_ in _location.store_
    - Ok. What toppings would you like?
* I would actually like _name.pizza_
    - What size?
* _size.pizza_
    - pizza_ordering.name.pizza_pizza_ordering.name.pizza.reject_pizza_ordering.name.store.accept_pizza_ordering.type.topping.reject: I am sorry sir, _name.store_ is all out of _type.topping_ for the _name.pizza_   <!-- predicted: pizza_ordering.size.pizza: Will both Pizzas be _size.pizza_? -->
* Bummer
    - general: Would you like something else.   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->
* _name.pizza_type.topping_type.topping_ pizza.
    - general: Same size?   <!-- predicted: pizza_ordering.preference_pizza_ordering.preference.reject: _pizza_ordering.preference_preference.reject_? -->
* Yes
    - pizza_ordering.pizza_order.accept: Ok. _pizza_order.accept_. It will be ready for pickup in _number_ minutes.   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->


## dlg-20b13528-7727-4e8c-ac3b-c4765322ec22
* Hi. Id like to order a drink from Starbucks.
    - What location do you want to order it from?
* Id like to order it from the location on _location.store_
    - general: Okay. And what would you like to order?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* _name.drink_location.store_.
    - general: What size would you like?   <!-- predicted: pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.type.topping.accept: Ok.. _name.pizza_preference.accept_type.topping_preference.accept_type.topping_..what size? -->
* Id like to get a _size.drink_.
    - general: And is there a particular type of milk that you prefer?   <!-- predicted: coffee_ordering.name.drink: Sure, they have _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, and _name.drink_. -->
* Id prefer _type.milk_.
    - And would you like _coffee_ordering.preference_ on it?
* Yes, Id like that.
    - general: Is that everything?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ok, _num.drink_ _preference.accept_, _, _size.drink_ a_type.milk_type.milk_preference.accept_ -->
* Yes, thats it.
    - coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Okay, so I have _num.drink_ _size.drink_ _name.drink_ with _type.milk_ and _preference.accept_.   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.reject: _coffee_ordering.preference_preference.reject_ available. Would you like to remove it or choose something else? -->
* That is correct.
    - coffee_ordering.coffee_order.accept: _coffee_order.accept_.   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* Thank you.
    - It should be ready for pickup shortly and your receipt will be sent to your mobile device via text message.
* Okay, thank you.
    - Have a wonderful day.
* You too!


## dlg-20b42130-2aae-489b-8563-296748118150
* Hi I would like to place an order for pickup
    - Sure, What would you like?
* Id like to order one _size.pizza_ _name.pizza_
    - Great, that requires two toppings, what would you like?
* How come?
    - general: It is part of our monthly special and youll actually save money   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* Oh thanks for letting me know!
    - No problem! What would you like?
* Ill have _type.topping_ and _type.topping_
    - pizza_ordering.type.topping.reject: Sorry sir we are out of _type.topping_   <!-- predicted: general: CHECKING..... -->
* Ugh that stinks!
    - pizza_ordering.type.topping: We do have _type.topping_ and that is a good alternative   <!-- predicted: pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Okay, so thatt a _size.pizza_., _type.topping_, _type.topping_ and _type.topping_ pie. -->
* Okay that will work
    - Would you like anything else?
* Sure, one bottle of pepsi
    - We have coke, is that okay?
* I suppose
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Perfect! so to confirm you are ordering one _size.pizza_ _name.pizza_ with _type.topping_ and _type.topping_   <!-- predicted: general: I just talked to the pizza parlor. -->
* Yep!
    - Great, give us _number_ minutes and the order will be ready
* See you then!
    - action_listen: action_listen   <!-- predicted: general: Did you receive the text l sent you with the receipt? -->


## dlg-20b8c855-ded8-4c2f-8c88-8e27a31da9a6
* Alexa, find me a reservation for _name.restaurant_ in _location.restaurant_ for tonight
    - How many people do you want for the reservation?
* I want a reservation for _num.guests_ people
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests_restaurant_reservation.num.guests.reject: There are no tables left for _num.guests_ people at _name.restaurant_ for tonight. Would you like to change the number of people   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* Yes I would like to change it to _num.guests_ people
    - restaurant_reservation.num.guests.accept_restaurant_reservation.type.seating: There are _type.seating_s for _num.guests_ people. Would you like a _type.seating_ or table?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* I would like a _type.seating_
    - general: What time would you like the reservation to be?   <!-- predicted: restaurant_reservation.time.reservation: I see _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_ and _time.reservation_ as available. -->
* I would like it for _time.reservation_ tonight
    - restaurant_reservation.type.seating: Would you like _type.seating_ or _type.seating_?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* I would like _type.seating_
    - general: Is the reservation for tonight?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* Yes it is
    - general: What should I put the reservation name under?   <!-- predicted: pizza_ordering.type.topping.accept: _type.topping_ are available. I will add that as soon as possible. -->
* _name.reservation_ please
    - restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.time.reservation.accept: I have made a reservation for _name.restaurant_ under _name.reservation_ for _time.reservation_ tonight   <!-- predicted: restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: _name.restaurant_name.reservation_ for _ people at _, and it_num.guests_looks like _time.reservation_o have a _. Your reservation ha_type.seating_n set. Anything else? -->
* Thank you
    - Would you like to make another reservation?
* No thanks. Thats all please.
    - No problem.


## dlg-20b97e53-ca8a-4df0-b770-bd6798cdd02c
* Hey, I need to get my car looked at.
    - I can help you with that. For what kind of car to you need service?
* Its for _year.vehicle_ _name.vehicle_ And I want to go to _name.store_.
    - When would you like an appointment?
* Sometime _date.appt_ would be good.
    - general: OK, and what kind of service do you require.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: They will take it at _time.appt_ otherwise they cant take it until _date.appt_. -->
* Well, _reason.appt_.
    - auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _._time.appt_ -->
* That should work... Wait a minute -- now theres _reason.appt_. Can you get me in right away?
    - auto_repair.date.appt_auto_repair.date.appt.accept_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ has an opening at _time.appt_. _date.appt_, three hours from now.   <!-- predicted: auto_repair.time.appt: Yes, there is an appointment slot for _time.appt_. -->
* I guess Ill have to take that.
    - auto_repair.name.store_auto_repair.time.appt: OK, I am scheduling an appointment at _time.appt_. at _name.store_.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt: Okay, it says that you are booked to get checked out at _time.appt_ _date.appt_. -->
* Any idea how much this will cost?
    - auto_repair.name.store_auto_repair.reason.appt: A _reason.appt_ fee of _price_ is charged at _name.store_. If a problem is detected, that fee is credited toward the final bill.   <!-- predicted: general: The total is $XX.XX. May I have your information to process the payment? -->
* OK. Thats acceptable.
    - auto_repair.name.store_auto_repair.time.appt: Your appointment at _name.store_ is confirmed for _time.appt_. Will you be wait while service is done or will you need a shuttle.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* I guess Ill wait. Do they have WiFi there?
    - auto_repair.name.store: _name.store_ has a full waiting area with refreshments, work space, and free WiFi.   <!-- predicted: auto_repair.time.appt.accept: See you at _time.appt_ after those two calls. -->
* Great. Thanks!
    - auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Youre welcome. To confirm, you have a _time.appt_. appointment at _name.store_ for service on your _year.vehicle_ _name.vehicle_. The minimum cost will be _price_ for _reason.appt_. Goodbye!   <!-- predicted: general: You’re welcome. Good luck. -->


## dlg-20c2c8f3-e20a-4fd6-b7e1-ee3cabc674dc
* Hi Cammy, I need a suggestion for a few local restaurants that are good. Do you have any suggestions?
    - general: Sure, do you have a preference or type of cuisine in mind?   <!-- predicted: restaurant_reservation.location.restaurant.accept: Sure, Ive already found five here in _location.restaurant_ City. -->
* I like Hibachi and Seafood
    - general: What area will you be in?   <!-- predicted: uber_lyft.type.ride: The _type.ride_ is fairy cheaper than _type.ride_. -->
* I will be in the _location.restaurant_ by the _location.restaurant_. I have some business associates flying in.
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: There is a _name.restaurant_ in _location.restaurant_, as well as a seafood restaurant called _name.restaurant_. Both have great reviews.   <!-- predicted: restaurant_reservation.name.restaurant.reject: Sorry, _name.restaurant_ is closed for a private party. -->
* Awesome, and how close are they to the beach?
    - restaurant_reservation.location.restaurant: They are both located on the _location.restaurant_ and have views of the water. They are each about _location.restaurant_.   <!-- predicted: uber_lyft.time.pickup: The current wait time is _time.pickup_. -->
* Does either have live music? I think the partners would like some kind of entertainment.
    - restaurant_reservation.name.restaurant: _name.restaurant_ does on weekends and some weeknights. _name.restaurant_ offers a show with dinner, as your chef prepares the meal in front of you, displaying fun culinary tricks.   <!-- predicted: general: Of course, they are really accomodating to special diets and requests. They even have an entirely gluten-free menu. -->
* I like the sound of that but sea food is probably the way to go. I think I would like to book with _name.restaurant_.
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.accept_restaurant_reservation.type.seating: _name.restaurant_ has availability and they can seat you _type.seating_ with an ocean view or you can eat _type.seating_, with intracoastal views.   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* I would like to sit _type.seating_ and I just found out there might be some more people coming.
    - restaurant_reservation.num.guests_restaurant_reservation.time.reservation: Sure, so we are booking the outside table for _num.guests_, Friday March _number_th, at _time.reservation_?   <!-- predicted: restaurant_reservation.time.reservation: Also Im looking at the current reservations, is it possible to move to _time.reservation_? -->
* There will be a total of _num.guests_ in our party now. Is that ok?
    - restaurant_reservation.num.guests_restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating: They dont have availability for _num.guests_ at that _time.reservation_ _type.seating_. You could eat _type.seating_ at that time or bump the reservation to _time.reservation_ and still sit outside?   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* Yes, lets go with the later reservation because its worth it to be on the water.
    - general: Ok, is there anything else I can assist you with?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* In case we arrive early, do they have a _type.seating_?
    - Yes, they have a fully stocked sit down bar with premium wines and liquors.
* Perfect. Thank you.
    - restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Ok, so we have an _type.seating_ waterview _type.seating_ for _num.guests_, reserved for Friday, March _number_th at _time.reservation_. Please check your text messages as the confirmation of reservation will be sent via text   <!-- predicted: general: Youre welcome enjoy your dinner. -->
* Thank you for all of your help with this matter. I will talk to you soon.
    - No problem, enjoy your evening and I will talk to you soon. Goodbye.
* Bye Bye.


## dlg-1b35767a-2396-4f13-98e8-c0eeec6e2d12
* Wed like to eat Mexican tonight. There is _name.restaurant_ and _name.restaurant_, both _location.restaurant_.
    - Okay Ive pulled up some information about them, what are you looking for?
* Id like the one where we have a _type.seating_
    - restaurant_reservation.type.seating: They both have a _type.seating_ available, anything else?   <!-- predicted: general: Great, let me check on that for you? -->
* Id like one with a TV so I can watch the game while we eat.
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.accept: Alright _name.restaurant_ has a TV available, but not _name.restaurant_.   <!-- predicted: general: Of course, they are really accomodating to special diets and requests. They even have an entirely gluten-free menu. -->
* We need a _type.seating_ for _num.guests_ at _time.reservation_, _type.seating_.
    - restaurant_reservation.time.reservation: Im sorry it looks like they have one available for _time.reservation_ or _time.reservation_.   <!-- predicted: restaurant_reservation.type.seating: Excellent, would you prefer a _type.seating_ or _type.seating_? -->
* Well take the _time.reservation_.
    - restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: And it looks like they dont have an _type.seating_ at that time. Is _type.seating_ okay or at a _type.seating_?   <!-- predicted: restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: _name.restaurant_name.reservation_ for _ people at _, and it_num.guests_looks like _time.reservation_o have a _. Your reservation ha_type.seating_n set. Anything else? -->
* What about a _type.seating_?
    - restaurant_reservation.num.guests.accept_restaurant_reservation.type.seating.accept: That will work, they have a _type.seating_ that seats _num.guests_.   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: I apologize, but they dont have any _type.seating_ available on that date at _time.reservation_. -->
* Sounds good, what kind of specials do they have?
    - general: There is the Bull Fighters platter for _number_ or Endless Enchiladas for _number_.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Okay what about kids choices.
    - They have a chicken and rice bowl with tamales and dipping sauce.
* Okay my wife likes spicy food, what do they have.
    - They have habanero chimichangas and red hot burritos smothered in green sauce.
* Okay that all sounds good, thanks.
    - Youre welcome, enjoy your dinner.


## dlg-20c8ff90-42ac-4fd4-af4c-5aa2517069c6
* I need a _restaurant_reservation.restaurant_reservation_ at a nice restaurant near here that has seafood. What do you recommend?
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: _name.restaurant_ _location.restaurant_ is very nice and gets fresh seafood daily.   <!-- predicted: restaurant_reservation.name.restaurant: Ive searched the area, theres a _name.restaurant_ not too far from your office -->
* Perfect, please get me a _restaurant_reservation.restaurant_reservation_ there for tomorrow _time.reservation_, Thursday, March _number_
    - What time would you prefer?
* Id like to eat at _time.reservation_.
    - Will anyone else be dining with you?
* Yes, my husband. So, _num.guests_ people total.
    - restaurant_reservation.type.seating: Okay. Would you like to eat _type.seating_ or _type.seating_?   <!-- predicted: general: What kind of table would you prefer? -->
* Id like to eat _type.seating_ at a _type.seating_.
    - I apologize, but they dont have any _type.seating_ available on that date at _time.reservation_.
* Oh, well what about at _time.reservation_?
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: They still dont have _type.seating_ available at _time.reservation_.   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* Okay, well then what other seafood restaurants are in the area?
    - restaurant_reservation.name.restaurant: _name.restaurant_ is also very good. It is located close by and they also get fresh seafood daily.   <!-- predicted: restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.accept_restaurant_reservation.time.reservation: _name.restaurant_ Sunday brunch starts at _time.reservation_ -->
* Okay, see if you can get me a reservation there please.
    - restaurant_reservation.type.seating: Do you still want to eat at a _type.seating_ _type.seating_?   <!-- predicted: general: No, they do not do that, but there is a splendid African restaurant about _number_ miles from here. They serve great East and West African dishes. -->
* Yes, I would prefer that.
    - restaurant_reservation.time.reservation: Do you want the the _time.reservation_ or _time.reservation_ reservation?   <!-- predicted: restaurant_reservation.reservation.accept: Okay, _reservation.accept_, sir. -->
* Id like it at _time.reservation_ if possible.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Alright, _reservation.accept_ for _num.guests_ at _time.reservation_ at _name.restaurant_ at a _type.seating_.   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.type.seating.accept: Ok it looks like they have have that time slot available _type.seating_ at _name.restaurant_ I will reserve that time slot. -->
* Thank you very much.
    - action_listen: action_listen   <!-- predicted: general: Youre welcome enjoy your dinner. -->


## dlg-20d9db60-f878-4ac5-b1d7-0251deae7ad0
* i want to order a coffee from starbucks
    - general: ok. which starbucks location?   <!-- predicted: coffee_ordering.location.store: The closest Starbucks location is _location.store_. What would you like to order? -->
* _location.store_
    - there is actually more than one starbucks in burlington. do you have a preference which one?
* _location.store_.
    - coffee_ordering.location.store.accept: _location.store_.   <!-- predicted: general: What size for the drink? -->
* great
    - general: what would you like?   <!-- predicted: coffee_ordering.name.drink: Can i suggest the _name.drink_ ? Its currently being featured. -->
* a _name.drink_
    - what flavor?
* _coffee_ordering.preference_name.drink_
    - general: what size?   <!-- predicted: pizza_ordering.preference_pizza_ordering.preference.reject: _pizza_ordering.preference_preference.reject_? -->
* a _size.drink_, please
    - general: what type of milk would you like?   <!-- predicted: coffee_ordering.preference.reject: Any _preference.reject_ -->
* _type.milk_
    - coffee_ordering.type.milk.accept: _type.milk_.   <!-- predicted: general: Any foam? -->
* excellent
    - would you like anything else?
* no thank you
    - coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: _size.drink_name.drink_preference.accept_type.milk_name.drink_ at the starbucks located at _location.store_s.   <!-- predicted: general: Would you like any flavors added to that? -->
* great
    - general: you will be receiving a text message on your cell phone with details of this order.   <!-- predicted: coffee_ordering.coffee_order.accept_coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_restaurant_reservation.num.guests.accept: _coffee_order.accept_num.drink_num.guests_ _preference.accept_size.drink_name.drink_location.store_ -->
* perfect. thank you. goodnight


## dlg-20e30538-a316-413e-bba6-e8f803b4cd3d
* I would like to look into more information about booking a table at _name.restaurant_ or _name.restaurant_ _location.restaurant_.
    - restaurant_reservation.name.restaurant: _name.restaurant_ really requires reservations while _name.restaurant_ doesnt.   <!-- predicted: general: Okay, Id be happy to. How many pizzas do you want? -->
* I would like to get a table at _name.restaurant_ _time.reservation_.
    - general: There are no tables left then.   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* How about _time.reservation_?
    - Yes, I can do that. For how many?
* _num.guests_
    - restaurant_reservation.type.seating: They have _type.seating_ - which would you prefer?   <!-- predicted: general: What kind of table would you prefer? -->
* _type.seating_ would be great. Do they have a gluten free menu?
    - Yes, they do have gluten free options.
* Do they have drink specials on the date we picked?
    - Yes, there is a top shelf happy hour from _number_pm-_number_pm.
* Perfect. Are there are any dinner specials?
    - They run daily dinner specials but do not post about them online.
* Thank you. Can you send an invite to my friends in messenger?
    - Yes, who do you want to send this to?
* I would like to send it to everyone on my favorites list, please.
    - That can be done. Anything else?
* No, that is all.
    - Okay, let me know if you need to me change anything.


## dlg-20e512d5-51c3-4a3d-a551-c088090a97ac
* i would like you to purchase _num.tickets_ for the movie _name.movie_name.theater_location.theater_ for _time.start_ tonight
    - general: that movie has sold out for that time tonight and that was the last showing tonight   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: _name.theater_num.tickets_name.theater_time.start_name.movie_location.theater_ -->
* ok how about _name.movie_ _location.theater_ _ for _number_pm_num.tickets_
    - movie_ticket.time.start_movie_ticket.time.start.reject: they have a showing at _time.start_   <!-- predicted: movie_ticket.location.theater_movie_ticket.location.theater.accept: This movie isnt playing in _location.theater_ but it is playing in _location.theater_. -->
* that would be ok
    - movie_ticket.time.start: that one is sold out the next showing is at _time.start_   <!-- predicted: general: It appears that there are tickets available. How many tickets do you want to purchase? -->
* that is too late is there any other times
    - general: i will check   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* ok thanks
    - general: that one is also sold out is there any other movies you would see instead   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* let me look give me a few minutes
    - general: that is fine   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: _name.theater_num.tickets_name.theater_time.start_name.movie_location.theater_ -->
* how about _name.movie_ at the same theater as _name.movie_
    - let me check
* thank you
    - general: that one only has earlier showings   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* are you series
    - yes no later showing for tonight
* ok im not meant to go to the movies tonight i a not going to purschase any
    - ok sorry.
* its not your fault. maybe we can have dinner instead
    - great goodnite
* goodnite to you too
    - ok


## dlg-20e717b0-8b53-4125-ae12-e2900f93f23f
* Hi Jess. _num.tickets_ were talking about seeing _name.movie_ at the movies tonight.
    - movie_ticket.location.theater_movie_ticket.location.theater.accept: Ok, in _location.theater_?   <!-- predicted: general: ok, may be hard to find. Will try and let you know -->
* Yeah, can you buy tickets for us?
    - Sure, what theater and time?
* Hopefully _time.start_, and the _location.theater_.
    - Alright let me look it up.
* Thanks. Also, get it in _type.screening_, that would be awesome!
    - Ok, Ill get back to you in a minute.
* k
    - movie_ticket.name.theater.accept_movie_ticket.time.start: Well, it looks like I can get you tickets, for a discount with our member card actually! But it has to be the _time.start_ showing at _name.theater_.   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: i have _num.tickets_ to _name.movie_ at _time.start_ in _location.theater_ -->
* Aw, they dont have any times later?
    - general: Not for the discount we have.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Bummer we would have to leave the conference early. How much are tickets regularly.
    - movie_ticket.price.ticket: It would be _price.ticket_ without the discount.   <!-- predicted: general: Is your friend an adult or senior? In case they have a senior discount. -->
* wow!
    - general: Plus, I bet youll want to see that movie earlier than later... its SCARY!!   <!-- predicted: movie_ticket.name.movie_movie_ticket.name.movie.reject_movie_ticket.name.theater_movie_ticket.time.start_movie_ticket.type.screening_movie_ticket.type.screening.reject: Ok, I checked and they said that _name.movie_ wasnt in _type.screening_ but if you were interested _name.movie_ will be tomorrow at the _name.theater_ at _time.start_ same price as the other selections. -->
* Haha, ok book them.
    - movie_ticket.type.screening.reject: Oh, also its not in _type.screening_.   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_ and emailed to your email address -->
* Anywhere?
    - general: It doesnt look like it, sorry.   <!-- predicted: movie_ticket.name.movie_movie_ticket.name.movie.reject_movie_ticket.name.theater_movie_ticket.time.start_movie_ticket.type.screening_movie_ticket.type.screening.reject: Ok, I checked and they said that _name.movie_ wasnt in _type.screening_ but if you were interested _name.movie_ will be tomorrow at the _name.theater_ at _time.start_ same price as the other selections. -->
* Ok, I want to see it anyway. Book them.
    - movie_ticket.name.movie.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: Alright _num.tickets_ tickets for _name.movie_ are booked for _time.start_ today. Youll get a confirmation text on your phone.   <!-- predicted: movie_ticket.price.ticket.accept: Ok, that will be _price.ticket_, Ill charge your account? -->
* Thanks!


## dlg-20f3c001-b0cb-482e-8d16-885fc3acdffc
* hi there becky i need your help
    - yes how can i help you?
* can you order a pizza from me from _name.store_?
    - pizza_ordering.location.store: yeah of course the one on the _location.store_ sir?   <!-- predicted: general: sure! how big would you like it? -->
* yes the _location.store_
    - what would you like?
* i want two _size.pizza_ _name.pizza_
    - pizza_ordering.name.pizza_pizza_ordering.size.pizza_pizza_ordering.size.pizza.accept: okay two _size.pizza_ _name.pizza_   <!-- predicted: general: Ok great, give me a minute here please -->
* and that bread that i like, what is it called
    - general: the crazy bread?   <!-- predicted: coffee_ordering.preference.accept: The _preference.accept_ is an extra dollar. -->
* yes the crazy bread.
    - okay what else?
* i want a pound of chicken wings
    - general: and what flavor do you want?   <!-- predicted: pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Okay. Ive got a _size.pizza_ pizza with _type.topping_, _type.topping_, _type.topping_preference.accept_type.topping_. its that correct? -->
* lets do lemon parmeson
    - okay and ranch with that?
* yes please
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept: okay so that is two _name.pizza_ _size.pizza_ pizzas with lemon pepper wings and crazy bread   <!-- predicted: general: OK, is that all? -->
* yes that is exactly what i want
    - okay the receipt is going to your phone as a text and itll be ready for pickup
* when do i pick it up?
    - in _number_ minutes
* okay thank you
    - thank you bye bye


## dlg-21006923-8675-4ca6-bc4c-12a3b059fec8
* I would like to order a _pizza_ordering.pizza_ordering_ form _name.store_ in _location.store_.
    - What type of pizza would you like?
* I would like to create _size.pizza_.
    - What toppings would you like?
* _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, and _type.topping_.
    - pizza_ordering.type.topping.reject: Im sorry, _type.topping_ and _type.topping_ are currently unavailable.   <!-- predicted: general: Is the meat extra or regular serving? -->
* Do you have _type.topping_?
    - Yes.
* What kind of sauce comes on the pizza?
    - pizza_ordering.preference: _pizza_ordering.preference_ and _pizza_ordering.preference_?   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* Do you have _preference.reject_?
    - No.
* What kind of cheese do you have?
    - pizza_ordering.preference_pizza_ordering.type.topping: _type.topping_pizza_ordering.preference_type.topping_pizza_ordering.preference_.   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* Can I have one _size.pizza_type.topping_pizza_ordering.preference_, _type.topping_type.topping_type.topping_type.topping_and _type.topping_
    - pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: I have one _size.pizza_type.topping_preference.accept_, _type.topping_type.topping_type.topping_type.topping_and _type.topping_   <!-- predicted: pizza_ordering.type.topping.reject: Okay, just a seck. They say they are _type.topping_ You could either have it without or order something else. -->
* Yes.
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ and will be available for pickup in _number_ minutes.   <!-- predicted: general: ok, your total will be _price_ is there anything else you would like? -->
* Thanks
    - Youre welcome.


## dlg-210c3d00-ac32-4ce4-b928-9807cfb544c8
* Id like to get a _name.store_ please.
    - general: Not a problem! What size are you looking for?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* Whats the smallest youve got, for like one person?
    - pizza_ordering.name.pizza: We have a _name.pizza_, if that would work.   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* Yes, thats great. Oh! And do you have _pizza_ordering.preference_?
    - pizza_ordering.preference: We have a _pizza_ordering.preference_ dough option, yes, though its not safe for celiac.   <!-- predicted: general: Im not sure, let me finish entering the details and Im sure I can let you know. -->
* Thats fine, just _pizza_ordering.preference_ works.
    - general: Great. What toppings can I get for you?   <!-- predicted: pizza_ordering.pizza_ordering: What type of _pizza_ordering.pizza_ordering_ do you want to order? -->
* Can I get _type.topping_ and _type.topping_?
    - pizza_ordering.type.topping: We can do _type.topping_, but Im afraid we only have _type.topping_.   <!-- predicted: pizza_ordering.preference: OK. NO _pizza_ordering.preference_? -->
* _type.topping_pizza_ordering.preference_.
    - pizza_ordering.name.pizza_pizza_ordering.preference_pizza_ordering.type.topping: _name.pizza_pizza_ordering.preference_ with _type.topping_d _type.topping_   <!-- predicted: general: Do you want this for pickup or delivery? -->
* Perfect, and can you go _pizza_ordering.preference_? Like half?
    - Absolutely.
* Great, and then also _pizza_ordering.preference_.
    - pizza_ordering.name.pizza.accept_pizza_ordering.name.store.accept_pizza_ordering.preference.accept_pizza_ordering.type.topping.accept: _name.pizza_name.store_ _preference.accept_ _preference.accept_ with _type.topping_ and _type.topping_?   <!-- predicted: general: Would you like something else instead? -->
* Exactly right.
    - pizza_ordering.location.store.accept: Okay great. and just to confirm this is the _location.store_ location?   <!-- predicted: general: Your total is _price_ do you want to pick it up now or later? -->
* Yep! When will it be ready?
    - It will be ready for pick up in about _number_ minutes.
* Thanks!
    - action_listen: action_listen   <!-- predicted: general: Your receipt and order confirmation will arrive shortly via text. -->


## dlg-210e230b-de16-45e8-a1f9-8577732c8ba1
* I would like to have dinner at a indian restaurant for _num.guests_ persons
    - general: Where are you starting from and where are you going to   <!-- predicted: restaurant_reservation.time.reservation: Ok, one moment. And yes, the skies will be clear with a temperature of _number_F _time.reservation_. -->
* I am leaving work and heading to the restaurant with my group of _num.guests_
    - general: ok. what time do you plan to arrive with your group   <!-- predicted: movie_ticket.num.tickets: How many people will be joining you, just _num.tickets_? -->
* make booking for _time.reservation_ at a table for _num.guests_ _type.seating_
    - restaurant_reservation.num.guests_restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating: ok. I can get a table of _num.guests_ _type.seating_ but not at _time.reservation_. Its all booked at _number_pm   <!-- predicted: general: Okay, how many people will be dining? -->
* what are the available time slots besides _time.reservation_
    - restaurant_reservation.time.reservation_restaurant_reservation.type.seating: well, they have a _time.reservation_, and a _time.reservation_ _type.seating_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* make the booking for _time.reservation_ for a party of _num.guests_ _type.seating_ for saturday, january _number_th
    - restaurant_reservation.type.seating: good. would you like to eat _type.seating_ or _type.seating_ and do you want access to the bar   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* _type.seating_ for a table of _num.guests_ with access to bar
    - restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: I will book the table for _num.guests_ _type.seating_ for _time.reservation_ with access to the bar for saturday, january _number_th   <!-- predicted: general: Got it. Would you like me to have any special accommodations ready at the table when you arrive? -->
* thanks. please send the reservation by email
    - general: will do. please arrive _number_ minutes prior to seating- normal protocol   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* thank you. one more thing, kindly check to see that the bar has my favorite guiness beer
    - ok and is this the same for the rest of your party
* yes
    - general: the restaurant do have a wide variety of beers and guiness is included   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Okay...and, done! Your _type.seating_ for _num.guests_ _time.reservation_ at _time.reservation_ at _name.restaurant_ _reservation.accept_. -->
* thank you
    - general: you are all set and enjoy your dinner   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->


## dlg-210f6978-a6da-448d-852f-c57af360623d
* Im looking to reserve a table at _name.restaurant_ for _num.guests_ tomorrow at _time.reservation_. Well need _type.seating_.
    - Im sorry sir but we are fully booked for tomorrow.
* Ok what about the day after tomorrow.
    - restaurant_reservation.time.reservation: That day we have spots available but only _time.reservation_   <!-- predicted: general: They have several desserts available including chocolate lava cake. -->
* Wow really? Then that wont work for us.
    - Yes, we do apologize sir its a busy season.
* No worries, thanks.
    - general: Have a nice day, sir.   <!-- predicted: restaurant_reservation.reservation.accept: Okay, _reservation.accept_, sir. -->
* Im looking to reserve a table at _name.restaurant_ for _num.guests_ tomorrow at _time.reservation_. Well need _type.seating_.
    - general: Excellent, we have have a spot available for that that. Are there any dietary restrictions?   <!-- predicted: restaurant_reservation.type.seating: Excellent, would you prefer a _type.seating_ or _type.seating_? -->
* Yes, my girlfriends friend is gluten free. And I am allergic to peanuts.
    - restaurant_reservation.type.seating: Thank you, sir. Do you have a preference for _type.seating_ or _type.seating_?   <!-- predicted: general: Let me just confirm with the restaurant -->
* _type.seating_.
    - What is the name for the person reserving?
* _name.reservation_
    - restaurant_reservation.name.reservation_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Perfect. Well thank you, _name.reservation_. Your _type.seating_ for _num.guests_ tomorrow at _time.reservation_ is served. Well have _type.seating_ available. We recommend you arrive _number_ minutes before you reservation time.   <!-- predicted: general: Will you require any special accommodations? -->
* Thank you oh and quick question do you have cake?
    - We dont unfortunately.
* Hmm, is it alright is one of us brings a cake? Were celebrating a birthday.
    - general: Absolutely, sir. You can bring a cake.   <!-- predicted: uber_lyft.location.to: Yes, Sir!  Im working on it now.  Oh, want time is you_location.to_rt? -->
* Great to hear. Thanks! Ill see you tomorrow at _time.reservation_.
    - action_listen: action_listen   <!-- predicted: general: No, they do not do that, but there is a splendid African restaurant about _number_ miles from here. They serve great East and West African dishes. -->


## dlg-1b477da2-9cfb-4073-b9f4-e24285a54c3c
* Hi, is this Muffler Man?
    - general: Yes, how may I help you?   <!-- predicted: auto_repair.name.store: OK. I found a highly rated mechanic nearby called _name.store_. -->
* I would like to schedule an appointment _reason.appt_
    - auto_repair.date.appt_auto_repair.date.appt.reject_auto_repair.time.appt_auto_repair.time.appt.reject: can you bring it in _date.appt_ about _time.appt_?   <!-- predicted: general: I can help with that. Where would you like to schedule? -->
* They are _reason.appt_. I would much rather have them done _date.appt_.
    - Are they front or rear brakes? If I have what you need in stock, we may be able to work something out.
* Ok, great! I need the _reason.appt_ done.
    - What is the make and model?
* It is a _year.vehicle_ _name.vehicle_.
    - auto_repair.time.appt_auto_repair.time.appt.reject: Ok, it looks like I have the brakes in stock. Can you come in this _time.appt_?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* No, I am not out of work until _time.appt_
    - auto_repair.date.appt_auto_repair.time.appt: We are only open until _time.appt_, so you would still have to pick it up _date.appt_.   <!-- predicted: general: Is the car otherwise functioning normally? -->
* Would you start work on it _date.appt_, though?
    - general: Yes.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* If I get out of work early, I can be there at _time.appt_ would that be alright?
    - Yes, I think that will work.
* Excellent, I will see you then.
    - general: Before you go, may I have your name and number for the reservation   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: _name.customer_name.store_ _date.appt_time.appt_ure taking in your _year.vehicle_name.vehicle_reason.appt_e phone number I have listed it _number_-_number_ Is all of that information correct? -->
* Yes, _name.customer_ _number_-_number_-_number_
    - auto_repair.name.customer.accept: Alright, _name.customer_, I will see you this afternoon.   <!-- predicted: auto_repair.appointment.accept_auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: _reason.appt_name.customer_, _appointment.accept_. You are scheduled to take your _year.vehicle_ _name.vehicle_ to _name.store_ _date.appt_ at _time.appt_ for a _reason.appt_. -->
* Thank you so much for your help. I really appreciate it.
    - No, problem, maam. Have a good day.
* Thank you, you too. Bye now.
    - Goodbye.


## dlg-210ff36c-0e3a-4983-8c97-f19ea04b2b59
* I need to order an uber ride.
    - Where are you right now?
* I am at _location.from_.
    - And where to do plan on going from there?
* _location.to_.
    - Alright. Well what type of ride do you want?
* Well what are my options?
    - uber_lyft.type.ride: _type.ride_, _type.ride_, and _type.ride_ are available.   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* I think I will go with _type.ride_.
    - uber_lyft.type.ride.reject: Oh. I am sorry. Nevermind. The _type.ride_ is not available.   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* Well what about _type.ride_?
    - Yes, that is available.
* How much is it?
    - uber_lyft.price.estimate.accept: _price.estimate_.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Yikes. How about _type.ride_?
    - uber_lyft.price.estimate.accept: _price.estimate_.   <!-- predicted: general: Let me check the fare estimates. -->
* That is fine. I will take that.
    - Ok. _ride_booking.accept_ and you can check the status of it on your phone.
* Thank you so much. You are a life saver!
    - That is what I am here for!


## dlg-211c6eb9-6892-40a0-989b-452cbf8a4b94
* Hello Alice, its _name.customer_ here.
    - auto_repair.name.customer: Hi _name.customer_, whats up?   <!-- predicted: general: Okay. can I get your phone number,your name and your address? -->
* I am having an issue I need you to take care of.
    - Whats the issue?
* Im having some automobile troubles.
    - auto_repair.name.store.accept: Shall I call your usual auto repair shop, _name.store_?   <!-- predicted: auto_repair.date.appt: OK, Ive explained the situation and the earliest they can see you is _date.appt_ morning. -->
* Yes please.
    - What shall I tell them is the nature of your issue?
* _reason.appt_.
    - auto_repair.reason.appt: Could be a _reason.appt_.   <!-- predicted: general: OK. When would you like to bring it in? -->
* Maybe, Im not sure. Its a _year.vehicle_ _name.vehicle_. Whatd they say for the appointment?
    - auto_repair.time.appt: The man said to bring your car in first thing in the _time.appt_ _number_ days from now because they are very backed up.   <!-- predicted: auto_repair.name.store: Will do!-- later-- _name.store_ just spoke with me, bring the car in right now; but -->
* Is that the best they can do? I dont want to drive like this and I have a lot of work to get done.
    - auto_repair.time.appt: OK I got them to agree to take the vehicle this _time.appt_.   <!-- predicted: general: Absolutely , working on this now. I have a few ideas. -->
* Thank you. Did you schedule it under my proper name and phone number?
    - auto_repair.name.customer.accept: Of course. _name.customer_, (_number_) _number_-_number_   <!-- predicted: general: You as well, good luck. I hope its nothing serious. -->
* Thank you Alice.
    - general: Youre welcome.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* Can you confirm the nature of the problem for me as well as the appointment time and the fee for the initial inspection?
    - auto_repair.date.appt.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: Your appointment _reason.appt_ is scheduled for _time.appt_ _date.appt_. The inspection fee is fifty dollars.   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Thanks Alice, thats all for now.
    - Youre welcome, goodbye sir.


## dlg-211d4ae0-0dd7-4a20-ac5e-d3249baffc9f
* Could you order me an _name.drink_ from Starbucks.
    - Sure, what size do you want?
* Whatever the largest option is.
    - coffee_ordering.size.drink: Ok, the largest is a _size.drink_. What kind of milk do you want?   <!-- predicted: coffee_ordering.preference: They have both _coffee_ordering.preference_ -->
* _type.milk_.
    - Ok, and do you want to add any other flavors to that?
* Yes, add _coffee_ordering.preference_ if they have it.
    - coffee_ordering.preference: Alright, and do you want anything added in like _coffee_ordering.preference_, _coffee_ordering.preference_, or _coffee_ordering.preference_?   <!-- predicted: general: Well thats a mouthful. -->
* Id like _preference.accept_, and thats all.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.reject: Alright, so thats a _size.drink_ _name.drink_ with _preference.accept_. It looks like they are out of _type.milk_ today. What do you want instead?   <!-- predicted: general: I hear you.. is there something else youd like? -->
* Ill do _type.milk_ in that case.
    - Great, Ill add it in. Is there anything else?
* Actually, could I add _preference.accept_ to that? That will be everything.
    - Sure, Ill add it in. Whats your current location?
* Im driving south into _location.store_ right now.
    - coffee_ordering.location.store: It looks like youll pass near a _location.store_. location. Is that ok?   <!-- predicted: general: Ok, let me confirm your order and make sure they can have it ready by _number_pm. -->
* Sure, _location.store_ is fine.
    - coffee_ordering.location.store.accept: Great, so the location is _location.store_ Your order will be ready for pickup there and the receipt will be sent to your phone.   <!-- predicted: coffee_ordering.coffee_order.accept_coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_restaurant_reservation.num.guests.accept: _coffee_order.accept_num.drink_num.guests_ _preference.accept_size.drink_name.drink_location.store_ -->
* Thanks so much for your help.
    - No problem, I hope you enjoy the coffee.


## dlg-211ed913-fe01-44c4-839d-315fa39d9290
* _name.movie_name.theater_ at a theater in _, can_location.theater_look up times please
    - general: Okay, how many tickets do you need?   <!-- predicted: movie_ticket.price.ticket: Adult tickets are _price.ticket_ Child tickets are _price.ticket_. How many tickets would you like? -->
* _num.tickets_ please
    - What time do you want to go?
* Im hoping _time.start_
    - general: Okay, Im looking that up now   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Thank you
    - movie_ticket.location.theater_movie_ticket.time.start_movie_ticket.type.screening: _location.theater_ only has a _time.start_ or _time.start_, both in _type.screening_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* I didnt want _type.screening_, is there anything else close?
    - movie_ticket.location.theater: Ill check _location.theater_   <!-- predicted: general: _number_ noon option is available with a margin of _number_ mins -->
* Thank you
    - movie_ticket.location.theater.accept_movie_ticket.name.theater_movie_ticket.time.start_movie_ticket.time.start.reject_movie_ticket.type.screening_movie_ticket.type.screening.accept: _location.theater_name.theater_ does have a _time.start_ showing that is _type.screening_   <!-- predicted: movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: I just purchased _num.tickets_name.movie_name.theater_ f_time.start_ -->
* Okay, I think that should work
    - movie_ticket.price.ticket: Okay great, it should be about _price.ticket_   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Okay thank you
    - Is there anything else you need?
* Actually, my wife may not want to see that, is _name.movie_ playing there?
    - Yes, it is
* Can you see if its around the same time?
    - movie_ticket.time.start: Theres one at _time.start_   <!-- predicted: general: Unfortunately yes. -->
* Let me see which one shed like to see
    - Okay
* She would like to see _name.movie_, can you get those tickets?
    - general: Yes I can   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Thank you
    - movie_ticket.price.ticket.accept: That will also be _price.ticket_   <!-- predicted: general: Do you have a preferred theater? -->
* That will work, thank you
    - Is there anything else?
* No, thank you that was great.
    - movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: Okay, your _num.tickets_ tickets for _name.movie_ _time.start_ at the _name.theater_ will be available at the booth. Have a good day   <!-- predicted: general: Okay, enjoy your movie. -->


## dlg-2122b064-f6b4-4b8e-9a80-1653e879b596
* Hey, I want to get tickets for _name.movie_
    - OK, where should I look?
* _location.theater_
    - movie_ticket.name.movie_movie_ticket.name.theater: _name.movie_ is playing at the _name.theater_.   <!-- predicted: general: Okay, I show several theaters close by. Do you have a preference on which one you would like to go to? -->
* Great! Is there anything available tonight at _time.start_?
    - movie_ticket.name.movie_movie_ticket.time.start_movie_ticket.time.start.reject: Sorry, but _name.movie_ is not starting at _time.start_ tonight. The closest available times are _time.start_ or _time.start_   <!-- predicted: movie_ticket.time.start: Yes, they have a _time.start_ showing -->
* No, that wont work. What about tomorrow at _time.start_?
    - movie_ticket.num.tickets.reject_movie_ticket.time.start_movie_ticket.time.start.reject: _time.start_num.tickets_ Saturday. The _time.start_time.start_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Hmm. Are there any other theaters nearby that show the film at _time.start_
    - movie_ticket.location.theater_movie_ticket.name.theater_movie_ticket.time.start: Checking... _name.theater_ in _location.theater_ has a showing at _time.start_.   <!-- predicted: movie_ticket.time.start_movie_ticket.type.screening: They have a _time.start_ showing in _type.screening_ and a _time.start_ showing in _type.screening_ -->
* How far from _location.theater_ is that?
    - movie_ticket.location.theater_movie_ticket.name.theater: _name.theater_ in _location.theater_ are _number_ miles west of _location.theater_.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* OK. Can you book that?
    - general: How many tickets do you need?   <!-- predicted: movie_ticket.name.movie_movie_ticket.num.tickets_movie_ticket.time.start_movie_ticket.time.start.reject: The late show wasnt until _time.start_ so that might have been a little too late. But, they do have _num.tickets_ tickets for the _time.start_ showing of _name.movie_ tonight, March _number_th. -->
* _num.tickets_.
    - movie_ticket.name.movie_movie_ticket.num.tickets_movie_ticket.price.ticket: _num.tickets_ for _name.movie_ will be a total of _price.ticket_   <!-- predicted: general: Okay. It looks like you can choose the general area you can sit. Were you looking for a seat near the front, middle, or back? -->
* OK, book it!
    - movie_ticket.name.movie_movie_ticket.num.tickets: _num.tickets_ for _name.movie_ have been ordered. Shall I bill this to your account?   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* Yes, please.
    - movie_ticket.location.theater_movie_ticket.name.movie_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.num.tickets.accept_movie_ticket.price.ticket.accept_movie_ticket.ticket_booking.accept_movie_ticket.time.start.accept: _num.tickets_ for a total of _price.ticket_ _ticket_booking.accept_ for _name.movie_ tonight at _time.start_name.theater_name.movie_ in _location.theater_. The tickets and a receipt have been sent to you in a text message.   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_ as a text message. -->
* Good. Can you also send directions?
    - movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept: _name.theater_name.movie_ in _location.theater_ have been sent to your mobile phone. Can I help you with anything else?   <!-- predicted: general: Yes. You press a button  they bring you food. Its full service! -->
* No, thanks. Goodbye!
    - general: Goodbye.   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->


## dlg-21276502-3a4f-4cb1-a244-b668ed546d9f
* i would like to make a reservation for dinner
    - ok I can help you with that. What restaurant and location are you selecting
* _name.restaurant_ on _location.restaurant_
    - general: alright how many will be joining you for dinner   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* _num.guests_ people total including me
    - general: okay and what date and time will you be attending   <!-- predicted: restaurant_reservation.time.reservation: Okay great we have the option for a bottle of wine or roses at longhorns and availability at _time.reservation_ and a _price_ charge for wine or roses. -->
* _time.reservation_
    - okay one moment while I compile your request
* no problem take your time
    - general: alright one moment... I have all of your information set would you like to process this reservation?   <!-- predicted: restaurant_reservation.time.reservation: It looks like they wont have a table available until _time.reservation_ tomorrow -->
* Yes please
    - alright your reservation has been set and How would you like to receive your confirmation number by email or text
* email is fine
    - okay it seems we do not have an email address on file for you would you like to add one now?
* Yes its happygolucky_number_
    - general: okay allow me one moment to update your info   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* okay
    - okay your info has successfully updated is there anything else i can help with
* yes is there a way to add a special request note
    - general: yes what is the request   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: _name.customer_name.store_ _date.appt_time.appt_ure taking in your _year.vehicle_name.vehicle_reason.appt_e phone number I have listed it _number_-_number_ Is all of that information correct? -->
* I would like a _type.seating_
    - okay i am adding that note now
* okay
    - general: alright note was added is there anything else i can assist with   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: _name.restaurant_ked for April _number_num.guests_th, _num.guests_ at _time.reservation_ for _name.restaurant_e. -->
* no that was it oh and did you email the confirmation
    - yes the confirmation email was sent to the email address provided
* ok thank you so much
    - it was my pleasure have a great day and enjoy
* thanks I will
    - general: thank you for using chat bot   <!-- predicted: action_listen: action_listen -->


## dlg-212db3a5-814e-4237-b6cf-f5182de4a3ba
* Can you make reservations for _name.restaurant_ for Monday Night. Steve Burns and Harold Smith are visiting and would like to schedule a dinner. They will be bringing _number_ of their top Sales Managers. So we are looking for a place that can accommodate a large number of people
    - general: Sure, how many people will this reservation be for?   <!-- predicted: uber_lyft.type.ride: How about _type.ride_? Its going to cost twice as much. But plenty of rooms to fit everything. -->
* _num.guests_
    - general: Great, what time would you like this reservation for?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* Make it _time.reservation_ , we can meet in the bar area around _time.reservation_
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject_restaurant_reservation.time.reservation: I just called _name.restaurant_ and they can accommodate the large party for Monday but there are no reservations at _time.reservation_, but I do need to tell you they do not have a bar area. Do you still want me to make the reservation?   <!-- predicted: general: okay let me check on that. -->
* Well, if they do not have a bar, and _time.reservation_ is not an option, lets see if they can accommodate a _time.reservation_ reservation
    - I spoke tot the manager and he stated that he can accommodate _time.reservation_ but you would have to have a minimum number of _number_ people because the only space that is available due to short notice is a private room.
* Its ok I think we will pass on _name.restaurant_. Can you look up any other steakhouses in the area with good ratings.
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject: Sure I found _name.restaurant_, I happen to know that they have a large bar area. Would you like me to call them and ask if they can accommodate our large party?   <!-- predicted: restaurant_reservation.name.reservation_restaurant_reservation.name.reservation.accept_restaurant_reservation.time.reservation.accept: Alright, well see you Friday night at _time.reservation_ _name.reservation_. -->
* No I had a bad experience with that place, can you look for another place?
    - restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept: _name.restaurant_name.reservation_, would you like me to call them and inquire?   <!-- predicted: general: Oh, Im sorry. Can I help you find another restaurant? -->
* Yes that would be great, I heard great things about that place, its a little bit further than i wanted to go, but why not.
    - I was able to confirm that they can accommodate our large party. They did mention that we need to put a deposit down in order to hold the reservation.
* Oh that is fine, how much of a deposit are they asking for?
    - general: They require a _price_ deposit to secure your table.   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests_restaurant_reservation.time.reservation_restaurant_reservation.type.seating.accept: _time.reservation_num.guests_ tonight at _time.reservation_name.restaurant_type.seating_ -->
* Yes go ahead and book the reservation. Can you also ask them to reserve some _type.seating_? Also can you let them know that all drinks will be charged to the same dinner bill.
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.accept: Sure thing! I just called back and they told me that they have a nice quiet area by the fire place in the bar for _time.reservation_ and dinner reservations at _time.reservation_   <!-- predicted: general: k sir, now you can here me. -->
* That is great, thank you so much for doing this.
    - restaurant_reservation.location.restaurant.accept: You are welcome.  The address is _location.restaurant_t   <!-- predicted: general: You are welcome let me know if you need anymore help. -->


## dlg-21315f48-61c7-4615-b2f8-66e04353d61b
* Hey Donna Im dragging can you order a coffee for me?
    - Sure thing Turker, where do you want it from?
* Starbucks, the usual.
    - general: Which Starbucks do you want it from?   <!-- predicted: coffee_ordering.name.drink_coffee_ordering.name.drink.accept: Do you want their _name.drink_? -->
* The _location.store_
    - general: Sounds good! What would you like?   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* _size.drink_name.drink_ and one pump of _coffee_ordering.preference_
    - What kind of milk would you like?
* The _type.milk_ is fine.
    - coffee_ordering.preference.reject: Alright, Im mobile ordering it for you. Looks like the _preference.reject_ is not available at this location. Is there another youd like?   <!-- predicted: general: Perfect, whats the best pick up location? -->
* Darn. Can I get the _coffee_ordering.preference_?
    - That is available! _coffee_ordering.preference_. Any other additions?
* No I think that is it.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Alright so I have a _size.drink_ _name.drink_ with _type.milk_, an _preference.accept_?   <!-- predicted: general: Ok, I will call them now and call you back with confirmation of the order. -->
* Yes that is correct!
    - general: Perfect. Do you want to use the reward you have on the account?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* Might as well!
    - coffee_ordering.location.store.accept: _location.store_ be ready in about _number_ minutes at _location.store_   <!-- predicted: general: YOU WANT PAY NOW? -->
* Perfect, thanks Donna.
    - No problem Turker. You should see the info pop up on your Starbucks app if you havent already.
* Got it, thank you
    - Have a nice day!


## dlg-213efbe4-1c5b-4d20-97ba-0798ba469135
* Hi, I saw where you have a _name.pizza_ for _number_.
    - Yes, we do but that is for online orders only.
* Ok, so are there any other specials that are similar?
    - pizza_ordering.name.pizza_pizza_ordering.name.pizza.accept: You can get two _name.pizza_ for _number_ dollars each.   <!-- predicted: restaurant_reservation.name.restaurant: No, _name.restaurant_ is known for traditional Chinese -->
* No thanks, just let me get a _size.pizza_ _name.pizza_.
    - general: Ok what type of crust?   <!-- predicted: pizza_ordering.name.pizza: Is the _name.pizza_ something you should order for the office? -->
* Make that a _type.crust_
    - Would you like anything else, maybe something to drink?
* No, but can I exchange the _type.topping_ for _type.topping_ on that?
    - general: Yes, you can! Will there be anything else   <!-- predicted: pizza_ordering.type.topping.reject: they just told me _type.topping_ is not available -->
* Im sorry can you change that to a _size.pizza_ pizza?
    - pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Yes, so you want a _size.pizza_ instead of _size.pizza_?   <!-- predicted: general: Sure, I will grab that too. -->
* That is correct!
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept: Ok so let me confirm, you want a _size.pizza_ _name.pizza_ on _type.crust_?   <!-- predicted: general: ok, your total will be _price_ is there anything else you would like? -->
* Yes, and dont forget exchange the _type.topping_name.pizza_type.topping_!
    - Yes, sorry I do have that!
* Thanks, that will be all.
    - Would you like to add a dessert?
* I would like but dont need! No thank you!
    - Ok if that completes your order, that will be _number_ we will send receipt by text and your order will be ready in _number_ minutes!
* Thank you!
    - Thank you maam!


## dlg-213efdf2-9bf9-4b5c-9f20-b2dbbf2cb9ca
* _type.ride_uber_lyft.uber_lyft_?
    - Certainly, what kind of car?
* Its just me, the _type.ride_ ride will work
    - general: Ok, I can get you an estimate. What is your route?   <!-- predicted: uber_lyft.time.pickup.accept: So schedule the Uber for _time.pickup_? -->
* From _location.from_, you know my address, to _location.to_
    - uber_lyft.price.estimate_uber_lyft.type.ride: Ok, _type.ride_ or _type.ride_? the price difference is about _price.estimate_   <!-- predicted: uber_lyft.location.to.accept: Ah, yes. _location.to_, correct? -->
* Just the _type.ride_. How soon can it be here?
    - general: Im not sure, let me finish entering the details and Im sure I can let you know.   <!-- predicted: uber_lyft.price.estimate_uber_lyft.type.ride: Looks like _type.ride_ is _price.estimate_ right now. -->
* Certainly
    - uber_lyft.price.estimate.accept_uber_lyft.type.ride.accept: Ok, So the total is between _price.estimate_ for the _type.ride_ fair   <!-- predicted: general: I know, right? -->
* That works, how soon will it be here?
    - uber_lyft.time.pickup.accept: It should arrive in about _time.pickup_   <!-- predicted: uber_lyft.ride_booking.accept_uber_lyft.time.pickup.accept: Lets see, I just sent the payment through and...Itll be a black _number_ Toyota Camry. _ride_booking.accept_ _time.pickup_. -->
* Ok, great
    - Oh, hold on, theres a problem with that first car.
* Um, whats the problem.
    - Its no longer available but I was able to get a replacement for you, its on its way now.
* Oh, excellent, youre the best.
    - general: Of course, I am sending the confirmation information to your mobile now, they will charge your card on file.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Perfect, thanks, gotta go, bye!
    - Bye!


## dlg-1b47bb2b-61b1-46b2-879a-719e939cf2f5
* Can I make a _restaurant_reservation.restaurant_reservation_ please?
    - Yes, where would you like to make one?
* How about the _name.restaurant_ in _location.restaurant_?
    - Ok, when would you like to make this reservation?
* Im thinking this Thursday night at _time.reservation_. Anything open?
    - restaurant_reservation.restaurant_reservation_restaurant_reservation.time.reservation: Im sorry I dont see anything open during that time. There is an available _restaurant_reservation.restaurant_reservation_ for _time.reservation_.   <!-- predicted: general: Let me check, one second. Yes, they have many times avilabile. What is your prefered time? -->
* Anything _time.reservation_? What about _time.reservation_ or _time.reservation_?
    - restaurant_reservation.restaurant_reservation_restaurant_reservation.time.reservation: Im sorry, the next available _restaurant_reservation.restaurant_reservation_ is at _time.reservation_.   <!-- predicted: restaurant_reservation.time.reservation.reject: _time.reservation_ is fully booked also. -->
* Ok what about the _name.restaurant_ _location.restaurant_? Do they have a _type.seating_ for _num.guests_ at _time.reservation_?
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests_restaurant_reservation.time.reservation_restaurant_reservation.type.seating: I am seeing a _type.seating_ for _num.guests_ at _name.restaurant_ at _time.reservation_. Is that ok?   <!-- predicted: restaurant_reservation.time.reservation: They do, they have one at _time.reservation_ and one at _time.reservation_. -->
* Yes, we can take the _time.reservation_ time. Can we get _type.seating_ seats too please?
    - restaurant_reservation.type.seating.reject: Sorry, there are no _type.seating_ seats available.   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* What about _type.seating_?
    - restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: _type.seating_ are all reserved as well.   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: I apologize, but they dont have any _type.seating_ available on that date at _time.reservation_. -->
* Its ok, well just take _type.seating_ for _num.guests_.
    - restaurant_reservation.location.restaurant.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: Booking your table for _num.guests_ at the _name.restaurant_ _location.restaurant_ for this Thursday at _time.reservation_. Everything correct?   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* Yes, all good.
    - restaurant_reservation.reservation.accept: _reservation.accept_   <!-- predicted: general: Okay your reservation has been made. -->
* Great! Thank you so much!
    - Youre welcome!


## dlg-2140aeaf-a743-46e6-a1b8-bfb7bcdd3133
* Hello, Id like to order a drink from Starbucks for pick up.
    - Hello. Which Starbucks location?
* The location closest to me.
    - coffee_ordering.location.store: The closest Starbucks location is _location.store_. What would you like to order?   <!-- predicted: general: From which store do you want me to get your coffee? -->
* _num.drink_name.drink_.
    - general: What size?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* _size.drink_.
    - general: What type of milk?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* _type.milk_ milk.
    - general: Do you have any other requests for your order?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* Only _coffee_ordering.preference_ instead of two.
    - coffee_ordering.type.milk.reject: Sorry, _type.milk_ milk is not available. Please choose another type of milk.   <!-- predicted: general: Okay. Anything else I should know? -->
* Okay, _type.milk_ milk.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: You would like one _size.drink_ _name.drink_ with _type.milk_ milk and _preference.accept_. Is that correct?   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* Yes.
    - coffee_ordering.location.store.accept: Your order for pick up at Starbucks _location.store_ is ready to be submitted. Would you like to proceed?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* Yes please.
    - general: Your order has been submitted and will be ready for pick up shortly. Your receipt will be sent to your mobile device.   <!-- predicted: coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Thats a _size.drink_ _name.drink_ with _preference.accept_ ready in a half an hour at _location.store_. Total is going to be _price_ -->
* Thank you.
    - Youre welcome.


## dlg-21435d68-40ae-4093-a28e-28fdca7ed73e
* I would like to request a Uber.
    - Okay where would you like to be dropped off and picked up?
* The dropoff will be at _location.to_.
    - Okay and the pickup?
* The pickup will be in _location.from_.
    - general: Okay what type of car do you need.   <!-- predicted: uber_lyft.location.to: Updating drop off point to _location.to_. -->
* I need a large car so I will require an _type.ride_
    - Okay when do you need this car by?
* As soon as possible.
    - uber_lyft.type.ride.reject: I looked up a car for you and there are no _type.ride_ available in the area.   <!-- predicted: general: Do you need that Uber right now? -->
* Okay a regular _type.ride_ will do just fine.
    - uber_lyft.price.estimate.accept: Okay the cost of the ride will be around _price.estimate_.   <!-- predicted: general: Your drivers name is Derek and his plate number is . -->
* Okay that would be fine.
    - Would you like me to order the ride.
* Yes please.
    - uber_lyft.ride_booking.accept: _ride_booking.accept_ and payed for.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Thank you very much.
    - uber_lyft.time.pickup.accept: It will be there in around _time.pickup_ and you can look on your phone for updates.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Okay sounds good thank you.
    - You are welcome.


## dlg-2144f39d-5ff5-4041-bf85-477b2c5dae08
* Hi can you please order m tickets to see the movie _name.movie_.
    - Sure, what city would you live me to get your tickets in?
* _location.theater_
    - Ok, do you have a favorite location or do do you want me to just pick?
* Sorry no, I want tickets for _name.movie_ at _name.theater_.
    - general: Okay, how many do you need?   <!-- predicted: movie_ticket.name.theater: Okay. I see one theater, _name.theater_. -->
* I need _num.tickets_ its a date niht for _num.tickets_.
    - Thats nice. Do you want me to order the tickets for a particular time or do you want the next showing?
* No I want the last showing because we have a dinner and I dont want to rush.
    - general: Do you know the last showing tome or do you want me too look it up?   <!-- predicted: movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: I just purchased _num.tickets_name.movie_name.theater_ f_time.start_ -->
* Girl I am just makin g ypou work to day, Seriously I am so rushed the last showing is at _time.start_
    - No thats ok thats perfect.
* Thank you can you please ordr mr tickets in _type.screening_ as well.
    - I certainly can do that for you. Do you know the price of the tickets?
* They are _price.ticket_ ticket totaling _price.ticket_
    - general: Ok thanks. Ho wwould you like me to pay should I use your credit card ?   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: _name.theater_num.tickets_name.theater_time.start_name.movie_location.theater_ -->
* No, my info is on file with the service so we will be good .
    - cool I will get it done right now a nd I will send the info and tickets directly to your phone.
* Thasnk you Ssally so much I will text back to et you know if I receicev it if I dont get it.
    - general: Ii am doing it as soon as I hang uo so if I dont hear back with in an half hour I will call you to double check that you got it   <!-- predicted: auto_repair.time.appt: They have a _time.appt_ slot open. Is that too late for you? -->
* Thsank you and have a god day.
    - You to and enjoy your movie.


## dlg-214d67a6-a34f-4d36-b91e-a74f24e5d55b
* I want to order a drink from starbucks
    - sure thing, which location would you want
* the one _location.store_
    - are you picking it up yourself?
* Yes, I am
    - and are we using your regular account with them
* yes, use that one
    - What kind of drink would you like?
* I want a _name.drink_
    - general: they said they dont have that until thanksgiving and christmas   <!-- predicted: coffee_ordering.type.milk: Okay. Do you want _type.milk_? -->
* what a shame, I really like that, give me a moment
    - general: for sure   <!-- predicted: coffee_ordering.type.milk.reject: They are also running low on _type.milk_ -->
* I want another kind of coffee
    - what would you want to order
* lets get a _name.drink_
    - what size would you want
* _size.drink_ one they hae
    - coffee_ordering.coffee_order.accept: _coffee_order.accept_, the drink should be ready for pick up soon, the receipt will be sent to your phone   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* thank you
    - you are welcome


## dlg-215525e2-4187-43a2-aea5-95515d34594d
* Hello Assistant, I would like you to make reservations for _num.guests_ at _name.restaurant_ in _location.restaurant_ please.
    - Hello sir, I would love to help you with that request. When did you want the reservations and for how many?
* _num.guests_ are going to be in _location.restaurant_ this weekend on business. I need a table for _num.guests_ at _time.reservation_.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.time.reservation: Ok, I have _name.restaurant_ hostess on the other line, she says that they are totally booked _time.reservation_ but that they could get you guys in on _time.reservation_.. Could that work for you?   <!-- predicted: general: Great, let me check on that for you? -->
* No, Sunday will not work. We will be heading back home. Do they have anything for _time.reservation_?
    - Hold a moment and I will check with them.
* Ok, Thank you so much Assistant.
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: It is my pleasure sir. They do have an opening on _time.reservation_, but not at _time.reservation_ like you suggested earlier. Its at _time.reservation_. How does that sound?   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_. Enjoy your feast. -->
* That sounds perfect!
    - general: Ok, was there anything else I can help you with?   <!-- predicted: restaurant_reservation.reservation.accept: Excellent, _reservation.accept_. Would you like a confirmation text sent to your mobile phone? -->
* Yes, actually we wondered if they had a _type.seating_ with heaters, since its cold out
    - general: Let me check with them.   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* Oh, and if they do have a _type.seating_ with heaters, will we be able to smoke?
    - restaurant_reservation.type.seating.accept: Ok, I checked with them, they do have a _type.seating_, but they do not have heaters.   <!-- predicted: general: No, they do not do that, but there is a splendid African restaurant about _number_ miles from here. They serve great East and West African dishes. -->
* Bummer. What about the smoking? Can we smoke there?
    - I will ask.
* Thank you very much
    - restaurant_reservation.type.seating: Im sorry sir, but as most other restaurants they have gone to _type.seating_.   <!-- predicted: general: Youre welcome enjoy your dinner. -->
* Well, it doesnt hurt to ask, right?
    - restaurant_reservation.num.guests.accept_restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation.accept: No, it does not. _num.guests_time.reservation_. Is there anything else I can help you with?   <!-- predicted: restaurant_reservation.reservation.accept: Great, done! _reservation.accept_ and ready! -->
* No Assistant. You have been very helpful and I really do appreciate you. Thank you.
    - You are welcome sir. I am here for you anytime you need anything.
* That is comforting to know. I will talk to you soon. Goodbye.
    - Goodbye sir.


## dlg-215b406a-ad92-440b-aa4e-17c08a8bcd7a
* Hi, I want a coffee today.
    - Alright, what would you like?
* I want something hot, what do you have?
    - coffee_ordering.name.drink: We have _name.drink_, and _name.drink_.   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* What would you recommend?
    - coffee_ordering.name.drink: Personally, I like the _name.drink_.   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* Do you have a _name.drink_?
    - general: We do have mild, would you like mild?   <!-- predicted: coffee_ordering.type.milk: The cold foam can be made with _type.milk_ or _type.milk_ only but not _type.milk_ -->
* I think so.
    - Absolutely. Anything else for you this evening?
* Im not sure. What are your specials right now?
    - Well, we have a few based on what you already ordered.
* Awesome, what are they?
    - coffee_ordering.name.drink.accept_coffee_ordering.size.drink.accept: I have a deal for buy one get one free _size.drink_ _name.drink_.   <!-- predicted: general: He is coming in a white honda civic. -->
* That sounds really good!
    - Would you like that?
* Yes, please.
    - Alright, can do.
* Thank you so much.
    - action_listen: action_listen   <!-- predicted: general: Great. Have a good night. -->


## dlg-2160790c-1cb6-4c99-90d4-e56b06b9b6a0
* Hello Jackson, whats up? I need you to book an appointment for the _time.appt_, Im in a tunnel and I have _reason.appt_
    - Hello, all right, how are you? sure, do not worry, Ill do it right now but I need you to give _number_ pieces of information
* Which?
    - general: The first your phone number   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Ok; _number_
    - The second, general information of the Auto
* _name.vehicle_ Year, _year.vehicle_
    - general: And third, your name   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _name.customer_
    - general: Ok I gave them the information, come as fast as you can get, they will be waiting for you   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Ok, where do I have to go?
    - auto_repair.name.store.accept: _name.store_   <!-- predicted: general: Yes, you can. Do you need shuttle service to your office? -->
* Ok, Ill arrive as soon as possible
    - general: Ok here I see you, have a good day   <!-- predicted: uber_lyft.time.pickup_uber_lyft.time.pickup.accept: Here is your reminder that your scheduled uber will _time.pickup_. -->
* Equally
    - general: By the way, one last thing, yesterday your breakfast toast burned   <!-- predicted: uber_lyft.ride_booking.accept: No problem dear customer. _ride_booking.accept_. The driver should be there shortly. -->
* Hahahaha, Im not good at cooking
    - Hahahaha, I see
* Well bye
    - Bye


## dlg-2175efd9-4f21-4ab1-879b-afbcbaec254f
* Sue, Im _num.guests_ for his birthday. Can you book me a reservation?
    - Sure. Do you know where?
* Lets try _name.restaurant_.
    - Okay, what day and time?
* Tomorrow at _time.reservation_.
    - Okay let me check.
* Thanks.
    - restaurant_reservation.time.reservation: Just got off the phone with them. They do not have availability at that time, but they have one for _time.reservation_.   <!-- predicted: general: reservation made -->
* No, thats too early.
    - restaurant_reservation.name.restaurant: How about _name.restaurant_?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Im sorry, we cant accommodate a group of your size at _time.reservation_. Would you be available to join us at _time.reservation_ instead? -->
* Okay, try them.
    - restaurant_reservation.name.restaurant.reject: Sorry, _name.restaurant_ is closed for a private party.   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_ -->
* _name.restaurant_name.reservation_
    - Okay let me call.
* Let me know.
    - restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Okay, they have a _type.seating_ tomorrow at _time.reservation_. _reservation.accept_   <!-- predicted: movie_ticket.name.theater_movie_ticket.time.start_movie_ticket.time.start.reject: Ok so Im on _name.theater_s website, and they dont have one for tonight at _time.start_. I also searched around just to make sure. But it looks like the only options aregonna be for _time.start_ or _time.start_ -->
* Great, thanks.
    - Enjoy your dinner
* Thank you!
    - Let me know how it goes


## dlg-2176b69a-28de-4155-9aa6-ce0ec705af92
* I need to bring my car in and have someone take a look at it. _reason.appt_.
    - Ok sure. Bring it in and we will take a look at it. What kind of car is it?
* It is a _year.vehicle_ _name.vehicle_
    - auto_repair.date.appt: Ok, we are familiar with that model.  You can bring it in _date.appt_y and we should be able to get to it.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Ok well I need this fixed _time.appt_.  Can I bring it in now?
    - auto_repair.time.appt.accept: _time.appt_. We should be able to run diagnostics and get you an answer quickly.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: Well, it looks like theyre soonest appointment i_date.appt_ morning a_time.appt_ -->
* Do you have any idea what might be wrong or how much it will cost just based on what I have told you over the phone.
    - No, it would be hard to tell you unless we have a chance to look at it.
* Ok, well I just have had bad experiences in the past with mechanics trying to rip me off.
    - Dont worry we have a diagnostic tool that will give you real time results from your computer and we can let you review the diagnostics.
* Ok, well that sounds fair. Do you charge for the diagnostics.
    - No, we do not charge for diagnostics. If you decide to fix the problem we will let you know how much and you can pay when the service is complete.
* Ok, do you take card
    - general: Yes we take all major cards.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Do you offer rental cars in case it needs to stay overnight?
    - Yes we do have a loaner we give out if we need to keep the car overnight.
* Great. I will go ahead and bring it in.
    - general: Ok I am sure we can get you fixed up.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Ok well I will see you soon.
    - general: Ok, so can I get your name and number so I can be waiting for you?   <!-- predicted: auto_repair.date.appt_auto_repair.date.appt.accept_auto_repair.time.appt: you can come in _date.appt_, at _time.appt_ -->
* Sure it is _name.customer_ and my phone number is _number_-_number_
    - auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.reason.appt.accept: Ok thank you _name.customer_. _date.appt_, correct?   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt.accept: Okay, I have you scheduled for _date.appt_ at _time.appt_ -->
* That is correct.
    - general: Ok we will see you soon   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.vehicle.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Okay so I have told them that _name.customer_ will be bringing her _year.vehicle_ _name.vehicle_ in at _time.appt_ _date.appt_. Phone number _number_-_number_ Anything else? -->
* Ok, Bye.
    - action_listen: action_listen   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->


## dlg-217ce39a-2f04-42b1-b657-ec45b0f779b9
* I need a ride. Call Lyft.
    - Where are you going and where do you want to be picked up?
* _location.from_ _location.to_
    - Which terminal?
* Alaska.
    - general: Domestic or International?   <!-- predicted: uber_lyft.duration.estimate_uber_lyft.price.estimate.accept_uber_lyft.time.pickup_uber_lyft.type.ride: Ok. I am looking it up now. Ok. There is an suv driver or _type.ride_ available for $_price.estimate_duration.estimate_time.pickup_ -->
* Domestic.
    - uber_lyft.location.from_uber_lyft.location.from.accept_uber_lyft.location.to_uber_lyft.location.to.accept: Requesting a ride from _location.from_ to _location.to_   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* How much does it cost?
    - uber_lyft.price.estimate_uber_lyft.price.estimate.reject: You have two options Shared Ride for _price.estimate_, or Lyft for _price.estimate_.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* How soon can I get there?
    - uber_lyft.duration.estimate_uber_lyft.time.dropoff_uber_lyft.time.dropoff.accept: Shared ride arrival _duration.estimate_. _time.dropoff_.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Hmm. How many people for the shared option?
    - uber_lyft.num.people_uber_lyft.type.ride: _type.ride_ option vehicle has room for _num.people_   <!-- predicted: uber_lyft.time.pickup: About _time.pickup_ -->
* Okay. Ill take the _type.ride_
    - uber_lyft.location.from_uber_lyft.location.to: Booking Shared Option from _location.from_ to _location.to_ --   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Wait! Maybe I better take the Lyft instead.
    - general: Are you sure?   <!-- predicted: uber_lyft.location.from.accept_uber_lyft.location.to.accept_uber_lyft.time.pickup.accept: ok then your ride is on the way to pick you up at the _location.from_ to take you to the _location.to_ and should be arriving in _time.pickup_ you can always check the status on your phone -->
* No. Um...lets go with the Shared Ride - sorry!
    - uber_lyft.location.from.accept_uber_lyft.location.to.accept_uber_lyft.price.estimate.accept_uber_lyft.type.ride.accept: No problem. _type.ride_location.to_location.from_ to _location.to_price.estimate_   <!-- predicted: uber_lyft.location.from_uber_lyft.location.from.accept_uber_lyft.location.to_uber_lyft.location.to.accept: ok, so placing a lyft for you from _location.from_ to the _location.to_ -->
* Great! Whens it coming?
    - general: Your ride is on the way. You can check the status on your phone.   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_. You can check its status on your phone. -->
* Thanks!
    - action_listen: action_listen   <!-- predicted: general: Youre welcome. Anything else I can assist you with? -->


## dlg-1b522e11-0983-4701-8aac-017078461fda
* Hi there. Id like to order some _pizza_ordering.pizza_ordering_ from _name.store_..
    - Okay. Sure. Which location?
* _location.store_
    - Super. What kind of pizza would you like?
* I would like a _type.topping_ and _type.topping_.
    - general: Sounds good. I will place your order.   <!-- predicted: pizza_ordering.preference_pizza_ordering.preference.reject: _pizza_ordering.preference_preference.reject_? -->
* Thank you.
    - pizza_ordering.type.topping.reject: Im sorry. They are out of _type.topping_.   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->
* Oh darn.
    - Can I substitute it for something else?
* How about _type.topping_ and _type.topping_.
    - Let me check.
* Great.
    - general: Yes, that is available. What size would you like?   <!-- predicted: pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: So that total is _price_ and can you confirm that you want _size.pizza_name.pizza_type.topping_type.topping_ by delivery? -->
* A _size.pizza_, please.
    - Okay. Placing the order now.
* Wonderful.
    - pizza_ordering.location.store.accept_pizza_ordering.name.pizza.accept_pizza_ordering.name.store.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Ive ordered a _size.pizza_name.pizza_type.topping_type.topping_ from _name.store_. It will be ready for pickup in _number_ minutes _location.store_.   <!-- predicted: general: Ok sent! Is there anything else for today? -->
* Thank you so much!
    - pizza_ordering.pizza_order.accept: No problem! _pizza_order.accept_   <!-- predicted: general: Was there anything else I can do for you? -->
* Perfect!
    - action_listen: action_listen   <!-- predicted: general: I am sending you the receipt via text message right now -->


## dlg-1a8b5529-488e-4a4b-b553-45129ee9b4bd
* Hey, can you get me a Uber?
    - I can get you a Uber, where are you at and where do you want to go?
* I am at the _location.from_ and want to head _location.to_.
    - Is there anyone else with you?
* No _num.people_.
    - Ok and is there particular kind of Uber you want
* What do they have?
    - uber_lyft.price.estimate_uber_lyft.type.ride: The popular choices are _type.ride_, _type.ride_ and _type.ride_. There are other choices, but those at gonna cost you over _price.estimate_   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: It looks like there is an opening _time.appt_. -->
* Hmmm ok what is the cheapest Uber?
    - uber_lyft.type.ride: That would be _type.ride_.   <!-- predicted: uber_lyft.price.estimate_uber_lyft.type.ride: Looks like _type.ride_ is _price.estimate_ right now. -->
* That is the car _type.ride_ one right?
    - general: Yea that is right.   <!-- predicted: uber_lyft.time.pickup: _time.pickup_ -->
* Nah I want to be by _num.people_.
    - uber_lyft.type.ride.accept_uber_lyft.type.ride.reject: Ok, well I just checked and there are no _type.ride_ cars in the area.   <!-- predicted: uber_lyft.time.pickup: Your car will be there in _time.pickup_, is that okay? -->
* Ok I just get the _type.ride_ then.
    - uber_lyft.location.from.accept_uber_lyft.location.to.accept_uber_lyft.num.people.accept_uber_lyft.type.ride.accept: Ok double checking, you want a _type.ride_ for _num.people_ and it will pick you up from the _location.from_ and drive you _location.to_?   <!-- predicted: general: Oh. I am sorry. it is no longer available. -->
* Yea that is correct.
    - uber_lyft.price.estimate.accept_uber_lyft.time.pickup.accept: Uber says your estimated fare is gonna be _price.estimate_ and the driver details are on the app. They should be there shortly, _time.pickup_.   <!-- predicted: general: Ok your ride should be there soon, anything else? -->
* Thanks a lot
    - Happy to help. Is there anything else?
* No, but thanks for asking.
    - action_listen: action_listen   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->


## dlg-217d75a1-7792-49fd-807c-0e86a20fc49d
* is there a cafeteria nearby?
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: theres _name.restaurant_ in _location.restaurant_   <!-- predicted: general: Ah soo a different location? -->
* search homecooking
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: theres the _name.restaurant_ in _location.restaurant_ that a   <!-- predicted: general: When do you want to watch it? -->
* ugh. what else?
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: _name.restaurant_ in _location.restaurant_   <!-- predicted: general: They have several desserts available including chocolate lava cake. -->
* what are there ratings like?
    - general: they havent been rated by anyone yet   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* find the nearest steak house
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.reservation_restaurant_reservation.name.restaurant: _name.restaurant_name.reservation_ is in _location.restaurant_   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_ -->
* what are there ratings like?
    - general: they average _number_   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* read me one of the one star reviews
    - restaurant_reservation.name.restaurant: _name.restaurant_, _name.restaurant_   <!-- predicted: uber_lyft.type.ride: How about _type.ride_? Its going to cost twice as much. But plenty of rooms to fit everything. -->
* is there a _name.restaurant_ nearby?
    - restaurant_reservation.location.restaurant: theres one in _location.restaurant_   <!-- predicted: restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject_restaurant_reservation.time.reservation: Im sorry. _name.restaurant_ Sunday Brunch begins at _time.reservation_ -->
* wheres the closest cafe?
    - restaurant_reservation.name.restaurant: theres _name.restaurant_ just up mission st   <!-- predicted: restaurant_reservation.type.seating: They both have a _type.seating_ available, anything else? -->
* read me a one star review
    - they just opened, no reviews yet
* _name.restaurant_location.restaurant_ near _location.restaurant_?
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: _name.restaurant_ is in _location.restaurant_   <!-- predicted: general: Okay, how many people will be dining? -->
* whats the next closest cafe after _name.restaurant_?
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: _name.restaurant_ is just up _location.restaurant_   <!-- predicted: general: They have several desserts available including chocolate lava cake. -->
* ok, and the next closest?
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.reservation_restaurant_reservation.name.restaurant.accept: _name.reservation_name.restaurant_ is in _location.restaurant_   <!-- predicted: general: Oh. I am sorry. it is no longer available. -->
* what are there reviews like
    - they average _number_ with over _number_ reviews
* ok, whats there address?
    - restaurant_reservation.location.restaurant_restaurant_reservation.location.restaurant.accept: _location.restaurant_   <!-- predicted: restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.accept_restaurant_reservation.name.restaurant.reject: there are _number_ restaurants that match your request. _name.restaurant_ and _name.restaurant_ -->


## dlg-1b5d22c6-7755-4364-bbd1-61530a28f1e1
* Hello, I think I need to make an appointment with _name.store_.
    - Again?
* Unfortunately, yes.
    - Whats the issue this time?
* Well, _reason.appt_. I have an important meeting in the city tomorrow but I likely wont make it there with the nail in my tire.
    - I see. Okay, let me see what I can do.
* Thank you.
    - general: I should know this by now, but can you give me the information of your car again?   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* Yes. Its a _year.vehicle_ _name.vehicle_.
    - Okay. And which phone should I put in for the contact info?
* Just put in _name.customer_ at _number_-_number_-_number_
    - Okay, sounds good. It is pretty late in the day. What time is your meeting in the city tomorrow?
* Its _number_ PM.
    - auto_repair.time.appt: It says here they have an appointment for _time.appt_, _time.appt_, or _time.appt_.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* That wont do. I dont think Ill make it in time. Do they take same day appointments?
    - Let me call them. Please hold.
* Thanks.
    - auto_repair.date.appt_auto_repair.time.appt: Okay, I got you an appointment for _time.appt_ _date.appt_. Can you make it in time?   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* Yes, I can!
    - general: Perfect. Theres going to be a hefty fee for it being a same day appointment.   <!-- predicted: auto_repair.date.appt_auto_repair.name.customer.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt_auto_repair.year.vehicle.accept: OK. Ill confirm everything now. Your name is _name.customer_ with phone number _number_-_number_ You have a _year.vehicle_ _name.vehicle_. _reason.appt_. Youre bringing it into _name.store_ _date.appt_ _time.appt_. Is all of that correct? -->
* How much?
    - Its a hundred for the base fee, not including the new tire and service fee.
* Thats fine. Thank you!
    - auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.time.appt.accept: They will see you for your _name.vehicle_ at _time.appt_ _date.appt_.   <!-- predicted: general: Oh yeah, and preliminary inspection will cost _price_. -->
* Thanks!
    - action_listen: action_listen   <!-- predicted: general: No problem, have a safe trip Kevin. -->


## dlg-1b616ab0-e6f2-4814-b938-bd2cf78c9ac0
* Im thinking about seeing the movie _name.movie_. Can you purchase some tickets for me?
    - Sure, are you seeing the movie in town or out of town?
* In town. Try to get tickets for the theater, _name.theater_, its only about _number_ minutes away from the restaurant I plan to go to.
    - Sure. And are you going solo, or is this a date night, or a night out with friends?
* Just _num.tickets_ tickets please.
    - Is there a certain day youd like to go? And do you prefer a matinee or a late showing?
* Lets aim for Thursday, and something between _number_PM and _number_PM would be great.
    - general: Thanks! Hold on one minute so I can see what they have for you.   <!-- predicted: auto_repair.time.appt: That time is not available, there is a time _time.appt_ if that is ok. -->
* Sure, take your time.
    - movie_ticket.time.start: Thanks for holding. I have three different times that would work. _time.start_, _time.start_ and _time.start_. Which sounds best?   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* _time.start_ works. Late but not too late.
    - movie_ticket.name.movie_movie_ticket.num.tickets_movie_ticket.time.start: Alright, booking _num.tickets_ tickets for _time.start_ to see the movie _name.movie_. Just using your card thats already on file.   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: _name.theater_num.tickets_name.theater_time.start_name.movie_location.theater_ -->
* Great! Thanks
    - movie_ticket.price.ticket: One ticket is _price.ticket_, so the total is _price.ticket_ before tax. Just keeping you updated while I finalize everything.   <!-- predicted: general: Youre welcome. Anything else I can assist you with? -->
* Whew! Its not cheap to go to the movies anymore!
    - movie_ticket.price.ticket: Well, they are having a special. I can save you _number_% or _price.ticket_ if you join their Movie Club. Want me to get you signed up?   <!-- predicted: general: okay so just to confirm all the information -->
* Thatd be great!
    - movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.price.ticket.accept_movie_ticket.time.start.accept: Alright, I emailed your receipt and tickets to print for your records. I purchased _num.tickets_ tickets at the _name.theater_ in _location.theater_, to see the movie _name.movie_ at _time.start_. With the _number_% savings for their Movie Club deal, it came to _price.ticket_.   <!-- predicted: movie_ticket.price.ticket.accept: Ok, that will be _price.ticket_, Ill charge your account? -->
* Amazing. Thank you so much!
    - Youre welcome. I also sent your tickets to your mobile device as a text message in case you forget to print them out.
* Youre a life saver. Thank you so much. Have a nice day. Goodbye.
    - action_listen: action_listen   <!-- predicted: general: Have a wonderful day. Good-bye. -->


## dlg-1b67b0fa-290d-44b5-9e53-d293ccd17f64
* Id like to place an order for a _uber_lyft.uber_lyft_ ride please.
    - uber_lyft.uber_lyft: Where is this _uber_lyft.uber_lyft_ going to be taking you to and from where?   <!-- predicted: general: Ok, where are you located right now? -->
* I need the _uber_lyft.uber_lyft_ to take me from _location.from_ to _location.to_
    - uber_lyft.location.from: Where is _location.from_?   <!-- predicted: general: Where is your start and destination end points? -->
* My address is on file with them as I have generated _uber_lyft.uber_lyft_ to and from _location.from_ before.
    - Ok, I see it.
* Great.
    - What size car are you looking to get?
* Which was has the shortest wait time?
    - The _type.ride_ has it.
* What is the wait time for _type.ride_?
    - uber_lyft.time.pickup: The wait time for that would be about _time.pickup_.   <!-- predicted: general: Youll need to connect a payment source to it, then just tap the request ride option in the app and the rest is self explanatory. -->
* What about for _type.ride_?
    - uber_lyft.time.pickup: That is about _time.pickup_.   <!-- predicted: general: He is coming in a white honda civic. -->
* Ill take that one.
    - uber_lyft.location.from.accept_uber_lyft.location.to.accept_uber_lyft.ride_booking.accept_uber_lyft.time.pickup.accept_uber_lyft.type.ride.accept: Ok, _ride_booking.accept_ on _type.ride_ from your _location.from_ to _location.to_. It will be arriving in approximately _time.pickup_.   <!-- predicted: general: Okay I wills send you the information -->
* Sounds great.
    - general: Anything else that you will be needing?   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_. You can check its status on your phone. -->
* That is it for now. Thank you.
    - OK, bye.


## dlg-1b6c7fe9-222f-49b0-a37b-5fbd241f230c
* I need an appointment at _name.store_
    - I can do that, what is the issue that you need an appointment?
* _reason.appt_
    - How long has this been happening for?
* _reason.appt_
    - auto_repair.time.appt: I will contact them _time.appt_ should I give them your details?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: I can schedule you an appointment for _time.appt_ _date.appt_ -->
* Yes what details do you need
    - general: What your make and model of your car is, year phone number and name   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Ive checked _name.store_ schedule. Times available _date.appt_ are _time.appt_, _time.appt_, _time.appt_, and _time.appt_. Which would you like? -->
* _name.vehicle_ _year.vehicle_ Blue and number is _number_-_number_-_number_ name obviously is _name.customer_
    - auto_repair.name.store: I will contact them immediately, what time are you proposing you get into _name.store_?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Id like it _time.appt_, preferably later _date.appt_ or _date.appt_ _time.appt_
    - I will contact them and see what they have to say
* Let me know as soon as possible
    - auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: They contacted me and said they have an opening for you at either _time.appt_date.appt_time.appt_ or _time.appt_ _date.appt_ _time.appt_ at _name.store_   <!-- predicted: auto_repair.date.appt_auto_repair.date.appt.accept_auto_repair.time.appt: you can come in _date.appt_, at _time.appt_ -->
* _date.appt_ _time.appt_ works for me, can you please relay that information to them
    - general: Yes I can do that for you   <!-- predicted: auto_repair.time.appt: They have a _time.appt_ slot open. Is that too late for you? -->
* Thank you
    - auto_repair.date.appt_auto_repair.date.appt.accept_auto_repair.time.appt_auto_repair.time.appt.accept: I will contact them right now and let them know youre coming in _date.appt_ _time.appt_   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* Thank you so much!
    - auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection   <!-- predicted: auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_ will cost around _price_ _reason.appt_ costs _price_ -->
* Great, Ill be there at _time.appt_
    - action_listen: action_listen   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->


## dlg-1b71366e-8894-4267-aff6-26e77db2f679
* hello Im looking for an economic auto repair service
    - general: Which is why I see you are a couple?   <!-- predicted: pizza_ordering.name.store: Sure !! Yes _name.store_ is available nearby _number_ miles -->
* what are your packages
    - I need to know what he wants to do to the car
* I would like to _reason.appt_
    - that will come at a cost of _number_
* I find it economical
    - It is the cheapest place you will find in the city
* and what quality
    - general: its very good   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: It looks like there is an opening _time.appt_. -->
* really
    - general: We guarantee a job well done   <!-- predicted: auto_repair.time.appt: Yes, the have a slot available around _time.appt_. Would you like me to book that? -->
* Ill wait
    - general: If you are not happy with your money back   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* when they are available
    - auto_repair.date.appt: for _date.appt_   <!-- predicted: general: No thankyou. -->
* what time can I take the car
    - auto_repair.time.appt: _time.appt_   <!-- predicted: general: Checking now, All options have the same travel time. -->
* and even when it will be ready
    - auto_repair.date.appt.accept_auto_repair.time.appt.accept: for _date.appt_ _time.appt_   <!-- predicted: general: Yes, pick up will be ready in about _number_ minutes -->
* Sounds good to me
    - we know that there are people who need their ato as soon as possible
* youre right and I am one of themyoure right and I am one of them
    - We guarantee you will be ready
* we will see you that day
    - We will wait for it
* I think they do a good job
    - thank you very much sir
* see you later
    - we are at your service


## dlg-1b916760-70eb-4b9f-b94e-641859b18278
* Can you order me a pizza?
    - Sure. What store?
* _name.store_ in _location.store_
    - What would you like to order?
* A _size.pizza_ _name.pizza_ with _type.topping_.
    - general: Ok. Would you like anything else?   <!-- predicted: pizza_ordering.type.topping.accept_pizza_ordering.type.topping.reject: Okay they are out of _type.topping_ is _type.topping_ okay? They ran out tonight -->
* No, that’s it.
    - pizza_ordering.type.topping_pizza_ordering.type.topping.reject: Unfortunately, they don’t have enough _type.topping_.   <!-- predicted: general: Okay, is this order for delivery or pickup? -->
* I’m really feeling for some _type.topping_ right now.
    - pizza_ordering.size.pizza_pizza_ordering.type.topping: Would you like to try for a _size.pizza_ with _type.topping_?   <!-- predicted: general: Yes do you want pick up or delivery? -->
* Sure. Let’s get one _size.pizza_ with _type.topping_ and _type.topping_ and a second small pizza with _type.topping_ and _type.topping_
    - pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: You would like a _size.pizza_ pizza with _type.topping_ and _type.topping_ and a second small pizza with _type.topping_ and green peppers. Is this right?   <!-- predicted: general: Ok not an issue. Any thing else you like? -->
* Yes.
    - Would you like to order pick-up or delivery?
* Pick-up
    - What time would you like to pick-up?
* ASAP
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ It will be ready for pick-up shortly. A receipt has been sent to your phone.   <!-- predicted: general: Okay the total will be _price_ and itll be ready for pickup in _number_ minutes. -->
* Great. Thanks.
    - Will there be anything else?
* Nope, that’s it.
    - action_listen: action_listen   <!-- predicted: general: Youre welcome, enjoy. -->


## dlg-1b91c32f-b40b-4a87-9da9-088a674dd61b
* Hey, I wanted to go see a movie tonight, can you get me tickets for the movie _name.movie_?
    - Where did you want to see it?
* Im pretty much in _location.theater_, so anything around there.
    - general: Do just need a ticket for you? Any price limit or type of projection?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* No, I need _num.tickets_. Not really any limit, but lets try to keep it _price.ticket_ for the both of them and just _type.screening_, I guess.
    - movie_ticket.location.theater_movie_ticket.name.theater: Okay, I have _name.theater_ on _location.theater_.   <!-- predicted: general: okay may i know the show timing -->
* Okay, I need tickets for a showtime _time.start_.
    - movie_ticket.time.start: I only see a _time.start_ and an _time.start_ showing.   <!-- predicted: general: Okay, and how many tickets would you like? -->
* Any other theaters nearby have anything _time.start_?
    - movie_ticket.name.theater_movie_ticket.time.start: The _name.theater_ has a _time.start_ show.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* No, I dont want to see it in _type.screening_.
    - movie_ticket.location.theater_movie_ticket.name.theater_movie_ticket.time.start: _name.theater_ on _location.theater_ has a _time.start_ show.   <!-- predicted: general: Which showtime would you like on Friday? -->
* I think that will work.
    - movie_ticket.name.theater.accept_movie_ticket.num.tickets_movie_ticket.time.start.accept: Okay, so _num.tickets_ tickets for the _time.start_ at _name.theater_?   <!-- predicted: general: Do you need any accessibility devices tonight? -->
* Yeah, and its on _location.theater_?
    - movie_ticket.location.theater.accept: Yes, _location.theater_.   <!-- predicted: general: Okay. It looks like you can choose the general area you can sit. Were you looking for a seat near the front, middle, or back? -->
* Do you know how long the movie runs?
    - movie_ticket.time.duration.accept: It says _time.duration_.   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Alright, so with previews we should be out _time.end_.
    - movie_ticket.num.tickets.accept: Okay, I bought _num.tickets_ tickets, charged to your account.   <!-- predicted: general: No sir, the bar is first come first serve and it is mostly adult beverages. -->
* Good, thank you.
    - Im sending the details to your phone now.
* Thanks, have a good night.
    - Enjoy your movie.
* Thanks, bye.
    - general: Good-bye.   <!-- predicted: action_listen: action_listen -->


## dlg-1ba0d418-3a60-49ff-bcb8-b3733f3ff3ec
* Hi, Im looking for a movie recommendation.
    - Ok, what kind of movie are you looking for?
* Im thinking of an action movie.
    - general: Ok, would you like some new or older?   <!-- predicted: movie_ticket.name.movie: Okay. You want an older, serious movie, with violence and an ensamble cast. How about _name.movie_? -->
* Older should be fine.
    - Ok, how about a movie from the _number_s?
* That would be fine.
    - general: Do you have any preference for actors?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* No.
    - movie_ticket.name.movie.accept: Ok, how about _name.movie_?   <!-- predicted: general: Sorry, there are no openings for that time. -->
* No, Ive seen that too many times.
    - movie_ticket.name.movie.accept: Ok, how about _name.movie_?   <!-- predicted: general: okay let me check on that. -->
* Seen that as well.
    - movie_ticket.name.movie.accept: Ok, how about _name.movie_?   <!-- predicted: general: Done. -->
* Do you have something a bit more obscure?
    - movie_ticket.name.movie: How about _name.movie_?   <!-- predicted: general: Yes, we do have American selections like hamburgers, steak and chicken. -->
* No, saw that recently.
    - movie_ticket.name.movie.accept: Ok, how about _name.movie_?   <!-- predicted: general: Please, name one. -->
* I dont think Ive seen that, Ill go with that movie.
    - Sounds good, let me know if you need any more recommendations.


## dlg-1ba64273-a53e-4b68-a366-6083c5b74f29
* Hi, I want to order a coffee to pick up please.
    - general: Certainly, what would you like?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* I would like a _name.drink_ please.
    - general: What size?   <!-- predicted: coffee_ordering.name.drink: Sure, they have _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, and _name.drink_. -->
* I think _size.drink_ is fine.
    - coffee_ordering.preference: Would you like _coffee_ordering.preference_ with that?   <!-- predicted: general: Any Ice? -->
* Oh, yes, please.
    - coffee_ordering.type.milk: _type.milk_ okay?   <!-- predicted: general: Should I charge it to the company card? -->
* I would like _type.milk_, actually.
    - general: Sounds good.   <!-- predicted: coffee_ordering.preference.accept: Any _preference.accept_? -->
* Oh, and I want an _preference.accept_, too.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk: Okay, so its a _size.drink_ _name.drink_ with an _preference.accept_, _type.milk_ and _preference.accept_?   <!-- predicted: coffee_ordering.preference: They have both _coffee_ordering.preference_ -->
* Yes, thats right.
    - coffee_ordering.type.milk.reject: Oh, Im sorry, they do not have _type.milk_ today.   <!-- predicted: general: Ok, ordering now. I will charge your starbucks card ending in _number_ -->
* Oh, well, then Ill take _type.milk_ instead.
    - Okay they do have that.
* Ok, good.
    - coffee_ordering.location.store.accept: I see your location is one on _location.store_?   <!-- predicted: general: i ordered it, the details will be sent to your phone! -->
* Yes, the same place.
    - Great, your drink will be ready shortly. I will send the receipt to your email in a few minutes.
* Perfect! Thank you very much.
    - You are welcome, have a nice day.
* You, too, bye!


## dlg-1bacf42e-2fed-47d7-949e-3cd06813983e
* HI i want to order a pizza from _name.store_
    - okay what would you like?
* i want a three topping _size.pizza_ pizza
    - general: okay which toppings?   <!-- predicted: pizza_ordering.name.pizza.reject: I am sorry, were currently out of the _name.pizza_. Is there anything else youd like instead? -->
* _type.topping_ _type.topping_ and _type.topping_
    - okay anything else?
* I want it with _type.topping_ and _preference.accept_
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ and send you the receipt   <!-- predicted: pizza_ordering.name.pizza.reject: Unfortunately, _name.pizza_ is not an option. Is there something else you would like instead? -->
* okay how long will it take?
    - it says itll be about _number_ minutes
* okay please send me the order details
    - I will, is there anything else?
* no just the one pizza
    - alright i just sent over the receipt
* thank you
    - I will call you when your pizza is ready
* can you text or email it to me?
    - yes is text okay?
* thats fine
    - okay i will do that. have a good day
* thank you again
    - youre welcome


## dlg-1a9e57e0-7616-44d1-8a02-266aaa3b57c8
* Hey. I need you to set me up an appointment at _name.store_ for tomorrow morning please.
    - Okay. What should I say the problem is?
* My _year.vehicle_ _name.vehicle_ is in need of a _reason.appt_
    - Okay. What name and number would you like me to make this appointment under?
* Give them my name _name.customer_ and phone number (_number_)_number_-_number_
    - general: Okay. I will do that now.   <!-- predicted: auto_repair.name.store: Will do!-- later-- _name.store_ just spoke with me, bring the car in right now; but -->
* Thanks.
    - auto_repair.date.appt_auto_repair.time.appt: They cant get you in until _time.appt_. Is that okay?   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* No. See if they have anything earlier. Let them know its urgent.
    - Okay. I will see what I can do.
* Thanks.
    - auto_repair.date.appt_auto_repair.time.appt: _date.appt_time.appt_ Would that work?   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: To confirm, bring your _name.vehicle_ in _date.appt_ _time.appt_ and have the _reason.appt_ for _number_ dollars. I told them they can reach you at _number_ _number_ _number_ is that correct -->
* Perfect
    - general: Okay I will book it now.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Thanks.
    - auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Okay. You have an appointment for your _year.vehicle_ _name.vehicle_ for a _reason.appt_ _time.appt_ at _name.store_   <!-- predicted: auto_repair.name.customer.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: To confirm, you have an appointment at _time.appt_ to have your _year.vehicle_ _name.vehicle_ _reason.appt_, the fee being _price_ Your name is _name.customer_ and number is _number_-_number_-_number_ -->
* Thank you.
    - The initial inspection fee will be _price_
* Okay. Thank you
    - Youre welcome.


## dlg-1bb17a53-e78c-4233-a9a6-bfef17706b22
* _restaurant_reservation.restaurant_reservation_
    - Ill be happy to help you. Do you know which restaurant you are interested in?
* I was thinking either the _name.restaurant_ or _name.restaurant_, both in _location.restaurant_.
    - Sounds great, for which day, time and for how may people?
* I would like around _time.reservation_ on this Saturday night. It will be for _num.guests_ people.
    - restaurant_reservation.name.restaurant: Would you like me to check with the _name.restaurant_ first?   <!-- predicted: uber_lyft.type.ride: How about _type.ride_? Its going to cost twice as much. But plenty of rooms to fit everything. -->
* Yes, please.
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests_restaurant_reservation.type.seating: Okay, the _name.restaurant_ has a table for _num.guests_ but it is in _type.seating_.   <!-- predicted: restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: _name.restaurant_name.reservation_ for _ people at _, and it_num.guests_looks like _time.reservation_o have a _. Your reservation ha_type.seating_n set. Anything else? -->
* Oh, that wouldnt work. Nothing in the _type.seating_
    - restaurant_reservation.name.restaurant: Unfortunately, no. Would you like me to check the _name.restaurant_?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* Yes, please, same time, _time.reservation_ on Saturday.
    - restaurant_reservation.name.restaurant.reject: _name.restaurant_ is full on this Saturday.   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* Oh, wow...okay, can you check with the _name.restaurant_ and see if they have a table in the _type.seating_ at different time?
    - Sure Id be happy to check for you, one moment.
* Okay, thanks.
    - restaurant_reservation.name.restaurant_restaurant_reservation.time.reservation_restaurant_reservation.type.seating: Thank you for your patience, the _name.restaurant_ will have a table at _time.reservation_ in the dining room or in their _type.seating_.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* I think Ill take the table _type.seating_ room at _time.reservation_.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_uber_lyft.num.people.accept: _num.people_num.guests_ for this Saturday at _ in the evening at the _. Is that c_time.reservation_ct?_name.restaurant_   <!-- predicted: general: ok great i ordered those. Do you want me to reserve seating? -->
* Yes, thats perfect.Thank you very much.
    - My pleasure, is there anything else I can do for you?
* No, thats all I need. Thanks again.
    - You are welcome. Good bye.


## dlg-1bc0b797-62ad-4186-a747-ee03e06d0eb7
* Hi, I would like to order a pizza.
    - Where would you like to order the pizza from?
* _name.store_ on _location.store_.
    - Okay. Give me a moment.
* Okay.
    - What type of pizza would you like?
* A _size.pizza_, _type.crust_, _type.topping_
    - pizza_ordering.size.pizza_pizza_ordering.type.crust_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Okay. A _size.pizza_ _type.crust_ _type.topping_.   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->
* Wait... no. Make it a _name.pizza_.
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept: A _size.pizza_ _name.pizza_ with _type.crust_?   <!-- predicted: pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.type.topping.accept: Ok.. _name.pizza_preference.accept_type.topping_preference.accept_type.topping_..what size? -->
* Yeah!
    - general: Okay. Did you want anything else from their menu?   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->
* Uh... no. Just the pizza.
    - Is this for pickup or delivery?
* Delivery.
    - general: What is your address?   <!-- predicted: pizza_ordering.location.store_pizza_ordering.name.store_pizza_ordering.type.topping.reject: _name.store_location.store_ is out of _. Would yo_type.topping_to change your order? -->
* _number_ Adams Street.
    - Okay. The total is _price_
* Okay.
    - Should I place the order?
* Yes please.
    - The order has been placed. It should take anywhere from _number_ to _number_ minutes to arrive.


## dlg-1bc45b04-0983-480f-aeb9-a5effeb6d3c7
* Howdy! Can you buy me tickets to _name.movie_?
    - general: I sure can. What theater location are you near?   <!-- predicted: movie_ticket.name.movie: Ok, I can see where _name.movie_ is play. Do you have a city you would like to see it in? -->
* Im in _location.theater_ visiting a friend.
    - general: Any idea the closest theater to her?   <!-- predicted: movie_ticket.location.theater_movie_ticket.location.theater.accept: This movie isnt playing in _location.theater_ but it is playing in _location.theater_. -->
* She says its the _name.theater_
    - Awesome. How many tickets?
* _num.tickets_ for my friend and I.
    - What time are you looking for?
* early afternoon around _time.start_ or _time.start_. We also want to see if its available in _type.screening_.
    - movie_ticket.type.screening_movie_ticket.type.screening.reject: They do not have it available in _type.screening_.   <!-- predicted: movie_ticket.time.start: Yes, they have a _time.start_ showing -->
* They never do or at least the movies I want to see are never in _type.screening_.
    - general: I understand. They usually charge more so its almost a win they dont.   <!-- predicted: movie_ticket.location.theater.accept: The next closest theaters are about _number_ miles away in the _location.theater_ -->
* I guess. How much are tickets for afternoon showings?
    - movie_ticket.price.ticket_movie_ticket.price.ticket.accept: _price.ticket_ a person for matinee   <!-- predicted: general: Its about two men dealing with racisim. -->
* That is a steal! Im super excited about this movie.
    - So it appears they only have a _time.start_ or a _time.start_ available today.
* Ahh shucks! It makes it so hard to grab dinner. Those times stink.
    - general: Movie times are usually really weird. I can look at another theater nearby?   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_, you should receive a conformation. -->
* Yes, please do that.
    - movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: _name.theater_ has a _time.start_ showing of _name.movie_?   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.type.seating.accept: Ok it looks like they have have that time slot available _type.seating_ at _name.restaurant_ I will reserve that time slot. -->
* My friend doesnt really like that theater, but the time is a lot better so we can grab a quick bite.
    - What would you like me to do?
* Book it.
    - general: I am sending you your movie tickets to your phone right now via text message. Enjoy the show   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_ and emailed to your email address -->
* I will. Thanks.


## dlg-1bcb4db7-d907-4864-97b8-a73c7d472c9a
* _name.store_ to order something from _name.store_, can you put in an order for me?
    - Sure I can just let me know what you want and where I need to order like the location.
* _location.store_ and I will look at the menu real quick.
    - Okay take your time no problem.
* Okay
    - pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: Okay is the _name.store_ on _location.store_ okay?   <!-- predicted: general: Okay and what drink do you want? -->
* Sounds good
    - Okay what would you like?
* I want a _size.pizza_ _type.crust_type.topping_pizza_ordering.preference_ and _type.topping_ only.
    - Okay
* Have them add _pizza_ordering.preference_ to please.
    - pizza_ordering.type.topping_pizza_ordering.type.topping.reject: Okay when I placed the order they said they didnt have _type.topping_ just _type.topping_.   <!-- predicted: general: Okay anything else? -->
* Okay just nix the _type.topping_ then.
    - Okay putting in the order now.
* Great thanks so much.
    - pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping.accept: _size.pizza_ _type.crust_ pizza, _type.topping_ only but with _preference.accept_.   <!-- predicted: general: Was there anything else I can do for you? -->
* Okay thats perfect thank you so much.
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_   <!-- predicted: pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Your order for one _size.pizza_ pizza with _type.topping_ and _type.topping_ has been complete. Your pizza will be ready for pickup in about _number_ minutes. -->
* Thats perfect, thank you so much for your help.
    - Thank you and have a lovely day
* Thanks again !!!
    - action_listen: action_listen   <!-- predicted: general: Bye see you tomorrow -->


## dlg-1bcf62d0-62ae-4125-a8cd-37b1d3918416
* hey i am craving _name.pizza_ from _name.store_
    - general: ok would you want me to order it for you?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* yes can you please order a whole pizza pie. however half of the pie add _type.topping_ toppings on it and the other half add _type.topping_.
    - sure let me go ahead check that out and place the order
* great, check the price for me before you place the order
    - ok got it.
* thanx
    - pizza_ordering.name.store.accept_pizza_ordering.type.topping.reject: i checked the _name.store_ and they are out on the _type.topping_, do you want another topping?   <!-- predicted: general: Okay great. Do you want me to order that now? -->
* _type.topping_pizza_ordering.preference_ to half of it instead.
    - ok got it. the extra topping for half the pizza is going to be _price_ , still want it?
* yeah sure and how much is the total with the two toppings?
    - general: the total will be _number_ with everything?   <!-- predicted: restaurant_reservation.num.guests.accept: Everything is good to go. They did change the table size instead of a table for _number_ they did the table for _num.guests_ with extra chairs , if we have _number_ they will add a table. -->
* ok great ,im hungry so go ahead and place the order asap
    - no problem, one minute.
* I am at home and i will head out to my office in like _number_ minutes.
    - pizza_ordering.preference.accept_pizza_ordering.type.topping.accept: _type.topping_preference.accept_ and the other half _ is that correct?_type.topping_   <!-- predicted: general: Ok, they will have it ready at _number_ and just texted you the receipt. -->
* yes perfect
    - general: ok the pizza will be available for pickup within _number_ minutes.   <!-- predicted: pizza_ordering.pizza_order.accept: Just one second and I’ll give you the total cost . . . Okay, Penny.  That will be _price_ plus taxes for a total of _price_  A_pizza_order.accept_es. -->
* ok ill head out to my office so i can get there in time.
    - general: you will also get a receipt sent to you phone in a couple minutes or so.   <!-- predicted: coffee_ordering.location.store: Yes, the order has been placed so if you want to pick it up shortly, it will be available _location.store_, by your residence. Your receipt will be sent to your mobile device so be sure to check for it. -->
* ok , perfect thank you
    - ok bye
* bye


## dlg-1bd2b047-42c6-4f6a-bb64-cf78ada2f9e8
* Id like to order a coffee drink from Starbucks coffee
    - Which Starbucks location would you like me to order from?
* _location.store_
    - general: Okay, when would you need it by?   <!-- predicted: coffee_ordering.location.store: The closest Starbucks location is _location.store_. What would you like to order? -->
* As soon as possible
    - general: Alright, what would you like to order?   <!-- predicted: coffee_ordering.name.drink: Can i suggest the _name.drink_ ? Its currently being featured. -->
* A _name.drink_
    - general: What kind of milk do you want with it?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* _type.milk_
    - coffee_ordering.preference: Do you want an _coffee_ordering.preference_ or anything?   <!-- predicted: general: Should I charge it to the company card? -->
* _coffee_ordering.preference_, thank you
    - coffee_ordering.preference.accept: Do you want _preference.accept_?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* Yes, definitely
    - general: What size do you want?   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.reject: _coffee_ordering.preference_preference.reject_ available. Would you like to remove it or choose something else? -->
* The biggest one, I think its the _size.drink_
    - coffee_ordering.name.drink.accept_coffee_ordering.size.drink.accept: Okay, Ill go ahead and order the _name.drink_size.drink_   <!-- predicted: general: Do you want any flavoring in the coffee? -->
* Thank you
    - coffee_ordering.location.store_coffee_ordering.location.store.accept: no problem, it will be ready in about ten minutes and will be waiting for you at the Starbucks _location.store_   <!-- predicted: general: was there anything else you wanted? -->
* Thank you, just send the receipt to my phone
    - general: Already done, anything else?   <!-- predicted: coffee_ordering.location.store_coffee_ordering.location.store.accept: Just waiting to pick it up now at the _location.store_. I used your rewards number and told them to send the receipt via text. -->
* No, that was all thank you very much for your help
    - Thank you very much


## dlg-1bd6c244-e547-4b93-9b3e-4180decfb23d
* Hi! I need you to take care of ordering a pizza for me from _name.store_.
    - Okay, Id be happy to. How many pizzas do you want?
* Just one but it needs to be an _size.pizza_.
    - general: Okay go that. What kind of crust do you want?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* I want _type.crust_ The one with the _preference.accept_ inside.
    - pizza_ordering.name.store.accept_pizza_ordering.type.crust.reject: Sorry, _name.store_ doesnt have _type.crust_ like some places do.   <!-- predicted: pizza_ordering.name.pizza_pizza_ordering.type.topping: Who doesnt deliver these days? Alright, so a _name.pizza_ with _type.topping_  _type.topping_? -->
* Oh, right. Okay then, just get the _type.crust_
    - general: Got it. Now what toppings do you want?   <!-- predicted: pizza_ordering.type.topping.reject: Okay, just a seck. They say they are _type.topping_ You could either have it without or order something else. -->
* Since Im going vegetarian, tell me what _name.pizza_ they have on the menu?
    - pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_   <!-- predicted: general: OK. Anything else you want ? -->
* Okay load it up with _type.topping_, _type.topping_, _type.topping_ and _type.topping_.
    - pizza_ordering.preference: Okay what kind of sauce? _pizza_ordering.preference_?   <!-- predicted: general: Yea they have a couple small sized dough but its whole wheat dough -->
* _preference.accept_.
    - pizza_ordering.preference_pizza_ordering.preference.reject: Do you want any _preference.reject_preference.reject_?   <!-- predicted: general: Do you want anything else with that. -->
* No just the _preference.accept_.
    - Okay hold on while I finish getting all that.
* no worries
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_.   <!-- predicted: general: Any drinks? -->
* Can you change the time to be ready in _number_? I cant get there that fast.
    - Yes, Ill change it. Hold on.
* Okay let me know.
    - Yep okay, all finished. they are going to email the receipt for you and you pay when you get there.
* awesome, thanks!
    - No problem, enjoy!


## dlg-1bdd1347-eb45-4e00-aabd-90a565e7a10c
* Hey Emily, can you order me a pizza for delivery to the office?
    - Yes which place would you like me to place the order from?
* Lets go with _name.store_
    - general: Okay, what would you like.   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* I want to do half all the _type.topping_ and half everything
    - Which size?
* Whats the biggest size they have and how big is it?
    - pizza_ordering.name.pizza_pizza_ordering.size.pizza_pizza_ordering.size.pizza.accept: There is an _size.pizza_ pizza and something called a _name.pizza_ but they dont have measurements   <!-- predicted: pizza_ordering.name.store.accept: Without Traffic it was _number_ minutes !! if you start now there is a possibility of traffic and it may take _number_ minutes to reach _name.store_ -->
* Okay lets just go with the _name.pizza_
    - What time do you want to set the delivery to?
* As soon as possible.
    - Okay let me go ahead and place the order
* Sounds good thanks
    - general: Unfortunately, its not allowing me to do the half and half   <!-- predicted: coffee_ordering.preference: Would you like _coffee_ordering.preference_? -->
* Oh thats fine lets do the all the _type.topping_ whole pizza
    - Okay let me get that ordered.
* Okay thanks
    - pizza_ordering.type.topping.reject: I dont have the option for all the _type.topping_ but I can do the everything   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* Okay thats fine too.
    - Okay everything looks good but delivery isnt going to arrive until an hour to an hour and a half.
* Thats not going to work, can you change it to pick up?
    - Yes, pick up will be ready in about _number_ minutes
* Thats perfect, lets do that then
    - Okay, I have everything set up for pick up and details will be sent to your phone.
* Great thanks
    - action_listen: action_listen   <!-- predicted: general: Your welcome, enjoy! -->


## dlg-1be4f986-0651-4938-bce2-61cf26fead57
* Hey, Im looking to book a reservation for _num.guests_ _time.reservation_ at either _name.restaurant_location.restaurant_name.restaurant_. Both are in _location.restaurant_. Id really prefer Menton if possible.
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject: I can help you with that. Lets see...Im sorry but it looks like theres no reservations available tonight at _name.restaurant_.   <!-- predicted: uber_lyft.type.ride: How about _type.ride_? Its going to cost twice as much. But plenty of rooms to fit everything. -->
* Shoot! Thats too bad. Well, check on _name.restaurant_ then.
    - restaurant_reservation.num.guests_restaurant_reservation.restaurant_reservation_restaurant_reservation.time.reservation: Looking it up right now. Yep, it looks like they have _restaurant_reservation.restaurant_reservation_time.reservation_num.guests_. What time would you like the reservations for?   <!-- predicted: general: Would you use a shopping cart to carry the gear if the arena had some? -->
* Great. _time.reservation_ please.
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work   <!-- predicted: general: Okay your reservation has been made. -->
* How about _time.reservation_ then?
    - restaurant_reservation.name.restaurant_restaurant_reservation.num.guests_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation_restaurant_reservation.type.seating.accept: That works. So a _type.seating_ for _num.guests_ at _name.restaurant_ _time.reservation_, correct?   <!-- predicted: restaurant_reservation.time.reservation: Reservations are available for the following times _time.reservation_, _time.reservation_, and _time.reservation_. What time would you like to book a reservation? -->
* Yes, thats right.
    - restaurant_reservation.type.seating: It looks like they have both _type.seating_ seating and _type.seating_ seating. Do you have a preference.   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_. Enjoy your feast. -->
* Its _number_ degrees outside, which do you think Id prefer?
    - restaurant_reservation.type.seating: The _type.seating_?   <!-- predicted: general: How would you like the invitations? How about we do a theme get together, make it fun spice things up. -->
* You got it Einstein. I dont want to freeze with my date!
    - restaurant_reservation.type.seating: No problem. Although the site says theres _type.seating_ seating. Does that make a difference   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_. Enjoy your feast. -->
* Id still prefer _type.seating_ please.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Okay...and, done! Your _type.seating_ for _num.guests_ _time.reservation_ at _time.reservation_ at _name.restaurant_ _reservation.accept_.   <!-- predicted: general: Any special diet restriction? -->
* Can you tell me the location?
    - restaurant_reservation.location.restaurant.accept: Sure, sorry about forgetting to mention that. Its at _location.restaurant_.   <!-- predicted: general: Sure no problem -->
* Thanks. Im looking forward to my hot date _time.reservation_.
    - general: I bet you are! Is there anything else I can help with?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: Theyve got _time.reservation_ available but not with the _type.seating_. Youd have to sit at _number_ different _type.seating_. -->
* Nope, all set. Thanks for your help. Good night!
    - Good night.


## dlg-1bf371ff-e4af-41d7-9915-6d71861bcc94
* Hi, I would like a drink from Peets please.
    - Ok, which location should I order from?
* _location.store_
    - Perfect. What would you like to order?
* What would you recommend?
    - coffee_ordering.name.drink_coffee_ordering.name.drink.accept: I recently had the _name.drink_ and loved it.   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* Ok. Perfect. Whats in that?
    - coffee_ordering.name.drink_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept: Its a _name.drink_ with _preference.accept_, _preference.accept_, and _preference.accept_   <!-- predicted: pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust? -->
* Ooh that sounds great.
    - general: Ok, what kind of milk would you like?   <!-- predicted: coffee_ordering.name.drink: Can i suggest the _name.drink_ ? Its currently being featured. -->
* _type.milk_ please.
    - Ok great. Anything else?
* No thats it
    - Ok perfect.
* _preference.accept_coffee_ordering.preference_?
    - Sure
* How much is that?
    - coffee_ordering.preference.accept: The _preference.accept_ is an extra dollar.   <!-- predicted: general: In _number_ minutes you can go for the coffees -->
* Perfect. Just add it to my account there.
    - coffee_ordering.coffee_order.accept: Great. _coffee_order.accept_ and you will get a receipt sent to your phone.   <!-- predicted: general: When do you plan to pick it up? Do you want me to order it right now? -->


## dlg-1aa53d7c-7c10-4d11-8131-0e3458962096
* Hey, Id like to order a pizza from _name.store_
    - Okay, and where are you located at?
* _location.store_
    - pizza_ordering.location.store.accept: Okay, got it. The nearest store is on _location.store_   <!-- predicted: general: Great! Okay, I can order here online, what would you like? -->
* Yep, thats the one!
    - general: What would you like   <!-- predicted: pizza_ordering.pizza_ordering: What type of _pizza_ordering.pizza_ordering_ do you want to order? -->
* A _name.pizza_ please.
    - pizza_ordering.type.topping.reject: Sorry, unfortunately the store is out of _type.topping_.   <!-- predicted: general: OK. Anything else you want ? -->
* _name.pizza_.
    - Okay, what size?
* _size.pizza_.
    - What kind of crust?
* _type.crust_.
    - Okay, anything else?
* Nope, just one pizza.
    - general: Okay the total will be _price_ and itll be ready for pickup in _number_ minutes.   <!-- predicted: pizza_ordering.location.store_pizza_ordering.name.store_pizza_ordering.type.topping.reject: _name.store_location.store_ is out of _. Would yo_type.topping_to change your order? -->
* Okay cool, Ill head there now.
    - Sounds great, anything else I can do for you?
* Nope, thats it.
    - Enjoy your meal!


## dlg-1bf38562-12d1-492a-b6fb-9bb0ed836a93
* Hi! Can you order a Lyft for me?
    - Sure! Where do you need to be picked up from?
* Have them pick me up from _location.from_, please.
    - general: Okay, got it. Where do you want to go?   <!-- predicted: uber_lyft.location.from: That is _location.from_ right? -->
* _location.to_.
    - Got it. What type of Lyft car do you need?
* I have a few people with me. Whats the price difference between a normal _type.ride_ and an _type.ride_?
    - uber_lyft.price.estimate_uber_lyft.price.estimate.reject: _price.estimate_s between _price.estimate_, and the XL ranges from _price.estimate_.   <!-- predicted: uber_lyft.price.estimate: In order, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_ -->
* Awesome, so Ill do the XL. How long will the ride take?
    - uber_lyft.duration.estimate: It says it should take _duration.estimate_   <!-- predicted: uber_lyft.time.pickup.accept: So schedule the Uber for _time.pickup_? -->
* Great!
    - When do you need to be picked up?
* As soon as possible, please.
    - Okay, Ill have it sent immediately.
* Perfect, thanks!
    - uber_lyft.duration.estimate.accept_uber_lyft.location.from.accept_uber_lyft.location.to.accept_uber_lyft.price.estimate.accept_uber_lyft.type.ride.accept: No problem! Just to confirm, I have an _type.ride_location.to_location.from_ and taking you to _location.to_. The ride will cost between _price.estimate_ and will take about _duration.estimate_   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_. You can check its status on your phone. -->
* That all sounds great.
    - general: Its on its way now and the driver will meet you out front.   <!-- predicted: uber_lyft.time.pickup.accept: Your uber will be arriving in _time.pickup_. Is there anything else I can do? -->
* Wonderful, thank you so much!
    - Youre welcome! Let me know if theres anything else you need!


## dlg-1bf53399-e985-4878-a5c6-8721633fc787
* Hello, I was calling about reserving some movie tickets to see _name.movie_?
    - general: Okay, where would you like to see it?   <!-- predicted: movie_ticket.num.tickets: How many people will be joining you, just _num.tickets_? -->
* The _location.theater_ _name.theater_.
    - Alright, how many tickets would you like?
* Just _num.tickets_.
    - Alright, what day would you like to see it on?
* Tuesday.
    - What time?
* _time.start_.
    - Oh, Im sorry. Theres no times available that early, would you like to see it at a later time on Tuesday?
* No thanks, I guess Ill reserve tickets for a different movie like... _name.movie_?
    - Sure thing! Same date and time for that movie?
* Yes.
    - Okay, anything else I need to know?
* Yes Id like to see it in _type.screening_.
    - movie_ticket.type.screening_movie_ticket.type.screening.reject: Oh Im sorry, once again there is no _type.screening_ seating for that movie at that time. Would you like to change the time?   <!-- predicted: general: Unfortunately, there is not. -->
* No, I guess I just wont get tickets today. Thank you for your help.
    - general: No problem! Im sorry I couldnt assist you more. Please do let me know if you change your mind.   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_, you should receive a conformation. -->
* I will, goodbye.
    - general: Goodbye.   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->


## dlg-1c0af1fa-39e8-4fe4-9a4e-aebdb4f18465
* Hi, Id like to order a _size.drink_ _name.drink_
    - What kind of milk would you like?
* _type.milk_
    - coffee_ordering.name.drink_coffee_ordering.size.drink_coffee_ordering.type.milk: Ok, so thatll be a _size.drink_ _name.drink_ with _type.milk_?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* Yes
    - general: Anything else?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* No, thatll be it
    - coffee_ordering.name.drink.reject: Sorry, sir, we are actually out of _name.drink_. Would you like a different drink?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Hold on, one second let me take a look
    - No worries, take your time sir
* Alright, Ill have a _name.drink_ _size.drink_, with _type.milk_
    - general: Ok, and thatll be it?   <!-- predicted: coffee_ordering.preference: _coffee_ordering.preference_ too? Thats optional. -->
* Correct
    - How would you like to pay?
* I have a starbucks account already with my credit card information
    - Ok, one second, let me pull it up
* Ok
    - coffee_ordering.coffee_order.accept_coffee_ordering.location.store.accept: Alright sir, _coffee_order.accept_. It will be ready shortly at _location.store_. Youll receive a text message for receipt   <!-- predicted: coffee_ordering.coffee_order.accept: _coffee_order.accept_, the drink should be ready for pick up soon, the receipt will be sent to your phone -->
* Thank you
    - Youre welcome. Have a nice day


## dlg-1c124f8e-db5d-4c3d-948e-cd1f5030a87c
* hello Amy, I need to book an appointment to get my car checked out.
    - auto_repair.name.customer.accept: Hello _name.customer_. Where is your car to be picked up at, and where would you like me to take it to have it checked out?   <!-- predicted: general: Good morning! What can I help you with? -->
* I will leave it parked outside my office . I would like you to take it to _name.store_.
    - auto_repair.name.store.accept: OK, I will set up an appointment with _name.store_. Where can I find the keys?   <!-- predicted: general: Okay, I will send someone now to get you. Whats your name? -->
* I have left the keys in the sun visor. The vehicle door code is _number_
    - general: Very good. What shall I tell the shop about the condition of the car?   <!-- predicted: auto_repair.time.appt: Yes, there is an appointment slot for _time.appt_. -->
* Yes, _reason.appt_
    - general: Alright, I will let them know. They said the more specific the better. Is there any other details you can tell me about the problem?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: Ok, the auto shop recommends an appointment time of _time.appt_ _date.appt_, is this convenient? -->
* Yes, _reason.appt_.
    - OK. I will make note of that.
* Also, it is only noticeable at speeds above _number_ miles per hour.
    - general: Alright, I will contact the shop. Is there a time that works best for me to schedule the appointment.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Yes. I will be leaving it at my office on _date.appt_, the sooner I can get it back the better.
    - auto_repair.date.appt_auto_repair.time.appt: OK. I have been in contact with the shop and they can take it around _time.appt_ _date.appt_time.appt_.   <!-- predicted: general: Not this time! Remember last time when you pissed yourself in front of the whole board of directors? -->
* Sounds good. Did they say when I would get the car back?
    - general: He said they wont know for sure how long the repair will take until they get the car in and diagnosed.   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* Alright, did they mention how much it would cost.
    - auto_repair.reason.appt.accept: They said it _reason.appt_ which would be around _price_ to repair. Again, they wont know for sure until they diagnose the problem. There is a _price_ flat fee for diagnosis.   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* OK, sounds good. Let me know when they get the diagnosis finished and get the quote in.
    - auto_repair.date.appt: Will do. I will be by on _date.appt_ to pick up the car.   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Fantastic. Thank you!
    - action_listen: action_listen   <!-- predicted: general: Oh yeah, and preliminary inspection will cost _price_. -->


## dlg-1c14fc2e-6712-4a36-8afa-a066d5c3f30b
* Hello, I would like to order a coffee from Starbucks?
    - sure, which starbucks would you like me to go?
* Ah, does not matter. The closet one, _location.store_.
    - general: You are funny, what would you like to drink?   <!-- predicted: coffee_ordering.name.drink: Sure, they have _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, and _name.drink_. -->
* I am feeling more that _name.drink_ today.
    - general: What size?   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.accept: I could ask them to _preference.accept_. Or a particular roast, how do you feel about their blonde roast? -->
* _size.drink_
    - What kid of milk do you want?
* With _type.milk_.
    - general: Noted, do you want any flavor?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* Yes, _preference.accept_ please.
    - coffee_ordering.preference: okay, and any _coffee_ordering.preference_ or _coffee_ordering.preference_?   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* _coffee_ordering.preference_preference.accept_coffee_ordering.preference_preference.accept_ you know I am on diet.
    - general: Oh Yes, sorry about that.   <!-- predicted: coffee_ordering.type.milk.reject: Got it! OMG! Looks like they are all out of _type.milk_! Do you have another milk choice? -->
* No worries.
    - Anything else?
* No that would be good.
    - coffee_ordering.location.store: Okay, I just placed an online order at the store in _location.store_.   <!-- predicted: general: I agree. -->
* Oh, good. I like the _name.drink_ there. They are fast.
    - general: Yes, the drink will be ready to be picked up in _number_ minutes.   <!-- predicted: coffee_ordering.type.milk: The cold foam can be made with _type.milk_ or _type.milk_ only but not _type.milk_ -->
* okay.
    - You will soon get the receipt in your phone via starbucks app.
* Great! Thank you.
    - action_listen: action_listen   <!-- predicted: general: No problem, enjoy your Starbucks! Bye! -->


## dlg-1c1a3c23-b779-4bb4-8518-94a263264871
* Hi Sue, Could you please order me a couple of pizzas from _name.store_?
    - Absolutely. What are you thinking?
* Well they are all vegetarians...
    - pizza_ordering.name.store.accept: Does _name.store_ do a vegetarian pizza?   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* yes - we will need to ask for substitutions though
    - I dont think they will do substitutions
* Lets beg them to. Its the only pizza I am comfortable with serving.
    - I agree. What should I order?
* _pizza_ordering.preference_type.topping_ and _type.topping_pizza_ordering.preference_
    - general: ok let me order on post mates   <!-- predicted: coffee_ordering.preference.accept: The _preference.accept_ is an extra dollar. -->
* perfect.
    - pizza_ordering.preference_pizza_ordering.type.topping.reject: _type.topping_pizza_ordering.preference_....   <!-- predicted: general: Your total will be _price_ and your receipt will be texted to you. -->
* _type.topping_pizza_ordering.preference_ and _pizza_ordering.preference_?_type.topping_
    - general: on the entire pizza?   <!-- predicted: coffee_ordering.preference.accept: The _preference.accept_ is an extra dollar. -->
* no - lets do _type.topping_ and _pizza_ordering.preference_type.topping_
    - There is no option for that.
* I hate how you cant add notes anymore
    - Me too. Should I just order it on the entire pizza?
* yes - that works.
    - ok great. How many?
* _number_
    - wow _number_?
* yes
    - general: ok they will need _number_ hours for the order   <!-- predicted: pizza_ordering.pizza_order.accept: Okay, _pizza_order.accept_ and it will be ready to be picked up in about _number_ minutes. -->
* thats fine but we cant wait much longer than that.
    - I understand. I will get their early to pick them up.
* thank you so much!
    - pizza_ordering.name.pizza.accept_pizza_ordering.type.topping.accept: _type.topping_name.pizza_ and _name.pizza_ pizzas _type.topping_ext _number_ hours?   <!-- predicted: general: Was there anything else I can do for you? -->
* yes. correct.
    - general: GOT IT!   <!-- predicted: uber_lyft.ride_booking.accept: Ok. _ride_booking.accept_. If there is anything else you need, please feel free to ask. -->


## dlg-1c247359-1717-42d6-8cfd-cefc34f2d274
* Hey Cynthia. Can you book a _type.seating_ at _name.restaurant_ next _time.reservation_ for _num.guests_ people please. It is my anniversary. _type.seating_ is fine if there is no seating _type.seating_
    - general: Oh happy birthday. Ill book it right away.   <!-- predicted: restaurant_reservation.name.reservation.accept_restaurant_reservation.name.restaurant.accept: _name.restaurant_name.reservation_ does not provide any live music but they do have music. -->
* Thank you very much.
    - restaurant_reservation.time.reservation_restaurant_reservation.type.seating.reject: Im sorry, they dont have any _type.seating_ available _time.reservation_ Would you like me to pick a different day?   <!-- predicted: general: Youre welcome enjoy your dinner. -->
* Oh okay, I guess that is fine. We can do Saturday any time _time.reservation_.
    - Okay I will call again to make the arrangements.
* Thank you very much.
    - Im sorry, they are busy all weekend. Maybe you should try a different place instead.
* Okay, can you try _name.restaurant_ in _location.restaurant_?
    - What time and day?
* Thursday _time.reservation_ is ideal for us.
    - I will call right now to confirm
* Thank you very much.
    - restaurant_reservation.type.seating_restaurant_reservation.type.seating.accept_restaurant_reservation.type.seating.reject: They said there is no _type.seating_ at all. Would you be fine sitting _type.seating_?   <!-- predicted: general: My pleasure, anything else I can do? -->
* Do they have _type.seating_? I heard it might be cold this week.
    - general: Yes they do.   <!-- predicted: restaurant_reservation.time.reservation: Unfortunately we do have live music. They dont start until _number_pm though, so if youd like to come in by _time.reservation_ you should be finished by the time they start. -->
* Yes, please make that arrangement then.
    - restaurant_reservation.time.reservation.accept: Okay I will. _time.reservation_   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.type.seating.accept: Ok it looks like they have have that time slot available _type.seating_ at _name.restaurant_ I will reserve that time slot. -->
* Okay, that is perfect. Thank you.
    - Youre welcome. Happy anniversary! Do you need me to pick up a gift, or arrange flower delivery?
* No thank you, youve already done enough.
    - action_listen: action_listen   <!-- predicted: general: Okay do not be late and call us if anything changes. -->


## dlg-1c24c8ba-e8b8-4545-b705-0b802335c295
* I would like to order a coffee
    - From where?
* Starbucks
    - What is the address?
* The one on _location.store_
    - What would you like?
* _name.drink_
    - general: What size?   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* _size.drink_
    - What type of milk?
* _type.milk_
    - Anything else?
* Could I also get _coffee_ordering.preference_?
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.type.milk.accept: Yes, to confirm that is a _name.drink_ with _type.milk_ and _preference.accept_   <!-- predicted: general: Of course, any other customizations? -->
* Correct
    - The order has been made and will be ready for pickup shortly
* Thank you
    - The receipt will be sent your email
* Thank you
    - goodbye


## dlg-1c2a3382-363f-4f2f-8406-26df4c927508
* Hi, I was wondering if you could order a pizza for me.
    - Sure, that wont be a problem.
* Awesome. Its my daughters birthday and I would like to order her favorite pizza.
    - Ok. What would you like for me to order?
* I would love a _name.pizza_.
    - Ok, what size?
* A _size.pizza_. And instead of the _type.topping_pizza_ordering.preference_type.topping_ instead.
    - general: Ok, great.   <!-- predicted: pizza_ordering.size.pizza: Sir, do you think that will be _size.pizza_ enough for the meeting? -->
* Can you repeat it back to me so I know you got it?
    - pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept_pizza_ordering.type.topping.reject: Sure. I have a _size.pizza_ _name.pizza_, instead of _type.topping_preference.accept_type.topping_. Correct?   <!-- predicted: general: okay good choice i will text you the payment -->
* Yes, that sounds perfect.
    - Do you want to pick up the pizza?
* Yes, I prefer to pick up.
    - Since you have an account through them, Ill send the receipt to your email.
* Sounds good.
    - Did you need or want anything else?
* No, thats it!
    - general: Ok, your pizza will be ready for pickup in _number_ minutes.   <!-- predicted: pizza_ordering.location.store_pizza_ordering.name.store_pizza_ordering.preference.accept_pizza_ordering.size.pizza_pizza_ordering.type.crust.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Great. So to confirm your order, you want two _size.pizza_ pizzas, both _type.crust_ with _preference.accept_. You want _type.topping_, _type.topping_, _type.topping_, and _type.topping_ on the first, and _type.topping_, _type.topping_, and black olives on the second, and you want to pick them up at the _name.store_ location on _location.store_. Does that all sound right? -->
* Awesome, thank you!
    - No problem.


## dlg-1c2cb50c-43b7-4ab5-ba07-46d680c919ab
* Hi there Id like a pizza from _name.store_
    - general: Sure thing what kind do you want.   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* Hmmm I thibk Im gonna go with _name.pizza_ this time, with _pizza_ordering.preference_ please.
    - general: Ok and what size did you want it to be?   <!-- predicted: coffee_ordering.name.drink: Sure, they have _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, _name.drink_, and _name.drink_. -->
* _size.pizza_ definitely.
    - pizza_ordering.size.pizza: They actually dont make that pizza that size but it is _size.pizza_ an then you can papa size it up.   <!-- predicted: general: OK. Anything else you want ? -->
* I mean sure I guess thats fine.
    - Great what toppings did you want on it?
* Well _pizza_ordering.preference_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_.
    - Got it anything else?
* Nah thats it.
    - pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Ok so thats a _size.pizza_ _name.pizza_ with _preference.accept_ _type.topping_, _type.topping_, _type.topping_, and _type.topping_?   <!-- predicted: general: Ok, they will have it ready at _number_ and just texted you the receipt. -->
* Yes that is right.
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ and the pizza will be ready for pickup in about _number_ minutes.   <!-- predicted: general: Your new total is _number_. Do you accept this charge? -->
* Great thats not a long time.
    - Nah thats pretty quick,actually.
* Yeah well thanks.
    - No problem and the reciept will be sent to youre phone.
* Ok thanks again, bye.
    - Bye bye.


## dlg-1aa8e6f7-1e85-4fe3-af31-e2516f522f77
* I need you to order a Lyft for me, its been a heck of a day and I need a drink
    - Ha, we all have those. What are you thinking?
* Just going from _location.from_ to _location.to_..Ive heard good things about _location.to_
    - uber_lyft.location.from: Can you remind me which _location.from_ youre at?   <!-- predicted: general: Ok, where in the plaza? -->
* Sure...its _location.from_
    - Are you still out by the airport or in the city now?
* In the city, think its called _location.from_
    - Ah, yeah, ok, I see that one now.
* Great, and headed to a _location.to_
    - Sure, let me see whats in the area...
* Someone was telling me about a place I would like...I think it was called _location.to_?
    - uber_lyft.location.to.accept: Hmm...one sec...yeah, ok, _location.to_?   <!-- predicted: general: Okay. Ill get right on that. -->
* Yeah, that sounds right. They said it was just _location.to_?
    - Yep, thats what Im seeing on the map
* Great, lets do that.
    - Yep, got it. One sec...do you care what kind of car?
* Whatever gets me there the fastest
    - uber_lyft.time.pickup.accept: It looks like its about _time.pickup_ for all of them   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: It looks like there is an opening _time.appt_. -->
* Sure, then whatevers cheapest?
    - uber_lyft.price.estimate.accept_uber_lyft.type.ride: A _type.ride_ will be about _price.estimate_, _type.ride_ will be about half that.   <!-- predicted: general: Ok, checking the app now. -->
* For that price, might as well just do the _type.ride_.
    - Ok. Ive requested the Lyft and it should be on its way. You can keep an eye on it on your phone
* Awesome, thanks!
    - action_listen: action_listen   <!-- predicted: general: Youre welcome. Anything else I can assist you with? -->


## dlg-1c2e164b-9a6b-4c77-ba00-15e29b2f5c8e
* Hey, Im looking for a high class restaurant to _num.guests_ to _time.reservation_.
    - Ok. What kind of food are you looking for _time.reservation_?
* Oh, nothing extraordinary. Just standard American cuisine. But I want it to be good.
    - restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject: Ok. How about the _name.restaurant_? Its got a spectacular view of the city.   <!-- predicted: general: Hi! What kind of movie do you like to watch? -->
* Thats great and all, but my wife isnt a fan of heights.
    - Ah. Ok. Then thats probably a bad choice.
* Yeah. What else do you recommend?
    - restaurant_reservation.name.restaurant: How about _name.restaurant_?   <!-- predicted: restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.reject_restaurant_reservation.time.reservation: Im sorry. _name.restaurant_ Sunday Brunch begins at _time.reservation_ -->
* Never heard of it, tell me more.
    - Theyve got some of the best steaks in town and VERY high class. Your wife would be honored to go here.
* Sounds good. But do they have good drinks?
    - Why, of course! Some of the best wine youve ever tasted. But be careful, it gets spendy.
* Dont worry about money, anything for my wife.
    - Of course, and what time would you like the reservation for?
* How about _time.reservation_?
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Looks like theyre all booked up for _time.reservation_ unfortunately   <!-- predicted: general: What kind of table would you prefer? -->
* What about _time.reservation_?
    - restaurant_reservation.time.reservation_restaurant_reservation.type.seating: _time.reservation_ is wide open. Would you like a _type.seating_ or _type.seating_?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: I apologize, but they dont have any _type.seating_ available on that date at _time.reservation_. -->
* _type.seating_. My wife enjoys the extra privacy
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Ok. Everything is set up. Youve got a reservation for _num.guests_ at _name.restaurant_, a _type.seating_ of course, for _time.reservation_   <!-- predicted: general: Sounds awesome; Valerie just called and asked about the dinner...is she part of the party? -->
* Great. That sounds fantastic.
    - Anything else I can help with?
* No. Thank you for your help.
    - action_listen: action_listen   <!-- predicted: general: Youre welcome enjoy your dinner. -->


## dlg-1c2ea836-910f-4961-afa0-cc2813feba34
* I need a _uber_lyft.uber_lyft_ please.
    - Where to and from?
* I need a _uber_lyft.uber_lyft_ from _location.from_ to _location.to_.
    - What type of ride would you like?
* I would like prices for _type.ride_
    - uber_lyft.price.estimate_uber_lyft.type.ride: _type.ride_ are _price.estimate_   <!-- predicted: uber_lyft.time.pickup_uber_lyft.type.ride_uber_lyft.type.ride.accept_uber_lyft.type.ride.reject: An _type.ride_ is unavailable. An _type.ride_ is _time.pickup_ away. Would that work? -->
* Actually that is not in my budget.
    - uber_lyft.price.estimate_uber_lyft.type.ride: May I suggest a _type.ride_ for _price.estimate_?   <!-- predicted: uber_lyft.type.ride: Ok so not an _type.ride_ but a _type.ride_? -->
* Oh, that still is too high.
    - uber_lyft.price.estimate.accept_uber_lyft.type.ride.accept: Okay, well they have a _type.ride_ for _price.estimate_.   <!-- predicted: general: that service isnt available in your area right now -->
* That will work for me.
    - Sounds like a plan.
* Can I have a _type.ride_ for that ride?
    - uber_lyft.type.ride: No, they only have _type.ride_.   <!-- predicted: uber_lyft.ride_booking.accept: Yes, _ride_booking.accept_y. You can check status on your phone. -->
* That is fine.
    - general: Great I will book for you with your card on file.   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_. You can check its status on your phone. -->
* Thanks!
    - uber_lyft.ride_booking.accept: _ride_booking.accept_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Thanks!
    - You can check the status on your phone.
* Bye!
    - Bye!


## dlg-1c4d45ab-2de4-48c6-8f18-c4db5fe32811
* Hi rachel, I need your help with a situation?
    - Whats the problem?
* _reason.appt_
    - how do you know this sir?
* _reason.appt_
    - auto_repair.name.store: can you book an appointment with _name.store_.   <!-- predicted: general: Oh, bummer. Whats up? -->
* okay I am putting us on a _number_ way call right now
    - auto_repair.reason.appt: I am trying to book an appointment for a _reason.appt_?   <!-- predicted: general: Ok. Can you remind me the name of the garage you usually take it to? -->
* The Model of the car is _name.vehicle_ year _year.vehicle_
    - general: when do you want the appointment sir?   <!-- predicted: auto_repair.date.appt.reject_auto_repair.time.appt.reject: _time.appt_date.appt_ -->
* _time.appt_ if possible I have to drive to a very important meeting in the _time.appt_
    - auto_repair.time.appt: the time right now is _time.appt_, what time do you want the appointment for?   <!-- predicted: general: Yes, actually there is an availability then. -->
* _time.appt_
    - auto_repair.time.appt_auto_repair.time.appt.reject: i just checked, there is no free time for _time.appt_   <!-- predicted: auto_repair.time.appt: Upon checking, it looks like _time.appt_ is available. Is _number_ a.m. okay? -->
* how about _time.appt_?
    - Yes _time.appt_ is free
* how much is it going to cost?
    - general: the diagnosis first is _number_usd and then the cars fixing is estimated at _number_usd   <!-- predicted: auto_repair.time.appt: Upon checking, it looks like _time.appt_ is available. Is _number_ a.m. okay? -->
* go ahead and book an appointment
    - auto_repair.time.appt.accept: i just booked it for _time.appt_, total price after tax was _number_   <!-- predicted: auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_ -->
* thank you
    - action_listen: action_listen   <!-- predicted: general: Look forward to seeing you soon John. -->


## dlg-1c4dad3e-f9b9-4dfe-be88-fd43d88cc167
* I need to make an appointment at _name.store_ repair shop.
    - Ok, what do I need to tell them.
* That I have _year.vehicle_ _name.vehicle_
    - general: What is the appointment for?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _reason.appt_
    - general: Is that all?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: They will take it at _time.appt_ otherwise they cant take it until _date.appt_. -->
* Might as well ask for an _reason.appt_.
    - general: Ok, I can see here online that they can do that for you.   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_. -->
* I need this to happen as soon as possible.
    - general: They are showing they dont have any open times until _number_ days from now.   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_. -->
* No it needs to happen sooner than that, _reason.appt_.
    - general: I see online that they do have emergency situation appointments.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt: Okay, it says that you are booked to get checked out at _time.appt_ _date.appt_. -->
* Is there an extra cost for that?
    - Yes, the hourly rate goes up from _price_ to _price_
* Ok, I dont have a choice but forget the _reason.appt_ part.
    - general: Ok when do you want me to set it up for.   <!-- predicted: auto_repair.time.appt: They have a _time.appt_ slot open. Is that too late for you? -->
* _date.appt_ at _time.appt_
    - auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.time.appt.accept: Ok I have an appointment for _time.appt_ _date.appt_ at _name.store_   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* Great!
    - general: They need your personal information for the appointment.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* Ok give them my name _name.customer_ and phone _number_-_number_-_number_
    - general: Got it   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->


## dlg-1c5ca982-47c5-4368-9c74-902cc8f49766
* I want to have some good japanese food
    - do you have a restaurant in mind
* yes, lets make a reservation at _name.restaurant_
    - general: what time?   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->
* tonight at _time.reservation_
    - for how many people
* for _num.guests_
    - restaurant_reservation.time.reservation.reject: I just check with them and they are fully booked at _time.reservation_   <!-- predicted: general: Okay, how many people will be dining? -->
* what about _time.reservation_
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: they dont take reservation after _time.reservation_   <!-- predicted: restaurant_reservation.name.restaurant_restaurant_reservation.name.restaurant.accept_restaurant_reservation.time.reservation: _name.restaurant_ Sunday brunch starts at _time.reservation_ -->
* that sounds like a pickle
    - restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: they said you can come and wait at _time.reservation_, they usually would have a table in _number_ minutes   <!-- predicted: restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Okay, they have a _type.seating_ tomorrow at _time.reservation_. _reservation.accept_ -->
* well, we can always switch to another restaurant
    - you are right
* _name.reservation_name.restaurant_, same detail at the first reservation
    - general: let me check with them   <!-- predicted: restaurant_reservation.type.seating: Ok do you want _type.seating_ or _type.seating_? -->
* you have their number right?
    - yes I do
* let me knows how it goes
    - restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: the appointment is made, they have reserved a table for you for _num.guests_ at _time.reservation_, the reservation is under your name   <!-- predicted: general: Just let me know what you want to do -->
* thank you
    - you are welcome


## dlg-1c5e0840-7637-43e4-a6e8-e47538d84ff5
* Hi there. Can I get you to swing by and get me a coffee on the way back to the house please?
    - Sure. Where would you like me to pick it up from?
* Starbucks. Theres one right here by the _location.store_ They always make the best coffee.
    - No problem. What kind of coffee would you like?
* An _name.drink_ sounds great.
    - general: Okay, any specifics, are you ok with the milk they use in it?   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.accept: I could ask them to _preference.accept_. Or a particular roast, how do you feel about their blonde roast? -->
* No, thank you, as a matter a fact, I want _type.milk_ instead.
    - coffee_ordering.preference: Are you okay with the _coffee_ordering.preference_ on top?   <!-- predicted: general: What kind of milk do you want with it? -->
* Oh yeah, please tell them _coffee_ordering.preference_ I like my whipped cream!
    - general: What size would you like?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.preference.reject_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Okay! So thats a _size.drink_ _name.drink_ made with _type.milk_, with _preference.reject_. Right? -->
* A _size.drink_ will do the trick.
    - coffee_ordering.location.store_coffee_ordering.name.drink_coffee_ordering.preference_coffee_ordering.size.drink_coffee_ordering.type.milk: Okay, so I have a _size.drink_ sized _name.drink_, _type.milk_, _coffee_ordering.preference_ from Starbucks in _location.store_, correct?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ok, _num.drink_ _preference.accept_, _, _size.drink_ a_type.milk_type.milk_preference.accept_ -->
* Yes, thats correct. Oh, and have them _coffee_ordering.preference_, and extra on topof the coffee as well, and a _coffee_ordering.preference_ the _coffee_ordering.preference_ on top of my _coffee_ordering.preference_.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Lets see, a _size.drink_ _name.drink_ _type.milk_ _preference.accept_, _preference.accept_ _preference.accept_   <!-- predicted: pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Got it! Let me repeat what I’ve got so you can verify it. You want a _size.pizza_ _name.pizza_ with double toppings of _type.topping_, _type.topping_preference.accept_type.topping_ and _number_ Garlic Dipping Sauces. And half of the pizza will have _preference.accept_. Is that correct? -->
* You got it.
    - coffee_ordering.preference.reject: Well, Im sorry to be the bearer of bad news, but they are out of the _preference.reject_ that goes in there. Do you still want this kind?   <!-- predicted: general: Ok, ordering now. I will charge your starbucks card ending in _number_ -->
* Yes,  just tell them to _preference.accept_p instead.
    - No problem, Ive got you.
* Thank you so much.
    - coffee_ordering.coffee_order.accept: _coffee_order.accept_ and Im headed there to pick it up now. Ill see you in about _number_ minutes.   <!-- predicted: general: You can pick up the order in _number_ minutes, but if you are running late the order will be made when you get there so the ice does not melt. -->
* Thank you, cant wait.
    - action_listen: action_listen   <!-- predicted: general: You can pick up the order in _number_ minutes, but if you are running late the order will be made when you get there so the ice does not melt. -->


## dlg-1c728a20-4099-40a6-aa5c-0186a3350b2d
* I would like to order an _name.drink_
    - coffee_ordering.name.drink: _name.drink_, what location are you wanting the drink from?   <!-- predicted: general: Starbucks or peets coffee? -->
* The location at _location.store_
    - general: Ok, what size would you like the drink to be?   <!-- predicted: coffee_ordering.location.store: The closest Starbucks location is _location.store_. What would you like to order? -->
* I would like a _size.drink_ size
    - general: What type of milk would you like in the drink?   <!-- predicted: coffee_ordering.type.milk: What kind of creamer? Theyve got _type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_. -->
* _type.milk_ is fine
    - coffee_ordering.preference: Ok, would you like to add any _coffee_ordering.preference_   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* _preference.accept_coffee_ordering.preference_coffee_ordering.preference_
    - Ok, would you like to add any other items your order today?
* No, thatll be all. Thanks
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ok, so to confirm your order. You have a _size.drink_ _name.drink_ with _preference.accept_, and _type.milk_. Is that correct?   <!-- predicted: general: Would you like to pick this up now or in the future? -->
* Yes, it is.
    - general: Ok, did you want me to go ahead and charge this to the account we have on file for you?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* Yes, please
    - general: Ok your total is _number_ and itll be charged to your credit card associated with the account.   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* Ok, perfect.
    - general: Your estimated time for pick-up is in _number_ minutes. Is that ok?   <!-- predicted: coffee_ordering.coffee_order.reject: This is outstanding your order will be ready in _number_ minutes _coffee_order.reject_ -->
* Yes, thats fine.
    - coffee_ordering.location.store.accept: Ok, your order will be ready for pick-up in ten minutes at the _location.store_. Your receipt will be sent to you via text message.   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* Ok, great thank you, goodbye.
    - action_listen: action_listen   <!-- predicted: general: You are welcome. See you tomorrow. -->


## dlg-1c7846f3-4ca0-4b1a-808c-e6b8527d6bce
* I would like for you to _pizza_ordering.pizza_ordering_ from _name.store_
    - okay. What would you like?
* _name.pizza_type.topping_.
    - general: Okay, what size do you want?   <!-- predicted: pizza_ordering.preference_pizza_ordering.preference.reject: _pizza_ordering.preference_preference.reject_? -->
* I want an _size.pizza_
    - Anything sides like a drink, bread sticks or cinnamon sticks?
* Ummm, I will get a two liter sprite and cinnamon sticks.
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Okay, so thats an _size.pizza_name.pizza_type.topping_ and a two liter sprite and cinnamon sticks?   <!-- predicted: pizza_ordering.preference.reject_pizza_ordering.type.topping: _type.topping_preference.reject_. -->
* Yes
    - okay, I am going to login using your saved details to your account and place the order.
* Thank you.
    - okay, it will be about _price_
* on second thought you can add breadsticks too and marinara dipping sauce
    - pizza_ordering.size.pizza.accept: ok, so _size.pizza_ pizza, cinnamon and breadsticks and a two liter sprite?   <!-- predicted: pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Yes, so you want a _size.pizza_ instead of _size.pizza_? -->
* yes that is correct
    - ok, I will modify and order
* You can use my card on file.
    - general: Ok, your receipt will be sent to your mobile device via text message.   <!-- predicted: pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Your order for one _size.pizza_ pizza with _type.topping_ and _type.topping_ has been complete. Your pizza will be ready for pickup in about _number_ minutes. -->
* when will it be ready?
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ and the pizzas will be ready for pickup in about _number_ minutes.   <!-- predicted: general: Yeah, it will be ready for pick up in about _number_ minutes. -->
* Can you also pick it up?
    - Sure, I will leave for it in a few minutes.
* Thank you.
    - action_listen: action_listen   <!-- predicted: general: My pleasure -->


## dlg-1c7f5f22-13f9-46b8-933a-b9d4ccc5dc50
* Hi, can you find tickets for the _name.movie_ movie?
    - Sure, for what city?
* _location.theater_ would be best.
    - Sounds good. What time?
* _time.start_ is perfect.
    - Ok. For how many people?
* _num.tickets_ people.
    - movie_ticket.type.screening: Did you want to see it in _type.screening_?   <!-- predicted: general: any preference for seating? -->
* No thank you.
    - movie_ticket.name.theater_movie_ticket.time.start: Ok, there is one showing at the _name.theater_ at _time.start_   <!-- predicted: movie_ticket.name.movie.reject_movie_ticket.num.tickets: There are no showtimes for _name.movie_ with _num.tickets_ available within the next hour either. Would you like to try a different time? -->
* Thats not far at all. Ill take that one.
    - movie_ticket.price.ticket: The cost is _price.ticket_ per person plus tax.   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->
* Ok, great.
    - Are you ready for me to read the information back to you?
* Yes.
    - movie_ticket.location.theater.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Ok, I have purchased tickets at the _name.theater_ in _location.theater_ for the _time.start_ showing.   <!-- predicted: movie_ticket.price.ticket.accept: Okay, that will be _price.ticket_ -->
* Great!
    - Do you need any other information like directions?
* No, I have the information. Thank you.
    - Youre welcome.


## dlg-1c9febcf-2752-496c-9379-04c6df007e67
* Will you please order me a pizza from the closest _name.store_?
    - Certainly. Do you want it delivered?
* No, I will pick it up when I leave the office.
    - general: Not a problem. What size would you like?   <!-- predicted: pizza_ordering.size.pizza: There are _number_ slices in a _size.pizza_. -->
* I would like one _size.pizza_ _type.crust_ pizza.
    - general: Are you looking for any toppings on the pizza?   <!-- predicted: pizza_ordering.type.topping.accept_pizza_ordering.type.topping.reject: Okay they are out of _type.topping_ is _type.topping_ okay? They ran out tonight -->
* I am going to go healthy with _type.topping_ and _type.topping_.
    - What kind of pepper would you like?
* The _type.topping_ probably. What are the other kinds of peppers?
    - They have _type.topping_, _type.topping_, _type.topping_, or _type.topping_
* I will go with the _type.topping_. Thanks
    - pizza_ordering.name.pizza_pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Ok so one _size.pizza_ _name.pizza_ with _type.topping_nd _type.topping_ for pick-up?   <!-- predicted: general: Would you like something else instead? -->
* Actually make that _type.topping_type.milk_type.topping_.
    - pizza_ordering.type.topping: _type.topping_ and _type.topping_ for your toppings then?   <!-- predicted: general: Okay, any thing else with that? -->
* That is correct. Thank you.
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping.accept: Alright I am placing the order for one _size.pizza_ _type.crust_ _name.pizza_ pizza with _type.topping_ and _type.topping_.   <!-- predicted: general: Your pizza should be ready in about _number_ minutes. -->
* Yes, I will pick it up when I leave.
    - It has been ordered and will be ready in _number_ minutes.
* Thank you so much.
    - Your receipt will be texted to your mobile.
* That is perfect. I appreciate your help.
    - Not a problem. Enjoy your pizza.


## dlg-1ab17b1f-9495-4e21-a286-e2884def112e
* Hi, Id like help picking a restaurant for a date
    - ok, what type of cuisine are you looking for?
* I dont really care, I just want to find something special.
    - Ok, would you like for me to search for best date restaurants recommended on Yelp?
* Yes, please
    - Ok, which location?
* Anything in _location.restaurant_ would work.
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: Ok. The top hits for best date resaurant in _location.restaurant_ on Yelp are _name.restaurant_, _name.restaurant_, and _name.restaurant_.   <!-- predicted: general: Okay, let me check that for you. How many people are attending? -->
* Can you tell me more about _name.restaurant_?
    - restaurant_reservation.location.restaurant_restaurant_reservation.name.restaurant: Yes. _name.restaurant_ is at _location.restaurant_. It has _number_ out of _number_ stars on Yelp, with _number_ reviews. Its tagged as Breakfast  Brunch, Mediterranean, and Cocktail Bars.   <!-- predicted: restaurant_reservation.name.restaurant: Ive searched the area, theres a _name.restaurant_ not too far from your office -->
* I know that place, its great. Can you check if they have a _type.seating_ for _num.guests_ available _time.reservation_?
    - restaurant_reservation.num.guests_restaurant_reservation.time.reservation: Yes, let me check, one second. Ok, I see they have an opening for _num.guests_ at _time.reservation_ and _time.reservation_ tonight.   <!-- predicted: restaurant_reservation.time.reservation: Sure thing. Looks like Theres an opening for _time.reservation_. Is that okay? -->
* Oh, that doesnt work. Can you tell me about those other restaurants you recommended?
    - restaurant_reservation.name.restaurant: _name.restaurant_ or _name.restaurant_?   <!-- predicted: general: Yes, they have a fully stocked sit down bar with premium wines and liquors. -->
* _name.restaurant_?
    - restaurant_reservation.location.restaurant_restaurant_reservation.location.restaurant.accept_restaurant_reservation.name.restaurant: _name.restaurant_ is at _location.restaurant_. It has _number_ out of _number_ stars on Yelp with _number_ reviews. Its tagged as TapasSmall Plates.   <!-- predicted: general: What kind of table would you prefer? -->
* Ok, how much is it?
    - general: Its rated as _number_ out of _number_ dollar signs on Yelp.   <!-- predicted: restaurant_reservation.time.reservation: It looks like they wont have a table available until _time.reservation_ tomorrow -->
* Ok, that sounds nice. Do they have any openings for _num.guests_ for _time.reservation_?
    - general: Let me check, one second. Yes, they have many times avilabile. What is your prefered time?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject: Oh Im so sorry, actually _time.reservation_ is booked. But they have spots open at _time.reservation_, _time.reservation_, or _time.reservation_. Would any of those work -->
* Anytime _time.reservation_.
    - restaurant_reservation.time.reservation: They have an opening at _time.reservation_. Shall I reserve this for you?   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.type.seating: _time.reservation_ _type.seating_ reservations available are _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_, and _time.reservation_. -->
* Yes please.
    - restaurant_reservation.location.restaurant_restaurant_reservation.location.restaurant.accept_restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: Ok, I have made a reservation for _num.guests_ at _time.reservation_ at _name.restaurant_, _location.restaurant_. I have sent a confirmation by text to your phone.   <!-- predicted: restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.reservation.accept_restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Okay...and, done! Your _type.seating_ for _num.guests_ _time.reservation_ at _time.reservation_ at _name.restaurant_ _reservation.accept_. -->
* Great, thank you! Can you put this in my google calendar?
    - Yes, anything else?
* No, thats it thanks
    - general: Ok, have a good day!   <!-- predicted: action_listen: action_listen -->


## dlg-1ca539f6-1d8e-4ea5-ba6b-45a3a53795a8
* Hello, Id like _num.tickets_ tickets for the _time.start_ showing of _name.movie_.
    - general: Sure. I just need to know which location.   <!-- predicted: movie_ticket.name.theater: Ok, Ive found tickets at _name.theater_, _name.theater_ and _name.theater_, which do you prefer? -->
* _name.theater_ in _location.theater_.
    - general: No problem, let me check that for you.   <!-- predicted: movie_ticket.name.theater: Okay. I see one theater, _name.theater_. -->
* Ok. Thank you.
    - movie_ticket.time.start.reject: It looks like the _time.start_ showing is no longer available. Would you like to try something else?   <!-- predicted: movie_ticket.name.theater.accept: I see _name.theater_ theater has good ratings. -->
* Darn, ok. How about the _time.start_ showing of _name.movie_?
    - At what location would you like?
* The same one, _name.theater_ in _location.theater_.
    - Ok one moment while I check that reservation.
* Ok, no problem.
    - general: Im sorry, but it looks like theres only _number_ ticket left.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Thats no good.
    - general: Im sorry, but both choices seem to be full on reservations.   <!-- predicted: movie_ticket.ticket_booking.accept_movie_ticket.time.start.accept: Ok. _ticket_booking.accept_ for tonight at _time.start_. I am texting the receipt and tickets to your mobile device. -->
* Thats okay. Thank you.
    - general: Would you like to check anything else?   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->
* No thanks.
    - general: Okay, Thank you for calling.   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->
* Thank you for your time.
    - Have a good day.


## dlg-1cb967b1-3aef-43b2-a5f2-0407bf29d42f
* I need to schedule a repair for my car at _name.store_.
    - Okay. What seems to be the problem with your car?
* _reason.appt_.
    - What is the problem with the lights?
* _reason.appt_.
    - general: What is the make and model of your vehicle?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: I can schedule you an appointment for _time.appt_ _date.appt_ -->
* Its a _name.vehicle_.
    - auto_repair.name.vehicle: What year was your _name.vehicle_ released in?   <!-- predicted: general: There is a _price_ service charge that will be included in the bill. Is this okay? -->
* _year.vehicle_
    - general: May I have your name?   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Ive checked _name.store_ schedule. Times available _date.appt_ are _time.appt_, _time.appt_, _time.appt_, and _time.appt_. Which would you like? -->
* _name.customer_.
    - May I have your phone number?
* _number_-_number_-_number_
    - What time would you like to schedule your repair?
* How about _date.appt_ at _time.appt_.
    - general: Sorry, they are currently full at that time?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: Ok. Today is _date.appt_. Can you come in _date.appt_ _time.appt_ -->
* Is _time.appt_ open?
    - Yes, _time.appt_ is avilable.
* Thats fine then.
    - auto_repair.appointment.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: _appointment.accept_ for _time.appt_ to _reason.appt_. The fee for the repair will be _price_   <!-- predicted: general: Your appointment has been made. Please be advised that there is a _price_ inspection fee. -->


## dlg-1ce9b799-23a7-4da2-8195-a78ed63d9a65
* Hey Kim, Can you call _name.store_ _auto_repair.auto_repair_? Im driving and cant go online right now.
    - Of course, whats happening with your car?
* _reason.appt_
    - Ok no problem, what is the make and model of your car?
* Its a _year.vehicle_ _name.vehicle_
    - Ok so i see a spot opened for _date.appt_ at _time.appt_.
* Thats to long from now. Is there anything _time.appt_?
    - general: Hold on let me take a look. Let me refresh the page.   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* Ok cause i need them to look at this problem _time.appt_.
    - So there is something opened for _time.appt_ _date.appt_.
* Ok that will work. book it for me.
    - auto_repair.reason.appt: ok and this is _reason.appt_, would you like to add _reason.appt_ to?   <!-- predicted: general: Is the car otherwise functioning normally? -->
* I guess, might as well schedule it now before they try to sell it to me at the shop.
    - general: Good idea to think ahead.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt: Okay, it says that you are booked to get checked out at _time.appt_ _date.appt_. -->
* Ok so do you need my card or anything to hold it.
    - general: no i have all your information here.   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt.accept: Okay, I have you scheduled for _date.appt_ at _time.appt_ -->
* ok great.
    - auto_repair.appointment.accept_auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: so _appointment.accept_ at _name.store_ _date.appt_ at _time.appt_ for _reason.appt_. is there anything else?   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.name.vehicle.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Okay so I have told them that _name.customer_ will be bringing her _year.vehicle_ _name.vehicle_ in at _time.appt_ _date.appt_. Phone number _number_-_number_ Anything else? -->
* No thats all i need for now. thanks alot!
    - no problem, anytime!


## dlg-1cf40349-5842-4d1a-b23d-1eddd94f2918
* Hi I would like to order a ride
    - Where do you want to be picked up and where are you going to
* This will be from _location.from_ to a _location.to_.
    - Great are there any other passengers
* _num.people_ people
    - What time will that be.
* _time.pickup_
    - Great what type of car do you want
* An _type.ride_
    - general: Oh I am sorry that is not available.   <!-- predicted: uber_lyft.type.ride: There is an _type.ride_ and _type.ride_ right now. -->
* Darn  is _type.ride_t available.
    - uber_lyft.price.estimate: Let me check...Yes it is and that will will be _price.estimate_   <!-- predicted: general: I can check. -->
* Can you tell me what the _type.ride_ is.
    - uber_lyft.type.ride.accept: That would be a _type.ride_ ride with a professional driver.   <!-- predicted: general: They have several desserts available including chocolate lava cake. -->
* I think we would like that one if available.
    - Let me check...yes it is available.
* Great lets book that.
    - uber_lyft.price.estimate.accept: Ok that will be _price.estimate_   <!-- predicted: general: Ok, please hold. -->
* Ok sounds good. Thank you!
    - Please be ready _time.pickup_ and you are welcome.


## dlg-1d0b0fe1-74b0-4af2-a91d-33bad93184d2
* Hi, can you get me a coffee from Starbucks?
    - Did you have a specific Starbucks in mind?
* I think the closest one is on _location.store_.
    - What would you like?
* Id like an _name.drink_.
    - general: What size?   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.accept: I could ask them to _preference.accept_. Or a particular roast, how do you feel about their blonde roast? -->
* I think Ill just take a _size.drink_.
    - general: What kind of milk would you prefer?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Ill have _type.milk_ if they offer it. Otherwise, Ill just get _type.milk_.
    - coffee_ordering.preference.accept: Would you like _preference.accept_ on top?   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* Yeah, that sounds delicious.
    - general: Is there anything else special you would like?   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* No, I think thats it.
    - general: Would you like me to put it on your personal account?   <!-- predicted: coffee_ordering.coffee_order.accept_coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: _coffee_order.accept_ a _size.drink_name.drink_preference.accept_ with _type.milk_ milk and _preference.accept_ for you _location.store_ You will receive a text shortly with an update on your order. -->
* Yes that would be perfect. Whats the total cost?
    - Itll be three dollars and sixty-five cents.
* Sounds good.
    - The order has been placed and it should be ready for pickup very soon.
* Thanks! Thats great.
    - Ill text you the receipt.
* Thats perfect. Thanks!
    - action_listen: action_listen   <!-- predicted: general: Anytime, do you need anymore assistance? -->


## dlg-1d0c55cd-9bc0-4605-85e2-0723200d4e1b
* Hi sweetie, can you possibly order me some Starbucks?
    - Sure thing! Which location you wanna pick it up at?
* _location.store_, please.
    - coffee_ordering.location.store_coffee_ordering.location.store.accept: _location.store_?   <!-- predicted: general: I agree. What should I order? -->
* Yes, thats the one!
    - Gotcha. Whats your order today?
* I think Im going to try something new. How about their _name.drink_?
    - That sounds delicious. What size you want?
* _type.milk_size.drink_.
    - coffee_ordering.size.drink: Alrighty, _size.drink_ it is.   <!-- predicted: general: Perfect, whats the best pick up location? -->
* Id also like to get it made with _type.milk_, please.
    - general: You got it. Anything else?   <!-- predicted: coffee_ordering.preference: Would you like it _coffee_ordering.preference_ or _coffee_ordering.preference_ -->
* Yes, actually I dont want the _coffee_ordering.preference_ of that either. Just the _preference.accept_.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.preference.reject_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Okay! So thats a _size.drink_ _name.drink_ made with _type.milk_, with _preference.reject_. Right?   <!-- predicted: general: Well thats a mouthful. -->
* Yep, thats right!
    - coffee_ordering.coffee_order.accept: Alrighty, _coffee_order.accept_ Itll be ready to pick up shortly.   <!-- predicted: coffee_ordering.location.store.accept: Okay, the drink should be ready at _location.store_ for pickup in _number_ minutes. -->
* Thank you, dear! Whats the total on that?
    - It came out to _price_ and they said theyll be sending your receipt via text to your phone.
* Wonderful! Thanks again. Bye bye.
    - Anytime! Talk to you later.


## dlg-1d289a60-b0f3-44c7-beaa-689d61e484c9
* Hi, Id like tickets to see _name.movie_ in _location.theater_
    - movie_ticket.location.theater.accept: Do you mean _location.theater_?   <!-- predicted: movie_ticket.movie_ticket_movie_ticket.name.movie: _movie_ticket.movie_ticket_name.movie_, where would you like to see it? -->
* Yes, thats right.
    - Got it.
* I want _num.tickets_ tickets for tonight.
    - Is there a theater you want to see this at?
* Tell me what theaters are available
    - movie_ticket.name.theater: There is only one theater, _name.theater_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Well, the Cinema it is then.
    - movie_ticket.name.theater.accept: You want tickets to _name.theater_?   <!-- predicted: movie_ticket.time.start.reject: there is no _time.start_ show -->
* Yes
    - general: What show time do you want?   <!-- predicted: movie_ticket.price.ticket.accept: Okay, that will be _price.ticket_ -->
* Id like something in the evening. What times does it play?
    - Show times are _time.start_ and _time.start_
* Are there any more times tomorrow?
    - Show times on Thursday are at _time.start_ and _time.start_
* Is there anything later?
    - No
* Are there different show times on weekends?
    - movie_ticket.time.start: Show times are _time.start_ and _time.start_ every day   <!-- predicted: movie_ticket.name.movie_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.time.start: Okay There is a _time.start_ screening for _name.movie_ at _name.theater_ -->
* Crap, that sucks
    - general: I am sorry   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: i have _num.tickets_ to _name.movie_ at _time.start_ in _location.theater_ -->
* Well, can I get _num.tickets_ tickets for _time.start_ today?
    - movie_ticket.num.tickets: Let me check on that. Yes, there are _num.tickets_ tickets available.   <!-- predicted: movie_ticket.time.start: Ok they do have a couple times available but unfortunately they only have _number_ openings _time.start_ and _time.start_. -->
* Is there dining service at the theater?
    - general: There are snacks and beverages available.   <!-- predicted: movie_ticket.type.screening.reject: No, there is no _type.screening_. -->
* How about stadium seating?
    - There is no stadium seating available.
* OK, give me _num.tickets_ tickets, cheapest price availalble.
    - movie_ticket.num.tickets.accept_movie_ticket.price.ticket_movie_ticket.price.ticket.accept: I have _num.tickets_ tickets at _price.ticket_ apiece for you.   <!-- predicted: movie_ticket.price.ticket.accept: Theyre _price.ticket_ for booking online. -->


## dlg-1d3c62e3-d2b1-476e-a52b-be8d1b25aa8d
* Honey, could I _pizza_ordering.pizza_ordering_ for pick up?
    - Sure thing, what would you like?
* Could I get an _size.pizza_name.pizza_type.topping_type.topping_ on _type.crust_?
    - pizza_ordering.type.crust.reject: I am sorry we are out of the _type.crust_ until tomorrow. Would you like a different type of crust?   <!-- predicted: general: Certainly. Do you want it delivered? -->
* Yes, lets go with _type.crust_.
    - pizza_ordering.size.pizza_pizza_ordering.type.crust_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: OK, so you want an _size.pizza_ _type.crust_ pizza with _type.topping_ and _type.topping_?   <!-- predicted: general: Sure, let me check for availability, it make take a few minutes. Please be patient. -->
* That is correct.
    - OK, we have that on your order.
* Thanks.
    - Would you like anything to drink with that?
* No thanks.
    - general: Can I get you anything else today?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* No thanks.
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping.accept: OK I have one _size.pizza_ _type.crust_name.pizza_type.topping_type.topping_, is that correct?   <!-- predicted: general: Your order has been confirmed and will be ready for pickup shortly. Your receipt will be sent to you through your mobile device via text message. -->
* Yes, thats correct.
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_   <!-- predicted: general: Is there anything else you want to order? Theyre doing a Monday night special two pizzas for the price of one. Would you like to order a second pizza? -->
* Great thank you.
    - You are most welcome, have a great day.
* Thank you, you too.
    - general: I will, goodbye.   <!-- predicted: action_listen: action_listen -->


## dlg-1d3d6854-62f7-4e43-a5bd-da90325ecdcc
* can you help me get some tickets to see _name.movie_?
    - general: sure I can help you with that, what city are you in   <!-- predicted: movie_ticket.name.movie: Ok, I can see where _name.movie_ is play. Do you have a city you would like to see it in? -->
* I am in a _location.theater_
    - do you have a particular theatre in mind?
* no, just anywhere in _location.theater_ that is playing _name.movie_
    - movie_ticket.name.movie: what time would you like to see _name.movie_   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.theater.accept: I have tickets available in _name.theater_ in _location.theater_ -->
* I was hoping to see it tomorrow around _time.start_
    - movie_ticket.location.theater.accept_movie_ticket.location.theater.reject_movie_ticket.name.theater_movie_ticket.time.start.reject: _name.theater_ _location.theater_location.theater_name.theater_ both have showtimes at _time.start_ tomorrow, will that work   <!-- predicted: general: Okay, let me check ticket availability for that showing. -->
* that sounds just about right
    - how many tickets would like to get
* just _num.tickets_, one for me and one for my friend
    - it looks like both those viewings are sold out
* are there any other showtimes near _time.start_ tomorrow?
    - movie_ticket.location.theater_movie_ticket.name.theater_movie_ticket.time.start: _location.theater_ has a sho_time.start_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* that would definitely work
    - movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: Ok, I have purchased _num.tickets_ for you at _location.theater_ to see _ at _name.movie_time.start_   <!-- predicted: general: Do you need any accessibility devices tonight? -->
* excellent!
    - movie_ticket.ticket_booking.accept: _ticket_booking.accept_ as a text message.   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* awesome, thank you!
    - you are welcome, bye!


## dlg-1d3d8118-40ee-4dfb-a724-be5ebb956802
* I would like to buy movie tickets to _name.movie_
    - What location sir?
* _location.theater_ please.
    - Sure I will check on that for you.
* Great!
    - Any particular time?
* Yes _time.start_ Im taking a friend of time.
    - Unfortunately that is not available sir.
* Ok, how about the movie _name.movie_ at _time.start_?
    - I can check on that for you sir.
* Thanks I will wait
    - movie_ticket.time.start.reject: That is not available at _time.start_   <!-- predicted: general: The restaurant offers valet service and there is paid parking garages around the area. -->
* Oh no
    - movie_ticket.type.screening_movie_ticket.type.screening.reject: Would you like to see it in _type.screening_?   <!-- predicted: general: Okay I wills send you the information -->
* No thank you
    - general: Do you still want movie tickets?   <!-- predicted: movie_ticket.name.movie.reject_movie_ticket.num.tickets: There are no showtimes for _name.movie_ with _num.tickets_ available within the next hour either. Would you like to try a different time? -->
* Not at this point
    - general: Ok sorry sir   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.time.start.accept: Enjoy _name.movie_ At the _location.theater_ at_time.start_ -->
* Its ok I will find something else today to
    - Great, I will catch you later.


## dlg-1abb1f12-65f8-4dab-9413-f7155d777932
* Hi, Im looking for really good spanish food in _location.restaurant_
    - restaurant_reservation.name.restaurant: I see a couple of great highly rated choices in that area. First is _name.restaurant_ and then There is _name.restaurant_   <!-- predicted: general: Hi! What kind of movie do you like to watch? -->
* Which is higher rated?
    - restaurant_reservation.name.restaurant.accept: _name.restaurant_ is. Would you like me to book a table for you?   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* yes, that would be good.
    - How many in your party?
* There are _num.guests_, it is for a birthday celebration.
    - Congratulations to the birthday boygirl.
* Thanks, can you get me a large table like that?
    - when did you want to go?
* I want to go _time.reservation_.
    - restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.time.reservation.reject: Let me check, Ok.. _time.reservation_ has no room for a table of _num.guests_, you could do that at _time.reservation_. and book _number_ tables, they said they can accomodate you by pushing _number_ together. Is that ok?   <!-- predicted: general: Any special diet restriction? -->
* Yes, I think I can make that work.
    - Ok. Ill book you right away.
* what are they known for there?
    - They serve great Tapas..they are known for that BUT they have delicious main dishes as well.
* Ok.. what is their rating?
    - They have a Michelin star there.
* Nice. Is there a dress code or any info I need?
    - No dress code but it is a sort of fancy place - you might feel comfortable if you dress up.
* Thank you, will remember that.
    - restaurant_reservation.reservation.accept: _reservation.accept_. I can send you an e mail reminder in the morning.   <!-- predicted: general: Let me just confirm with the restaurant -->
* That would be great, Mucho Gracias.
    - action_listen: action_listen   <!-- predicted: general: okay payment will be done youll get your confirmation -->


## dlg-1d4a8868-5167-43b7-9edc-fa242786a854
* Hi, I want to order a drink from Starbucks please at _location.store_, OK.
    - general: What would you like?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* Id like a _name.drink_ please.
    - general: What size?   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.accept: I could ask them to _preference.accept_. Or a particular roast, how do you feel about their blonde roast? -->
* I want a _size.drink_ please.
    - coffee_ordering.size.drink.reject: Im sorry they are all out of _size.drink_ cups at the moment.   <!-- predicted: coffee_ordering.preference.reject: Any _preference.reject_ -->
* Okay, I can have a _size.drink_ please.
    - general: Sure thing. What would you like in it?   <!-- predicted: coffee_ordering.type.milk: What kind of milk would you like--_type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_? -->
* Id like _coffee_ordering.preference_ please.
    - general: No problem. Anything else? What type of milk?   <!-- predicted: coffee_ordering.preference.accept: Would you like _preference.accept_ and _preference.accept_ in the coffee? -->
* Id like _type.milk_ in it.
    - general: Any toppings for the drink?   <!-- predicted: coffee_ordering.preference: That is available! _coffee_ordering.preference_. Any other additions? -->
* How about _coffee_ordering.preference_
    - Sure thing.
* Thanks!
    - coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Ive placed your order for a _size.drink_ _name.drink_ with _preference.accept_ and _type.milk_ at _location.store_   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.reject: _preference.reject_coffee_ordering.preference_. Do you still want the same drink minus the salt? -->
* Thank you.
    - Your order will be ready for pickup shortly and the receipt will be sent to your mobile phone.
* I will be happy to get it soon!
    - Goodbye
* Goodbye
    - action_listen: action_listen   <!-- predicted: general: Ah soo a different location? -->


## dlg-1d5446d4-7506-427d-a7d8-66565e7aaad7
* Hello! I need to buy _num.tickets_ _movie_ticket.movie_ticket_ to see the movie _name.movie_.
    - Okay. What is the city of the movie theatre?
* I wanted to go to _name.theater_ in _location.theater_.
    - movie_ticket.location.theater_movie_ticket.name.theater: All right. Which _name.theater_ in _location.theater_ do you prefer?   <!-- predicted: general: Okay, and how many tickets would you like? -->
* Id like tickets to _location.theater_.
    - Okay. What time were you interested in?
* There are a couple of showtimes that would work. Either the _time.start_ or the _time.start_?
    - general: And where were you wanting the seats to be located?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* I always prefer the seats directly behind the handicapped railing in the center.
    - movie_ticket.time.start: It looks like there arent any center handicapped railing seats for the _time.start_ showing, and center seats for the _time.start_, but further back.   <!-- predicted: general: Yes, I see lots of seats in other sections. -->
* Oh no, okay. Well, what about the _name.movie_ movie?
    - general: Okay. What showtimes interested you?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* It looks like they have a _time.start_ and a _time.start_.
    - All right. Did you have the same seat preferences?
* Yes, please.
    - movie_ticket.num.tickets.reject_movie_ticket.time.start: Im sorry. It looks like they dont have _num.tickets_ seats available next to each other at the _time.start_ showtime, and no center seats at the _time.start_ showtime.   <!-- predicted: movie_ticket.location.theater_movie_ticket.name.movie_movie_ticket.name.theater_movie_ticket.num.tickets_movie_ticket.time.start: Should I order _num.tickets_ for _name.movie_ At _location.theater_ _ sh_time.start_ith stadium seating? -->
* Seriously?
    - general: Yes, I am sorry. Was there another movie or showtime that interests you?   <!-- predicted: movie_ticket.location.theater_movie_ticket.name.movie_movie_ticket.name.theater_movie_ticket.num.tickets_movie_ticket.time.start: Should I order _num.tickets_ for _name.movie_ At _location.theater_ _ sh_time.start_ith stadium seating? -->
* No. Ive lost interest in seeing a movie now.
    - general: Im sorry about that. Let me know if theres anything else you need.   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* Okay. Thank you.
    - My pleasure. Good afternoon!


## dlg-1d585579-f687-4d7f-b19a-720665455a57
* I would like to order a coffee from Starbucks.
    - Which Starbucks would you like it from?
* _location.store_.
    - Sure, which coffee would you like?
* _name.drink_.
    - Okay, what size?
* A _size.drink_, please.
    - general: Sure, would you like milk with it?   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* Yes, _type.milk_.
    - general: Okay, thats available.   <!-- predicted: coffee_ordering.preference.accept: Would you like _preference.accept_ and _preference.accept_ in the coffee? -->
* And _preference.reject_
    - general: Oh, so sorry. Thats not available right now.   <!-- predicted: coffee_ordering.preference: They have both _coffee_ordering.preference_ -->
* Okay, Ill take it without it.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Sure, so that a _name.drink_ _size.drink_ with _type.milk_, _preference.accept_   <!-- predicted: general: OK, is that all? -->
* Right.
    - coffee_ordering.location.store_coffee_ordering.location.store.accept: Okay, your drink order will be available in a few minutes at the _location.store_.   <!-- predicted: general: Ok, ordering now. I will charge your starbucks card ending in _number_ -->
* Thank you!
    - Youre welcome. Enjoy.
* Thanks, take care.
    - You, too.


## dlg-1d5c500f-e110-48d9-9ee7-d7eece6c3ed1
* Hello, Id like to make a coffee order for your _location.store_, please!
    - Of course, did you have a particular size of drink in mind when calling us today?
* _size.drink_, please.
    - coffee_ordering.preference: What _coffee_ordering.preference_ would you like the drink to be?   <!-- predicted: general: What kind of milk do you want with it? -->
* _preference.accept_.
    - general: Any additions?   <!-- predicted: coffee_ordering.preference: Would you like _coffee_ordering.preference_? -->
* Yes, I have low blood-sugar so _preference.accept_ please!
    - coffee_ordering.preference: Of course! Any _coffee_ordering.preference_ today?   <!-- predicted: general: I agree. -->
* Yes, plenty of it. Can I get it _preference.accept_?
    - Sounds delicious, of course! What flavor would you like the other half?
* _preference.accept_.
    - general: Any particular kind of of milk you need?   <!-- predicted: coffee_ordering.preference: Would you like _coffee_ordering.preference_? -->
* _type.milk_name.drink_, please. Im vegan.
    - general: Any drizzle today?   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* _preference.accept_!
    - coffee_ordering.name.drink: Of course, is it a _name.drink_?   <!-- predicted: coffee_ordering.preference: Would you like _coffee_ordering.preference_? -->
* Yes, howd you know? Oh, and _type.milk_ please!
    - coffee_ordering.name.drink.accept_coffee_ordering.size.drink.accept: It just sounded like _size.drink_ delicious _name.drink_ to me! Anything else today?   <!-- predicted: coffee_ordering.type.milk.reject: Got it! OMG! Looks like they are all out of _type.milk_! Do you have another milk choice? -->
* No, Im good.
    - coffee_ordering.location.store.accept: Perfect! Your order will be ready at _location.store_.   <!-- predicted: coffee_ordering.coffee_order.accept_coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.num.drink.accept: I have _coffee_order.accept_num.drink_name.drink_ at starbucks _location.store_ your order will be ready for pickup shortly and receipt will be sent to your mobile device via text message -->
* Wow. Thanks!
    - Anytime! I am sending you a text confirmation about your order time now. Have a great coffee day!
* You too!


## dlg-1d5e1fa5-6d93-4fae-8292-509b48e95034
* Hello there, I would like to order a _size.pizza_ _name.pizza_ from _name.store_
    - Hi, I am more than happy to make that order for you.
* I want to add two different toppings on this order.
    - general: Sure, that works. Please let me know what two toppings you would like to add.   <!-- predicted: pizza_ordering.preference_pizza_ordering.preference.reject: _pizza_ordering.preference_preference.reject_? -->
* The first topping is _type.topping_.
    - general: Great, I will add that on. What is the second topping?   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* The second topping is _type.topping_.
    - pizza_ordering.type.topping.reject: Let me check that for you. Sorry, there is no _type.topping_ available at this moment.   <!-- predicted: general: Would you like something else instead? -->
* That is fine. Please add _type.topping_ instead.
    - general: I will do that right now.   <!-- predicted: pizza_ordering.preference.accept_pizza_ordering.type.topping.accept: OK.. THEY HAVE _type.topping_ WITH _preference.accept_ -->
* Do you know if there is _number_ liter drink available?
    - Sure, let me check that for you. What type of drink do you want?
* I would like to order a _number_-liter Sierra Mists.
    - I will add that to your order.
* Great, please provide me a total cost.
    - The total cost of your order will be _price_
* Thank you so much for all of help.
    - You are welcome.
* When will order be ready?
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ and the pizzas will be ready for pickup in about _number_ minutes.   <!-- predicted: general: It will take _number_ minutes for pick-up. -->
* Thank you very much!
    - No problem.


## dlg-1d608d0c-9fd8-4557-8ee6-c3cee81c6c9f
* Hi, Tony, I need to make a dinner reservation for my family and I next week. Im thinking of going to _name.restaurant_.
    - Sure, what day and time do you need?
* I need it for _time.reservation_.
    - Ok, and how many people are going to be with you?
* Itll be _num.guests_ other people so a total of _num.guests_ people. And could you try to get a _type.seating_ for all of us?
    - restaurant_reservation.name.restaurant.reject: Oh no, _name.restaurant_ doesnt have any more availability at that time for that many people. Do you want to try a different day?   <!-- predicted: restaurant_reservation.type.seating: Excellent, would you prefer a _type.seating_ or _type.seating_? -->
* Ok, how about on _time.reservation_?
    - Sadly they have no more availability on Saturday.
* Ok, I had another restaurant in mind in case this were to happen. Could you check to see if theres availability at _name.restaurant_?
    - general: Sure, which day and time do you want me to check for?   <!-- predicted: restaurant_reservation.time.reservation: Also Im looking at the current reservations, is it possible to move to _time.reservation_? -->
* Check for the Thursday and Saturday availability, just in case.
    - Ok, let me see.... It looks like they have availability for both days and times! Which would you prefer?
* Lets do the _time.reservation_.
    - restaurant_reservation.num.guests: Ok, great. And still for _num.guests_ people, right?   <!-- predicted: general: Any special diet restriction? -->
* Yes, for _num.guests_ people. And dont forget to get a _type.seating_!
    - restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept_restaurant_reservation.type.seating.accept: Right, no problem. _time.reservation_ for _num.guests_ people in a _type.seating_.   <!-- predicted: general: Any special diet restriction? -->
* Thats right. Thank you.
    - restaurant_reservation.type.seating: No problem. Do you need a _type.seating_ or want to eat _type.seating_?   <!-- predicted: restaurant_reservation.reservation.accept: _reservation.accept_. Enjoy your feast. -->
* Definitely dont want to eat _type.seating_ and I wont need a _type.seating_, but thanks for asking.
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.reservation.accept: Of course! _reservation.accept_. Ive sent you the confirmation to your email for _name.restaurant_. Enjoy your dinner with your family!   <!-- predicted: restaurant_reservation.time.reservation_restaurant_reservation.time.reservation.reject_restaurant_reservation.type.seating_restaurant_reservation.type.seating.reject: I apologize, but they dont have any _type.seating_ available on that date at _time.reservation_. -->


## dlg-1d6a28d8-85f3-4049-a221-b459530c36cb
* Order a _pizza_ordering.pizza_ordering_.
    - Sure. Where would you like to order your pizza?
* _name.store_
    - pizza_ordering.name.store: Which _name.store_?   <!-- predicted: pizza_ordering.location.store.accept_pizza_ordering.name.store.accept: _location.store_name.store_ _location.store_his fine? -->
* _location.store_
    - What would you like to order?
* A _size.pizza_ _name.pizza_.
    - general: Would you like to order anything else?   <!-- predicted: pizza_ordering.type.topping.reject: Sorry we just ran out of _type.topping_, anything else interest you? -->
* No.
    - pizza_ordering.name.pizza_pizza_ordering.type.topping_pizza_ordering.type.topping.reject: I’m sorry. The store is out of _type.topping_ and can’t do _name.pizza_ at the moment.   <!-- predicted: general: Your order comes to _price_ How would you like to pay -->
* Oh. What about ordering a _name.pizza_ _type.topping_?
    - pizza_ordering.name.pizza_pizza_ordering.name.pizza.accept_pizza_ordering.preference_pizza_ordering.size.pizza_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.reject: A _size.pizza_ _name.pizza_ _type.topping_ has been added to your cart. Would you like anything else?   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* No.
    - When would you like to pick up?
* ASAP.
    - pizza_ordering.location.store.accept_pizza_ordering.name.pizza.accept_pizza_ordering.name.store.accept_pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept: Ok. You would like to order a _size.pizza_ _name.pizza_ _preference.accept_ at the _name.store_ in _location.store_. Is this correct?   <!-- predicted: general: Okay the total will be _price_ and itll be ready for pickup in _number_ minutes. -->
* Yes
    - pizza_ordering.pizza_order.accept: _pizza_order.accept_ You will receipt a receipt confirmation to your phone shortly.   <!-- predicted: general: Your order comes to _price_ How would you like to pay -->
* Great. Thanks.
    - Is there anything else I can assist you with?
* No. That’s it. Thanks!
    - action_listen: action_listen   <!-- predicted: general: Have a nice day. Goodbye. -->


## dlg-1d74e400-8f7e-493a-b5b2-abfd6bc80f86
* Can you make me an appointment to have my car looked at
    - Of course is there any specific repair place you want me to call?
* Yes call _name.store_ please
    - right away sir
* thank you
    - Sir i have them on the other line, they want to know what the appointment is for
* _reason.appt_
    - general: ok sir, what day and time would you like it made for   <!-- predicted: auto_repair.date.appt_auto_repair.name.store_auto_repair.time.appt: Checking... _name.store_ can get you _date.appt_ at _time.appt_. -->
* _time.appt_ _date.appt_ _time.appt_ if they can fit it in
    - auto_repair.time.appt: will _time.appt_ work sir?   <!-- predicted: general: Yes, actually there is an availability then. -->
* yes, can you get them to arrange a tow truck i dont feel safe driving it
    - i will ask them.
* ok
    - sir they need the address to pick it up from .
* its at my home address, _number_ park ave, new york
    - auto_repair.time.appt: sir, they will be there at _time.appt_ to pick it up they wanted me to tell you that you will need to be there or have someone there with the keys or they wont be able to take the car   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept_auto_repair.year.vehicle.accept: Were all set! Just so youre aware there is an initial inspection fee. Ive got you scheduled for your _year.vehicle_ _name.vehicle_ with _reason.appt_ _date.appt_ _time.appt_. If you need anything else just let me know. -->
* ill be there
    - last thing sir, what is the make an model of the vehicle?
* Its a _year.vehicle_ _name.vehicle_
    - auto_repair.date.appt.accept_auto_repair.name.store.accept_auto_repair.time.appt.accept: ok sir, everything is all set up for _time.appt_ _date.appt_ at your home for towing to _name.store_   <!-- predicted: auto_repair.date.appt.accept_auto_repair.time.appt.accept: Okay. Scheduled now. You should be there by _time.appt_ at the latest _date.appt_. -->
* Thanks
    - Your Welcome


## dlg-1d84502c-425b-42dc-94a3-971363224ffc
* Hows it going, Im looking for a movie.
    - What kind of movie?
* Im thinking an action movie.
    - general: Ok, do you want something recent or older?   <!-- predicted: movie_ticket.name.movie: Okay. You want an older, serious movie, with violence and an ensamble cast. How about _name.movie_? -->
* Older would be good.
    - general: How about something from the _number_s?   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* That would be fine.
    - movie_ticket.name.movie: How does _name.movie_ sound?   <!-- predicted: general: Okay -->
* No, Ive already seen that.
    - movie_ticket.name.movie.accept: Ok, how about _name.movie_?   <!-- predicted: general: Yea, the best part is it comes with a home-made Ranch dressing. -->
* No, Ive seen that as well.
    - movie_ticket.name.movie: Let me see, how about _name.movie_?   <!-- predicted: general: Just let me know what you want to do -->
* Ive seen that.
    - movie_ticket.name.movie.accept: Ok, how about _name.movie_?   <!-- predicted: general: Ill do that -->
* I havent seen that actually, lets go with that.
    - general: Sounds good, let me know if you need any more recommendations.   <!-- predicted: restaurant_reservation.type.seating: Ok Ill give them a call. Do you still want a _type.seating_? -->


## dlg-1d932413-eea7-4f6a-823f-77caebf9e5a0
* ACKJ_number_XLBR_number_YHF
    - Hi
* Hello
    - How can I help you?
* I would like an Uber to pick me up at _location.from_.
    - What hotel are you staying at?
* _location.from_
    - uber_lyft.location.from.accept: _location.from_?   <!-- predicted: general: How many passengers? -->
* Yes
    - How many people are riding with you?
* _num.people_ people total.
    - uber_lyft.type.ride: Would you like to use the _type.ride_ Service?   <!-- predicted: general: understood will do -->
* How is that different?
    - uber_lyft.type.ride: _type.ride_ is the lowest cost option.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* What is the estimated fare?
    - What is your destination?
* _location.to_
    - general: Let me check the rates.   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Okay. There is no _type.ride_ available it looks like. -->
* Thank you
    - uber_lyft.price.estimate: It looks like rates range from _price.estimate_ one way.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* What makes the difference in price?
    - The cost increases for larger vehicles and groups.
* I believe I will go with the lowest cost option
    - uber_lyft.price.estimate.accept_uber_lyft.type.ride.accept: OK so the _type.ride_ for _price.estimate_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Yes
    - Ok let me find an available car.
* Ok how long?
    - uber_lyft.time.pickup.accept: A car will be there in _time.pickup_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Great thank you!
    - uber_lyft.location.from: No problem have a great evening in _location.from_.   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_. You can check its status on your phone. -->


## dlg-1abd8fff-4a1a-47d5-9dc0-7726725ca624
* Im hungry, can I get a pizza from _name.store_
    - Sure, will this be for pick up or delivery?
* Pick-Up
    - pizza_ordering.location.store.accept: Are you ordering from your normal place on _location.store_?   <!-- predicted: general: Great. How many pizzas would you like to order? -->
* Yes
    - general: Alright, what would you like to order?   <!-- predicted: pizza_ordering.pizza_ordering: What type of _pizza_ordering.pizza_ordering_ do you want to order? -->
* A _size.pizza_ _name.pizza_ with the coupon for free breadsticks.
    - pizza_ordering.name.pizza.reject: I can get you the breadsticks, but they currently cant make the _name.pizza_, is there another pizza you would like?   <!-- predicted: pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Yes, so you want a _size.pizza_ instead of _size.pizza_? -->
* What other specialty pizzas work with the coupon?
    - pizza_ordering.name.pizza_pizza_ordering.preference_pizza_ordering.type.topping: _name.pizza_pizza_ordering.preference_, _name.pizza_type.topping_name.pizza_type.topping_name.pizza_   <!-- predicted: pizza_ordering.type.topping: _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_, _type.topping_ and _type.topping_ -->
* Could I get a two topping with _type.topping_ and _pizza_ordering.preference_ as a side?
    - pizza_ordering.preference: What kind of cheese? _pizza_ordering.preference_ or _pizza_ordering.preference_?   <!-- predicted: pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Yes, so you want a _size.pizza_ instead of _size.pizza_? -->
* _preference.accept_
    - Alright, is there anything else you want in addition to the breadsticks and pizza?
* Does the coupon allow for a _number_ liter soda?
    - general: No, but would you like me to order you one anyway?   <!-- predicted: pizza_ordering.name.pizza_pizza_ordering.preference_pizza_ordering.size.pizza_pizza_ordering.type.crust: Absolutely, that is a _size.pizza_name.pizza_type.crust_ with _pizza_ordering.preference_, _pizza_ordering.preference_, and _pizza_ordering.preference_ Is there anything else I can get for you? -->
* No thanks, Ill pick one up on the way over.
    - Alright, and when would you like to pick it up?
* As soon as possible.
    - pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept: Okay, I have you down for a _size.pizza_ _name.pizza_ with _preference.accept_ and a side of free breadsticks. Anything else?   <!-- predicted: general: Do you want me to put the order in now or wait a little while? -->
* Nope, were done
    - Okay, It should be available to pick up in _number_ minutes.
* Thanks.
    - action_listen: action_listen   <!-- predicted: general: Youre welcome. Anything else I can assist you with? -->


## dlg-1d99e647-cc16-4f7f-81b7-d548344eb0f1
* Hi, I need to get _movie_ticket.movie_ticket_ please?
    - Sure, in which city?
* In _location.theater_ please
    - movie_ticket.location.theater_movie_ticket.location.theater.accept: There are a few locations in _location.theater_, do you know which location?   <!-- predicted: general: Okay, I show several theaters close by. Do you have a preference on which one you would like to go to? -->
* _location.theater_name.theater_.
    - Okay, which movie?
* I want to see _name.movie_.
    - Sounds good. For how many people?
* Just _num.tickets_ adults.
    - Okay, for which day and time?
* We want o go today, around _time.start_? And we want _type.screening_.
    - Okay, let me check for you.
* Okay thanks.
    - movie_ticket.time.start_movie_ticket.time.start.reject_movie_ticket.type.screening: They have _type.screening_ at _time.start_ and _time.start_ but _time.start_ showing is sold out.   <!-- predicted: movie_ticket.name.movie_movie_ticket.time.duration.accept: _name.movie_ is PG-_number_ and runs for _time.duration_. -->
* Oh, shoot. Do they have regular one then? Not _type.screening_.
    - movie_ticket.time.start_movie_ticket.type.screening.accept: Yes, they have a _type.screening_ at _time.start_.   <!-- predicted: general: Bummer. It is not playing at that theater. -->
* Thats perfect! Can we get assigned seats?
    - movie_ticket.num.tickets: Unfortunately there are no _num.tickets_ seats together where we can assign.   <!-- predicted: general: A lady friend. -->
* Oh, so you think we can get _num.tickets_ seats together once we get there?
    - Yes, I see lots of seats in other sections.
* Okay, well figure out when we get there.
    - movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: Okay so its _num.tickets_ adult tickets for _name.movie_ this _time.start_name.theater_location.theater_.   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Yes, thats fine.
    - movie_ticket.ticket_booking.accept: _ticket_booking.accept_   <!-- predicted: general: And will either of them require wheelchair seating accommodations? -->
* Great, thanks.
    - My pleasure!


## dlg-1d9d233f-e617-44e9-a8df-04b951129615
* Hi! I want to find a movie to watch.
    - Hi! What kind of movie do you like to watch?
* Fantasy movie.
    - Please, name one.
* What about _name.movie_?
    - movie_ticket.name.movie: These are movies about _name.movie_.   <!-- predicted: general: Ah soo a different location? -->
* Id like to watch _name.movie_. Do you have something else?
    - general: These are movies close to your request.   <!-- predicted: pizza_ordering.name.store: Sure !! Yes _name.store_ is available nearby _number_ miles -->
* Well, I changed my mind. I think about _name.movie_ now.
    - movie_ticket.name.movie: This is a list of _name.movie_ movies. Do you want to see any movie now?   <!-- predicted: general: Sounds cool. Okay, so I bought the tix, you can pick them up at the front. -->
* Can you find something like _name.movie_?
    - movie_ticket.name.movie: These are movies close to _name.movie_.   <!-- predicted: general: Ah soo a different location? -->
* I would like to see reviews for _name.movie_.
    - movie_ticket.name.movie: These are _name.movie_ reviews.   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* I would like to see _name.movie_.
    - general: Do you want to watch it now?   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Yes.
    - Do you want to add more movie?
* No, thats it for now.
    - Enjoy your movie. Good night.


## dlg-1da4c2c5-2d37-454b-a451-f345064af40a
* I want to purchase tickets for the movie _name.movie_
    - What theater were you thinking of?
* _name.theater_, _location.theater_
    - movie_ticket.num.tickets: Just _num.tickets_ ticket?   <!-- predicted: general: Okay, I show several theaters close by. Do you have a preference on which one you would like to go to? -->
* No, Im taking a friend, so _num.tickets_
    - Okay, what time were you thinking of?
* Is there anything _time.start_?
    - movie_ticket.name.movie_movie_ticket.name.movie.accept_movie_ticket.time.start: Theres only a showing at _time.start_ and _time.start_ for _name.movie_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* That wont work, maybe Ill see _name.movie_
    - general: Ill see if they have anything at around the time you wanted   <!-- predicted: movie_ticket.name.movie_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.time.start: Okay There is a _time.start_ screening for _name.movie_ at _name.theater_ -->
* ok
    - movie_ticket.name.movie_movie_ticket.name.movie.accept_movie_ticket.time.start: Theres only a showing at _time.start_ and _time.start_ for _name.movie_   <!-- predicted: movie_ticket.name.movie_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.time.start: Okay There is a _time.start_ screening for _name.movie_ at _name.theater_ -->
* Theres no other times for either of those movies
    - general: No, those are the only times   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* Alright, I dont think Im going to see a movie at all tonight then
    - You sure, we can try another one if you want
* No, Im just going to stay in tonight, thank you for your help
    - Youre welcome, let me know if you change your mind
* I will thank you
    - Youre welcome


## dlg-1dabca81-a231-4d09-9dd7-d1dfe7c6f98b
* Hey can ou pick me up a Coffee?
    - Yes, sir where would you like me to go?
* Starbucks.
    - What would you like sir?
* Let me get a _size.drink_.
    - coffee_ordering.size.drink: A _size.drink_ what sir?   <!-- predicted: general: Got it. That was hot, right, not iced? -->
* A _size.drink_ _name.drink_
    - Very well, sir.
* Im not finished yet!
    - Sorry sir, what else can I get for that.
* Make that coffe and _name.drink_
    - Yes sir, anything elses.
* Make sure they put on _preference.accept_.
    - Yes sir.
* I would also like that with an _coffee_ordering.preference_.
    - coffee_ordering.preference_coffee_ordering.preference.accept: _coffee_ordering.preference_preference.accept_ sir, anything else?   <!-- predicted: pizza_ordering.name.pizza.accept_pizza_ordering.preference.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.topping: Okay. So I have a two liter diet Pepsi two _size.pizza_, regular _name.pizza_ with _preference.accept_, baked well done and one with _type.topping_ and the other with _type.topping_ and mushrooms? -->
* A _preference.accept_ as well.
    - You got it sir.
* Would you like somethign for yourself.
    - Why thank you for the offer sir, but I shouldnt.
* Pleases, chap, its on me.
    - Thank you kindly.
* I want you to go to the starbucks on _location.store_
    - Why is that sir?
* The barista at the closer one is a
    - Sir, thats not apporopriate.
* I appologize.
    - Not a problem sir.
* Just go get my coffee will you.
    - general: Absolutley.   <!-- predicted: pizza_ordering.location.store.accept: Let me look at the locations real quick. _location.store_? -->


## dlg-1dac9e14-1f6b-45b7-b695-a76faafa1d50
* Hey Connie.
    - Hi boss. Whats up?
* My car is on the fritz again.
    - What can I do to help?
* Can you make me an appointment to get it in the shop?
    - Sure. Where do you want to take it?
* I always use _name.store_ I think they have a website.
    - I found it. Whats the vehicle information?
* Black _year.vehicle_ _name.vehicle_
    - general: Got it. And whats it doing?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* _reason.appt_.
    - general: Funny noise? Like a clown?   <!-- predicted: auto_repair.time.appt.accept: Oh dear. Let me see there is one at _time.appt_, can you make that? -->
* No, more of a _reason.appt_.
    - general: Is it all the time?   <!-- predicted: auto_repair.date.appt_auto_repair.reason.appt: They said they usually want you to schedule a day ahead but since it is _reason.appt_, they said you can bring it in _date.appt_. -->
* No, just when Im turning a corner.
    - auto_repair.date.appt_auto_repair.time.appt: Got it. How about _date.appt_ at _time.appt_?   <!-- predicted: general: What is the name of it? -->
* Ive got court. What about _date.appt_?
    - They have a _time.appt_ a _time.appt_, and a _time.appt_.
* The _time.appt_ would be great.
    - auto_repair.date.appt.accept_auto_repair.time.appt.accept: Ok. Which number do I use for confirmation of _date.appt_ at _time.appt_.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: They cant get you in until _time.appt_. Is that okay? -->
* _name.customer_ _number_-_number_
    - general: Got it. Be careful!   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->


## dlg-1dad9d1a-9fad-40ac-ae92-31d175871933
* Hi. Could you please schedule an Uber for me?
    - Sure thing. From where to where?
* From _location.from_ going _location.to_.
    - And this is for right now, yes?
* Thats right. Could you tell me the estimated fare on that?
    - general: First, is there any particular type of ride you want?   <!-- predicted: uber_lyft.duration.estimate_uber_lyft.price.estimate.accept_uber_lyft.time.pickup_uber_lyft.type.ride: Ok. I am looking it up now. Ok. There is an suv driver or _type.ride_ available for $_price.estimate_duration.estimate_time.pickup_ -->
* No, just a _type.ride_.
    - uber_lyft.type.ride: Okay. So that would be an _type.ride_. Or you could choose to _type.ride_ for a cheaper price.   <!-- predicted: general: Ok. What type of rides would guys like? -->
* Thats okay. Make it an _type.ride_.
    - uber_lyft.price.estimate_uber_lyft.price.estimate.accept: I got you. Okay. So your estimated fare is _price.estimate_ for a one way trip.   <!-- predicted: general: Very good. The next question is car type. -->
* Okay. Excellent. Is that all?
    - uber_lyft.location.from_uber_lyft.location.from.accept: Just need to confirm your pickup location and youre all set. Thats _location.from_, yes?   <!-- predicted: general: Just let me know what you want to do -->
* Thats correct. Yes.
    - uber_lyft.time.pickup_uber_lyft.time.pickup.accept: Okay, great. And your Uber should be there within _time.pickup_.   <!-- predicted: general: Great. Will there be anything else? -->
* All right. And hey, out of curiosity, how much cheaper would the _type.ride_ be?
    - general: It would be about half the price.   <!-- predicted: uber_lyft.time.pickup: About _time.pickup_ -->
* So _price.estimate_?
    - Around there. Yes.
* Okay. Thanks a lot. Thats all I needed.
    - Youre welcome. Bye bye.


## dlg-1db7578c-ebc6-465b-a661-328a38f72d33
* Hey Susan. Will you order me some coffee for pick up from Starbucks?
    - Definitely, what do you want from Starbucks?
* I want a _name.drink_.
    - coffee_ordering.name.drink: Just a _name.drink_?   <!-- predicted: coffee_ordering.size.drink: Ok. Do want a _size.drink_ or _size.drink_? -->
* No. I think I want _coffee_ordering.preference_
    - Okay. What size did you want?
* Make it a _size.drink_.
    - coffee_ordering.preference_coffee_ordering.preference.accept_coffee_ordering.size.drink: A _size.drink_preference.accept_coffee_ordering.preference_? Late night tonight?   <!-- predicted: general: Got it. That was hot, right, not iced? -->
* Nope. Just driving down South to my parents house.
    - general: Thats right. Are you wanting to pick up your coffee on the way?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* That would be great!
    - Any particular location?
* I think theres on _location.store_. Order it there and send me the address.
    - coffee_ordering.location.store_coffee_ordering.location.store.accept_coffee_ordering.location.store.reject: Is it the _location.store_ or the _location.store_?   <!-- predicted: general: Ok - while Im out in that area is there anything else you need? -->
* _location.store_.
    - Looks like thats about _number_ minutes from you.
* Can you have them have it ready a half an hour from now.
    - I can. Anything else? Food?
* Nope thats all.
    - coffee_ordering.location.store.accept_coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Thats a _size.drink_ _name.drink_ with _preference.accept_ ready in a half an hour at _location.store_. Total is going to be _price_   <!-- predicted: general: Would you like for me to order it now? -->
* Thanks Susan! Youre awesome!
    - action_listen: action_listen   <!-- predicted: general: You can pick up the order in _number_ minutes, but if you are running late the order will be made when you get there so the ice does not melt. -->


## dlg-1db9db81-739a-45a2-b140-75529783de51
* I want to see _name.movie_
    - movie_ticket.name.movie: Ok, I can see where _name.movie_ is play. Do you have a city you would like to see it in?   <!-- predicted: movie_ticket.movie_ticket_movie_ticket.name.movie: _movie_ticket.movie_ticket_name.movie_, where would you like to see it? -->
* _location.theater_name.theater_.
    - movie_ticket.location.theater_movie_ticket.location.theater.accept_movie_ticket.name.movie_movie_ticket.name.theater: _name.movie_location.theater_name.theater_ at _name.theater_ and _name.theater_   <!-- predicted: general: I see. Do you know which theater there you want to go to or do you need recommendations? -->
* _location.theater_name.theater_ more, so I want _num.tickets_ for there. Me and my friends are going to have a girls night.
    - movie_ticket.num.tickets: You need _num.tickets_, is that correct?   <!-- predicted: general: okay may i know the show timing -->
* Yea, thats right.
    - movie_ticket.name.movie: Ok, what time would you like to see _name.movie_?   <!-- predicted: general: And a phone number? -->
* What times is the movie playing? I would like something after _time.start_.
    - movie_ticket.name.movie_movie_ticket.time.start: _name.movie_ is playing at _time.start_, _time.start_, _time.start_ and _time.start_   <!-- predicted: movie_ticket.time.start: Showtimes at _time.start_ ,_time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_, _time.start_. -->
* _time.start_ sounds perfect.
    - movie_ticket.time.start_movie_ticket.time.start.reject: I am unable to get the tickets for _time.start_.   <!-- predicted: general: It’s booked and the tickets have been texted to you. -->
* Ok, thats horrible. Lets try _time.start_.
    - movie_ticket.num.tickets_movie_ticket.time.start: _time.start_ has _num.tickets_ available, would you like for me to get those for you?   <!-- predicted: general: Do you need any accessibility devices tonight? -->
* Yes please!
    - movie_ticket.location.theater.accept_movie_ticket.name.movie_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: I have _num.tickets_ for a _time.start_ viewing of _name.movie_location.theater_name.theater_ for tonight. Does that sound correct?   <!-- predicted: movie_ticket.price.ticket.accept: Your card has been charge _price.ticket_ and the tickets for tonights showing have been sent to your device as a text message. -->
* Yep, that is all correct! Does this have a _type.screening_ showing?
    - movie_ticket.name.movie.accept_movie_ticket.type.screening.reject: I am sorry, _name.movie_ is not available in _type.screening_.   <!-- predicted: restaurant_reservation.time.reservation: I see _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_ and _time.reservation_ as available. -->
* Thats ok. But everything in the ticket purchase is correct.
    - general: Is there anything else to add to this order?   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* No, thats all.
    - general: If all the details are correct, your tickets will be purchase through the app. Any updates to this purchase will be sent to you via text.   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* Ok, thanks!


## dlg-1dcc07b5-61d0-43ec-b844-528feeeb0a26
* Hey, can you order me an _uber_lyft.uber_lyft_?
    - Sure! where are you and where are you trying to go?
* Im at the _location.from_ and I need to get to the _location.to_
    - okay, what type of uber do you want to take?
* _type.ride_
    - uber_lyft.price.estimate_uber_lyft.type.ride_uber_lyft.type.ride.reject: it looks like there are not any _type.ride_ available right now, and that is the _price.estimate_ option.   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* okay what other ubers can I take right now?
    - uber_lyft.type.ride: There is an _type.ride_ and _type.ride_ right now.   <!-- predicted: general: I see -->
* what are prices for those two rides?
    - uber_lyft.price.estimate_uber_lyft.type.ride: the _type.ride_ is priced at _price.estimate_ and the _type.ride_ is _price.estimate_   <!-- predicted: uber_lyft.price.estimate: In order, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_, _price.estimate_ -->
* okay
    - uber_lyft.type.ride: normally the _type.ride_ is for multiple passengers but im not sure if you have a lot of bags from the airport.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* I really dont have that much, but the _type.ride_ is _price.estimate_...
    - uber_lyft.type.ride: Do you want me to send the _type.ride_ then?   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Sorry, the _type.ride_ is the cheapest option so theyre all taken. -->
* yes, that would be great! How much was the _type.ride_ again?
    - uber_lyft.price.estimate.accept: _price.estimate_   <!-- predicted: uber_lyft.time.pickup: The current wait time is _time.pickup_. -->
* yeah thats fine
    - uber_lyft.type.ride.accept: Okay, your _type.ride_ is on its way to pick you up! you should be able to check the status on your phone.   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_. You can check its status on your phone. -->
* great, thank you!
    - of course!


## dlg-1dd9830f-cc62-4afd-a40e-5967628eb56a
* Hi, _reason.appt_
    - Im sorry to hear that, would you like me to schedule an appointment to bring it in?
* Yes, please call _name.store_ and ask for the next available appointment.
    - auto_repair.time.appt_auto_repair.time.appt.accept: They have an opening _time.appt_ or _time.appt_, at _time.appt_.   <!-- predicted: general: Yea, the best part is it comes with a home-made Ranch dressing. -->
* I can get there _time.appt_!
    - general: Fantastic. What is the make, model, and year of the truck?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: It looks have your vehicle seen _time.appt_. You would need to drop it off and allow them to keep it overnight. -->
* It is a _year.vehicle_ _name.vehicle_.
    - auto_repair.reason.appt.accept: _reason.appt_?   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Yes.
    - Your name and number?
* _name.customer_ _number_-_number_-_number_
    - general: Can you spell the last name?   <!-- predicted: auto_repair.name.customer.accept: Okay _name.customer_, the phone number was _number_-_number_-_number_ correct? -->
* _name.customer_
    - auto_repair.name.customer.accept_auto_repair.name.store.accept: Thank you, _name.customer_. I have you confirmed for an immediate appointment at _name.store_.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* Thank you so much!
    - general: Youre welcome. Is there anything else?   <!-- predicted: auto_repair.date.appt.accept_auto_repair.name.customer.accept_auto_repair.time.appt: Drive safetly, appointment is at _time.appt_ _date.appt_, for _name.customer_, number _number_-_number_-_number_- fee will be _price_ for initial inspection -->
* Not right now.
    - Ok, have a good day
* Thank you, you too
    - general: Good bye   <!-- predicted: action_listen: action_listen -->
* Bye


## dlg-1ae783cf-df06-4994-ab32-fba740de3517
* I want to order a pizza from _name.store_ for pickup.
    - Ok. What kind of pizza would you like?
* I would like a _size.pizza_ _name.pizza_.
    - What kind of toppings?
* Id like _type.topping_, _type.topping_, _type.topping_ on it.
    - pizza_ordering.name.pizza_pizza_ordering.size.pizza_pizza_ordering.type.topping: Ok. You can get a _size.pizza_ _name.pizza_ this month with the same toppings you want and _type.topping_ for the same price.   <!-- predicted: pizza_ordering.preference_pizza_ordering.preference.reject: _pizza_ordering.preference_preference.reject_? -->
* Could I get _type.topping_ instead of _type.topping_ on the _name.pizza_?
    - general: Yes, I can make that substitution for you.   <!-- predicted: pizza_ordering.size.pizza_pizza_ordering.size.pizza.reject: Yes, so you want a _size.pizza_ instead of _size.pizza_? -->
* That sounds good.
    - pizza_ordering.type.crust: Do you want _type.crust_, _type.crust_, or _type.crust_?   <!-- predicted: pizza_ordering.size.pizza.accept_pizza_ordering.type.topping.accept: Okay, so thatt a _size.pizza_., _type.topping_, _type.topping_ and _type.topping_ pie. -->
* _type.crust_. If it is same price as the others.
    - It is.
* Great, make it a _type.crust_ then.
    - Would you like any sides, dessert, or drinks.
* No, I think that is enough calories for me.
    - general: Fair enough, the total will be _price_ including tax.   <!-- predicted: pizza_ordering.size.pizza: Oh no! I was just told they no longer have plain dough to make a _size.pizza_ pizza. -->
* Ok. Use the same payment information you have on record.
    - pizza_ordering.name.pizza.accept_pizza_ordering.size.pizza.accept_pizza_ordering.type.crust.accept_pizza_ordering.type.topping_pizza_ordering.type.topping.accept: Sure. To confirm, your order for pickup is for one _size.pizza_ _type.crust_ _name.pizza_ with _type.topping_ instead of _type.topping_.   <!-- predicted: general: Here Ill turn up the volume so you can hear yourself. Ask something. -->
* Yup thats it. Thank you.
    - Your pizza order is complete and will be ready for pickup in about _number_ minutes.


## dlg-1dd9f708-49a6-4481-94af-4a98d2dae03a
* Hey, I want to take my friend out to the movie theater to watch _name.movie_. May you help me find the movie.
    - movie_ticket.location.theater: Hie. Sure I would be happy to help. Are you going to watch it in _location.theater_?   <!-- predicted: general: Hi! What kind of movie do you like to watch? -->
* Yes, either _location.theater_ or _location.theater_.
    - Okay, let me check.
* Thank you.
    - movie_ticket.name.movie.accept: Unfortunately the movie you want to see will start showing on the _number_ of February but I have an alternative movie for you called _name.movie_.   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.theater.accept: _name.theater_ is located _location.theater_. -->
* Oh yes, I saw the trailers before. It is in the same genre as _name.movie_. Sure, we will watch it.
    - movie_ticket.num.tickets: Okay, great. Is it just the _num.tickets_ of you?   <!-- predicted: general: Ok, but what about time to eat lunch? -->
* Yes just us _num.tickets_.
    - movie_ticket.location.theater.accept_movie_ticket.name.theater.accept_movie_ticket.time.start: _name.theater_ in _location.theater_ is showing it at _time.start_ and _time.start_.   <!-- predicted: general: Okay, I will use the discover card. Should I finalize the ride? -->
* _time.start_ will be too late for us, can you do _time.start_?
    - Sure, and remember they serve food and beverages so if you like, you can grab something to eat there.
* Oh, thats a great idea, thank you for that suggestion.
    - general: I will email you their menu so that you can see if the food and beverages they offer tickle your fancy.   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* That sounds awesome.
    - general: Do you want front row seats, back row seats, or the mid-section?   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* Mid-section is fine.
    - movie_ticket.num.tickets_movie_ticket.price.ticket.accept: Okay, it would be _price.ticket_ for _num.tickets_. Should I go ahead and confirm the booking?   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_ as a text message. -->
* Yes please, thank you.
    - movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email.   <!-- predicted: movie_ticket.ticket_booking.accept: _ticket_booking.accept_ as a text message. -->
* Thank you so much, I appreciate the help.
    - Anytime, have a great evening. Good-bye.
* Bye.


## dlg-1de27694-39e6-4cc8-b282-9a3cb4ccbf1d
* hi alexa i think id like something from peets today
    - OKAY SIR WHAT WERE YOU THINKING FOR TODAY?
* i was craving a _size.drink_ beverage but you know im lactose intolerant
    - coffee_ordering.type.milk: they do have different options such as _type.milk_   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.accept: I could ask them to _preference.accept_. Or a particular roast, how do you feel about their blonde roast? -->
* oh great! what do you suggest
    - general: they hace some seasonal drinks right now   <!-- predicted: coffee_ordering.type.milk: You can get _type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_, or _type.milk_. -->
* like which ones?
    - coffee_ordering.name.drink: they have _name.drink_, _name.drink_, and a _name.drink_   <!-- predicted: general: I personally would recommend Lyft over Uber. -->
* i think i would go with the _name.drink_ one
    - general: okay and what milk did you want?   <!-- predicted: pizza_ordering.type.topping.reject: Okay, I tried to order them but they are currently out of _type.topping_, so they cant make either. -->
* ill go with _type.milk_ with that. make it a _size.drink_
    - coffee_ordering.name.drink_coffee_ordering.size.drink_coffee_ordering.type.milk: okay so to confirm i have a _size.drink_ _name.drink_ with _type.milk_   <!-- predicted: coffee_ordering.name.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference_coffee_ordering.size.drink_coffee_ordering.type.milk: So thats _num.drink_ _size.drink_ _name.drink_, with _type.milk_, and _coffee_ordering.preference_ on top. -->
* yes exactly like that
    - coffee_ordering.type.milk_coffee_ordering.type.milk.reject: okay there are telling me they do not have _type.milk_, would you like _type.milk_ instead?   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* i guess that will do yes
    - coffee_ordering.name.drink.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: okay so a _size.drink_ _name.drink_ with _type.milk_   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.preference.reject_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Okay! So thats a _size.drink_ _name.drink_ made with _type.milk_, with _preference.reject_. Right? -->
* yes exactly
    - general: okay i ordered it your order will arrive shortly   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.num.drink_coffee_ordering.num.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept: Okay. Your order for _num.drink_ _size.drink_ _name.drink_ with _preference.accept_ and _preference.accept_, and _num.drink_ venti _name.drink_ will be ready in _number_ minutes. -->
* thank you so much i appreciate it
    - no problem, your receipt will be texted to you okay
* yes of course
    - action_listen: action_listen   <!-- predicted: general: Your appointment has been made. Please be advised that there is a _price_ inspection fee. -->


## dlg-1df021cf-857e-40e1-bdc4-dc5e073b2219
* Hi, I am interested in setting an appointment to get my car looked at.
    - Do you have a preference regarding where you want to go?
* Yes, _name.store_
    - general: Great, I have that.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: _time.appt_date.appt_ _ at_time.appt_time.appt_ -->
* I need to schedule something _date.appt_ _time.appt_, probably first thing.
    - auto_repair.time.appt: You can drop it off in the _time.appt_.   <!-- predicted: general: Im sorry to hear that, would you like me to schedule an appointment to bring it in? -->
* Ok.
    - auto_repair.time.appt_auto_repair.time.appt.accept: They have you booked at _time.appt_. but you can leave it and the keys any time before.   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* Ok.. can I book a loaner car from them for the time the car is there?
    - general: You can, they offer that service.   <!-- predicted: auto_repair.time.appt: I can squeeze you in a _time.appt_. -->
* good.
    - general: What can I tell them you want done?   <!-- predicted: auto_repair.time.appt: Upon checking, it looks like _time.appt_ is available. Is _number_ a.m. okay? -->
* _reason.appt_.
    - which vehicle do you want them to look at tomorrow?
* The _year.vehicle_name.vehicle_time.appt_
    - general: Got it.   <!-- predicted: auto_repair.date.appt_auto_repair.time.appt: Alright, Ill put you in for _time.appt_ _date.appt_. -->
* I want them to mainly look at the _reason.appt_, but if they can see any other reason for the pulling to the right when braking it would be good.
    - general: Ok, Ill note that.   <!-- predicted: auto_repair.time.appt: That time is not available, there is a time _time.appt_ if that is ok. -->
* what is their estimate cost?
    - They charge _number_ which can apply to repairs you might have done.
* Good, Ill be there early _date.appt_..what time is someone there?
    - auto_repair.time.appt: Someone is at the desk at _time.appt_.   <!-- predicted: general: He is coming in a white honda civic. -->
* Thanks again.
    - thank you good bye.


## dlg-1df16674-44bf-4c0b-964f-6eb09cbe69b8
* Please order me an iced coffee drink.
    - From which store do you want me to get your coffee?
* Starbucks.
    - Sounds good. What kind of drink do you like?
* Get me _name.drink_.
    - general: What size?   <!-- predicted: coffee_ordering.type.milk: Okay. Do you want _type.milk_? -->
* _size.drink_.
    - general: Milk?   <!-- predicted: coffee_ordering.preference.reject: Darn! It looks like they are out of the _preference.reject_ used in that drink. -->
* _type.milk_
    - coffee_ordering.preference: With _coffee_ordering.preference_?   <!-- predicted: general: Perfect, whats the best pick up location? -->
* Of course.
    - coffee_ordering.name.drink_coffee_ordering.preference_coffee_ordering.size.drink_coffee_ordering.type.milk: Just to confirm --- _size.drink_ _name.drink_ with _type.milk_ and _coffee_ordering.preference_.   <!-- predicted: general: Any foam? -->
* Yes
    - coffee_ordering.type.milk.reject: Unfortunately, they dont ran out of _type.milk_. Would you like to try a different kind of milk?   <!-- predicted: coffee_ordering.preference_coffee_ordering.preference.reject: _coffee_ordering.preference_preference.reject_ available. Would you like to remove it or choose something else? -->
* What else do they have?
    - coffee_ordering.type.milk: _type.milk_, _type.milk_, _type.milk_, _type.milk_, _type.milk_.   <!-- predicted: coffee_ordering.preference: Starbucks offers _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_ _coffee_ordering.preference_. _coffee_ordering.preference_, _coffee_ordering.preference_, and hazelnut. They have _coffee_ordering.preference_ and _coffee_ordering.preference_. -->
* Let me try _type.milk_.
    - coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Great, will order _size.drink_ _name.drink_ with _type.milk_ and _preference.accept_.   <!-- predicted: general: All with the same sizes? -->
* Thanks.
    - coffee_ordering.location.store.accept: Youre welcome. Your order has already been paid for and is ready for pick up in _number_ minutes at the Starbucks _location.store_. Receipt will arrive via text message on your phone.   <!-- predicted: coffee_ordering.coffee_order.accept: _coffee_order.accept_, the drink should be ready for pick up soon, the receipt will be sent to your phone -->
* great.thanks.
    - Youre welcome.


## dlg-1df37e89-6503-45ab-9a7b-5982e3c52ad7
* I need to get tickets to go see the movie _name.movie_
    - general: Which city do you want see it in?   <!-- predicted: movie_ticket.name.movie: Ok, I can see where _name.movie_ is play. Do you have a city you would like to see it in? -->
* _location.theater_
    - Ok which theater?
* Its playing at the _name.theater_
    - all right what time?
* the _time.start_ showing.
    - And how many tickets do you need?
* I am taking a friend so _num.tickets_ will do.
    - Do you want to pay with your credit card or put it on your account.
* on my account please, They already have all my information.
    - Would you like me to pre-order any snacks?
* Oh, yes lets do one large popcorn and _number_ large Cokes.
    - Anything else?
* yea how about something sweet like MMs,
    - Plain or Peanut?
* Do they offer Peanut butter?
    - yes they do, you would prefer those?
* yes I would
    - movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: Ok so that is _num.tickets_ to see _name.movie_ at _time.start_ at the _name.theater_ in _location.theater_.   <!-- predicted: coffee_ordering.name.drink.accept_coffee_ordering.preference.accept_coffee_ordering.size.drink.accept_coffee_ordering.type.milk.accept: Okay. I have one Starbucks _size.drink_preference.accept_name.drink_ with _type.milk_, _preference.accept_. -->
* correct.
    - For your snacks it was a Large Popcorn, and _number_ large Cokes, and Peanut butter Mms.
* Yes Perfect.
    - movie_ticket.price.ticket.accept: Ok the total that is going on your movie account is _price.ticket_ even.   <!-- predicted: general: And its charged to your Peets account. -->
* Great thanks.
    - Your tickets will be sent to your Mobile Device as a text message.
* Ok , Thank you.
    - action_listen: action_listen   <!-- predicted: general: Enjoy your lunch! -->


## dlg-1df7fc9b-69df-4abb-984d-0d3656f5d59c
* Im looking for a solid Chinese restaurant
    - general: Great, what is your location?   <!-- predicted: restaurant_reservation.name.restaurant: _name.restaurant_ really requires reservations while _name.restaurant_ doesnt. -->
* Im in _location.restaurant_
    - How many people are in your party?
* _num.guests_
    - general: What time would you like to eat?   <!-- predicted: restaurant_reservation.time.reservation: Okay great we have the option for a bottle of wine or roses at longhorns and availability at _time.reservation_ and a _price_ charge for wine or roses. -->
* _time.reservation_ should be fine
    - restaurant_reservation.name.restaurant: Theres _name.restaurant_, _name.restaurant_, and _name.restaurant_ in the area   <!-- predicted: restaurant_reservation.time.reservation: I see _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_, _time.reservation_ and _time.reservation_ as available. -->
* Lets go with _name.restaurant_
    - restaurant_reservation.name.restaurant.reject: Unfortunately, _name.restaurant_ is booked at that time   <!-- predicted: general: Okay, how many people will be dining? -->
* How about _name.restaurant_?
    - restaurant_reservation.name.restaurant.reject: _name.restaurant_ doesnt have any tables available to accommodate your party   <!-- predicted: general: What kind of table would you prefer? -->
* Ok, how about _name.restaurant_?
    - general: Yes, they have a table available at the time with the amount of people in your party   <!-- predicted: restaurant_reservation.type.seating: Do you prefer _type.seating_ -->
* Lets book it
    - restaurant_reservation.name.restaurant.accept_restaurant_reservation.num.guests.accept_restaurant_reservation.time.reservation.accept: Sounds good. To confirm, _num.guests_ people for _time.reservation_m at _name.restaurant_?   <!-- predicted: general: Alright, youre all set. Enjoy your dinner! -->
* Yes
    - restaurant_reservation.reservation.accept: _reservation.accept_   <!-- predicted: general: Alright, youre all set. Enjoy your dinner! -->
* Thanks
    - No problem, enjoy!


## dlg-1e08d45a-384b-4ba2-96e0-18cd8dfdb6f1
* Hi Marcy, how are you?
    - Doing great! Whats up Jack.
* I need you to schedule an auto repair appointment for me, Im busy driving at the moment but this just came up..
    - Okay sure, I will take care of that for you. Let me get to my PC real quick-
* Thank you. Id like you to book the appointment with _name.store_ and please let me know when they have an opening.
    - Can do! But first well need to fill out some information on the website.
* Thanks Marcy, what do you need?
    - general: I will need the make, model, and the year first please.   <!-- predicted: auto_repair.name.customer: No problem _name.customer_, I also went ahead and left the following info for contact, _name.customer_ at _number_-_number_-_number_ -->
* Got it. Its a _year.vehicle_ _name.vehicle_.
    - I have successfully submitted the information you provided and now looking for the nearest location to you.
* Thank you for your help, do you need anything else from me?
    - auto_repair.name.customer: No problem! Yes, Ill need to enter your full name, _name.customer_ and list a telephone number for you. Do you want me to give them your office or mobile number?   <!-- predicted: general: No problem! Hope it all goes well. -->
* You can give them my mobile its _number_-_number_-_number_
    - Thank you Jack. Whats the reason for the appointment?
* _reason.appt_..
    - I see, I see. Ok. With that Ill start looking for availabilities on the soonest we can get you in. What time of day do you prefer?
* Id like it as soon as humanly possible, Marcy. I was thinking of sometime _time.appt_ as its _time.appt_no_time.appt_
    - auto_repair.date.appt.reject_auto_repair.time.appt: _date.appt_time.appt_ work?   <!-- predicted: general: oh no, will we be able to get it to the shop without a tow? -->
* Ugh. Not really, but I will take it I suppose.
    - auto_repair.location.store.accept_auto_repair.name.customer_auto_repair.time.appt_auto_repair.time.appt.accept: Oh! Great news _name.customer_! The _time.appt_ spot just opened up and I just put you down at the _location.store_. Will that be alright?   <!-- predicted: general: Payment info is stored in the accounts, correct? -->
* Yes! Thank you so much, Marcy. A huge headache is now gone.
    - Youre very welcome! Is there anything else you needed?
* No, thanks Marcy. Ill be bringing you lunch _date.appt_ after I get out of the auto _appointment.accept_. Take care!
    - auto_repair.date.appt.accept: See you _date.appt_, Jack. Goodbye.   <!-- predicted: general: No problem! Hope it all goes well. -->
* Bye.
    - action_listen: action_listen   <!-- predicted: general: No problem, have a safe trip Kevin. -->


## dlg-1e0ffc71-c948-4cb3-bd06-49abb9f84dd0
* I need you to call me an _type.ride_.
    - uber_lyft.type.ride: Where do you need the _type.ride_ to pick you up?   <!-- predicted: general: I can certainly help you with that. What sort of car are you interested in? -->
* _location.from_
    - What is your destination?
* _location.to_
    - uber_lyft.type.ride: Which fares would you like to hear? _type.ride_, _type.ride_, or _type.ride_?   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* _type.ride_
    - uber_lyft.location.from_uber_lyft.location.to.accept_uber_lyft.price.estimate.accept_uber_lyft.type.ride: Ok, the estimated _type.ride_ fare from _location.from_ to _location.to_ is _price.estimate_. Would you like me to call an UberX for you?   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* Yes.
    - uber_lyft.type.ride: Ok, please hold while I call the _type.ride_ for you.   <!-- predicted: general: Which Uber service do you prefer? -->
* Thank you.
    - uber_lyft.type.ride: _type.ride_ is on the way.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Thank you.
    - uber_lyft.location.from.accept_uber_lyft.time.pickup_uber_lyft.type.ride: _type.ride_ should be at _location.from_ in about _time.pickup_   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Thank you.
    - uber_lyft.time.pickup_uber_lyft.time.pickup.accept_uber_lyft.type.ride: Your _type.ride_ car is arriving in about _time.pickup_.   <!-- predicted: general: And hell be driving a black Cadillac Escalade. You can check his progress on your phone via the Uber app. -->
* Thank you.
    - uber_lyft.type.ride.accept: Your _type.ride_ has arrived.   <!-- predicted: auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_ will cost around _price_ _reason.appt_ costs _price_ -->
* Thank you.
    - general: Is there anything else you need?   <!-- predicted: auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_ will cost around _price_ _reason.appt_ costs _price_ -->
* Thats it. Thank you.
    - uber_lyft.duration.estimate.accept_uber_lyft.time.dropoff.accept: _time.dropoff_duration.estimate_. Have a good trip.   <!-- predicted: auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_ will cost around _price_ _reason.appt_ costs _price_ -->


## dlg-1e1f6e1b-59ea-4791-b548-6b560b56d43f
* Hello Justin
    - Hi how are you?
* Not so good my _reason.appt_.
    - general: Oh thats not good.   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* Yeah a _reason.appt_.
    - general: Total bummer.   <!-- predicted: uber_lyft.type.ride_uber_lyft.type.ride.reject: Ok. so I found out that unfortunately, the _type.ride_ cars are not present in your area, but the _type.ride_ ones are. They are spacious but cost a bit more. -->
* Well can you get an appointment scheduled for the car to be seen ?
    - Sure no problem
* Something that is not so pricey.
    - auto_repair.name.store: Okay how about _name.store_?   <!-- predicted: general: CHECKING..... -->
* No too much.
    - auto_repair.location.store.accept_auto_repair.name.store_auto_repair.name.store.accept: Okay we have _name.store_ _location.store_.   <!-- predicted: general: Any side sauces? -->
* Okay how much?
    - general: Well whats exactly wrong with the car   <!-- predicted: movie_ticket.time.duration.accept: I guess _time.duration_. -->
* _reason.appt_.
    - Oh I see.
* How much will that be.
    - According to them to just look at it will be _price_ and to fix dependa on the issue
* Okay well just take it down for me
    - No problem at all
* What time will you be here
    - auto_repair.date.appt_auto_repair.time.appt_auto_repair.time.appt.accept: _time.appt_date.appt_.   <!-- predicted: general: Checking now, All options have the same travel time. -->
* Okay sounds good
    - general: Well see you then   <!-- predicted: auto_repair.reason.appt_auto_repair.reason.appt.accept: _reason.appt_ -->
* Oh can you make sure the _reason.appt_d as well
    - No problem
* Thanks for helping me with this issue i dont know what i would do without you.
    - Your welcome thats what im here for
* Ok take care
    - general: Bye see you tomorrow   <!-- predicted: auto_repair.name.store.accept_auto_repair.name.vehicle.accept_auto_repair.reason.appt.accept_auto_repair.time.appt.accept: _time.appt_ going into _name.store_ll be taking your _name.vehicle_reason.appt_ -->


## dlg-1e234b96-ddc9-4ab7-a4f0-2beec220cd80
* Hey assistant..Can you check whether tickets are available for the movie _name.movie_ in nearby theatres here in _location.theater_
    - Sure. I can check that information for you
* Thank you
    - movie_ticket.name.theater_movie_ticket.time.start: I see that there is a show at _time.start_ today at _name.theater_, approximately _number_ miles from your place. Do you want me to reserve the tickets?   <!-- predicted: general: Where do you want to watch the movies? -->
* Sure. Book _num.tickets_ for me for the _time.start_ show
    - movie_ticket.num.tickets_movie_ticket.time.start: Sure. I see that only _num.tickets_ is available for _time.start_ show   <!-- predicted: general: Do you need any accessibility devices tonight? -->
* Is it? Are there any options?
    - I see that tickets are available for _time.start_ show
* Ok..That will be very late.I think in that case, i may need to finish my dinner and then go for the movie.
    - Sure.
* Let me check with my friend if _time.start_ show is fine for him
    - Ok. Let me know then
* Assistant. Go ahead and book _num.tickets_ for _time.start_ show for _name.movie_
    - general: Ok. Which seat do you prefer?   <!-- predicted: movie_ticket.location.theater.accept_movie_ticket.name.movie.accept_movie_ticket.name.theater_movie_ticket.name.theater.accept_movie_ticket.num.tickets.accept_movie_ticket.time.start.accept: _name.theater_num.tickets_name.theater_time.start_name.movie_location.theater_ -->
* I prefer the lounge seat.
    - general: Do you want to have food delivery service choosen?   <!-- predicted: restaurant_reservation.location.restaurant.accept: _location.restaurant_ Ive also included there telephone number for your convenience. -->
* YEs. Order just popcorn or frenchfires. _number_ coke as well
    - Ok.I see that the card information is already setup
* Yes..Let me know the details after the booking is donw
    - movie_ticket.time.start.accept: I have reserved the tickets for _time.start_ show, also also food will be delivered at he break time at your place   <!-- predicted: uber_lyft.ride_booking.accept_uber_lyft.time.pickup.accept_uber_lyft.type.ride.accept: Sure. _type.ride_ has been _ride_booking.accept_ and should be here in a little over _time.pickup_. -->
* Thaank you so much
    - general: Tickets details will be sent to your mailphone.   <!-- predicted: movie_ticket.num.tickets.accept_movie_ticket.ticket_booking.accept: I have just _ticket_booking.accept_ _num.tickets_ for _num.tickets_ have also texted you the confirmation text message and email. -->
* Yes. I received the same
    - Thank you for confirmation. Is there anything i can help you with
* No. I am good. Thank you
    - Ok. Enjoy rest of your evening
* Thank you. Bye
    - general: Bye   <!-- predicted: action_listen: action_listen -->


## dlg-1b0252bf-b03d-4afb-961d-d92a859ce344
* Jane I need you to order _num.people_ an uber.
    - Okay. Where are you now and where will you be going?
* Im at _location.from_ and Im headed to _location.to_.
    - Which _location.to_ are you headed to?
* Im headed to the _location.to_.
    - uber_lyft.location.to_uber_lyft.location.to.accept: _location.to_ got it.   <!-- predicted: uber_lyft.location.to: Thats _location.to_? -->
* Yes _location.to_.
    - uber_lyft.num.people: Is _num.people_ or more than you riding?   <!-- predicted: general: What type of ride to you want? Limo, Cab, or Uber? -->
* Its an uber _num.people_.
    - What size uber do you want then?
* It doesnt really matter.
    - uber_lyft.price.estimate_uber_lyft.price.estimate.accept_uber_lyft.type.ride: _type.ride_ is _price.estimate_ and _type.ride_ is _price.estimate_.   <!-- predicted: general: Oh, I know its so frustrating. -->
* Hmm just go with the _type.ride_.
    - general: When do you want me to order it?   <!-- predicted: uber_lyft.time.pickup: the wait is _time.pickup_ -->
* I am outside now ready for a ride.
    - Okay. I am ordering the ride now.
* Okay that sounds great.
    - general: The Uber is on the way.   <!-- predicted: uber_lyft.ride_booking.accept: _ride_booking.accept_ I’ll be on your phone -->
* Thank you for your help.
    - You are welcome. You can check the status on your phone.



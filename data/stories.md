## chitchat
* canthelp
    - utter_canthelp

## greet + canthelp
* greet
    - action_greet_user
* canthelp
    - utter_canthelp

## greet + newsletter + canthelp + continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu

## greet + newsletter + canthelp + don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just sales + continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales + don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* canthelp
    - utter_canthelp
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat

## deny ask_whatspossible
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp

## more chitchat
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat

## ask_whatspossible
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat

## ask_whatspossible more
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## just newsletter + confirm
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, continue, + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, don't continue, + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter, continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback

## just sales
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback

## just sales, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt OR ask_whatspossible
    - action_chitchat
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_direct_to_step2

## new to rasa/bots, explain core and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain core and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_direct_to_step2

## new to rasa/bots, explain nlu and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_also_explain_core
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain nlu and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_direct_to_step2

## new to rasa/bots, don't explain and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_explain_nlucore
* deny
    - utter_direct_to_step2

## new to rasa/bots, don't explain and try out stack
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_direct_to_step2
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_direct_to_step2

## not new to rasa + not interested in products
* greet
    - action_greet_user
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + nlu + nothing special
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_ask_for_nlu_specifics
* deny
    - utter_quickstart_nlu_only
    - utter_anything_else

## not new to rasa + nlu + unknown topic
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part
    - utter_dont_know_nlu_part
    - utter_search_bar
    - utter_anything_else

## not new to rasa + nlu + intent + no recommendation
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## how to get started without privacy policy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_whatisrasa OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR ask_howbuilt
    - action_chitchat
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## story number 1
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback

## story number 2
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* out_of_scope
    - utter_thumbsup
    - utter_anything_else

## story number 4
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else
* ask_whatspossible
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## story number 5
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## story number 6
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## story number 7
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback

## story number 8
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## story number 9
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* deny
    - utter_nohelp

## story number 11, continue
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## story number 11, don't continue
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## story number 12
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

## story number 12, continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

## story number 12, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

## story number 14
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_weather
    - action_chitchat

## story number 15
* greet
    - action_greet_user
* ask_weather
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## story number 17
* greet
    - action_greet_user
* deny
    - utter_nohelp
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* ask_whoisit
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat

## story number 18
* greet
    - action_greet_user
* ask_weather
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* deny
    - utter_nohelp
* enter_data
    - utter_not_sure
    - utter_possibilities
* deny
    - utter_nohelp
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities
* enter_data{"number":5}
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 00e7815f79e4413abb0dfb4b392f1099 on November 15th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## story from linda
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with dfbb633d10854f97b880a2496d632f0d on November 16th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with alan on November 16th 2018
* nlu_info{"nlu_part":"duckling"}
    - slot{"nlu_part":"duckling"}
    - utter_duckling_info
    - utter_anything_else
* affirm
    - utter_what_help

## Story from conversation with alan on November 16th 2018 2
* nlu_info{"nlu_part":"intent classification"}
    - slot{"nlu_part":"intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* affirm
    - utter_what_language
* enter_data{"language":"spanish"}
    - slot{"language":"spanish"}
    - action_store_bot_language
    - slot{"can_use_spacy":true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with linda on November 15th 2018
* greet
    - action_greet_user
* ask_whatisrasa
    - action_chitchat
* ask_whatisrasa
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with 477ddbe73e374eedb07104c5d9f42c31 on November 16th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* greet
    - action_greet_user

## Story from conversation with 4986d88ccb784dc19dc5a553a8e07890 on November 19th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_direct_to_step2

## Story from conversation with 7830abb04e1c49809d89b0d420443928 on November 19th 2018
* greet
    - action_greet_user
* ask_whoisit
    - action_chitchat
* out_of_scope
    - utter_out_of_scope
* ask_whatspossible
    - action_chitchat
* how_to_get_started{"product":"nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with 29d264d8ce574a11bde572f0e79b73f3 on November 19th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_isbot
    - action_chitchat
* affirm
    - utter_thumbsup

## Story from conversation with 6fd65c93e374489f9c8d76697ab9c493 on November 19th 2018
* greet
    - action_greet_user
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* affirm
    - utter_thumbsup

## Story from conversation with 35d1ecc91c364cbf8a6edf006e5d8c9a on November 19th 2018

* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else
* affirm
    - utter_thumbsup

## Story from conversation with 4c274f8d470e4b77adbfefe7cda7cad7 on October 27th 2018

* greet
    - action_greet_user
* greet
    - action_greet_user
* affirm
    - utter_thumbsup
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with d041ba4b0a89479e9bb6a5007f2cdc87 on November 15th 2018
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else
* ask_weather
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with dominik on November 19th 2018
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch{"current_api":"luis"}
    - slot{"current_api":"luis"}
    - utter_switch_luis
    - utter_anything_else
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_explain_core
    - utter_anything_else
* how_to_get_started{"product":"nlu"}
    - slot{"product":"nlu"}
    - utter_explain_nlu
    - utter_anything_else

## Story from conversation with dominik
* nlu_info{"nlu_part":"intent classification"}
    - slot{"nlu_part":"intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* affirm
    - utter_what_language
* enter_data{"language":"spanish"}
    - slot{"language":"spanish"}
    - action_store_bot_language
    - slot{"can_use_spacy":true}
    - utter_spacy_or_tensorflow
    - utter_anything_else
* enter_data{"language":"french"}
    - slot{"language":"spanish"}
    - action_store_bot_language
    - slot{"can_use_spacy":true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## Story from conversation with dominik on November 19th 2018
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding":false}
    - utter_ask_which_product
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_core_tutorial
    - utter_anything_else
* how_to_get_started{"product":"nlu"}
    - slot{"product":"nlu"}
    - utter_ask_for_nlu_specifics

## Story from conversation with 201bb55841154f858f524a485f8816c3 on November 18th 2018

* greet
    - action_greet_user
* how_to_get_started{"product":"nlu"}
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with cd483ab3456d47dfb40bd1f51043fb54 on November 18th 2018

* greet
    - action_greet_user
* greet
    - action_greet_user
* how_to_get_started{"product":"core"}
    - utter_getstarted
    - utter_first_bot_with_rasa

## Story from conversation with cfa8bb9deaf0427498c662745431a282 on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_whatisrasa
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with cdd14d763a664a5b95e998ce165bd86f on December 16th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* ask_faq_languages
    - action_faqs
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 67a8696eb5894b25a800b6cbd7a695bb on December 15th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_howdoing
    - action_chitchat
* ask_whoisit
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* ask_faq_languages
    - action_faqs
* enter_data
    - utter_not_sure
    - utter_possibilities
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 030829eb30ed4339985d7e71737f6c2d on January 1st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with e977c395a2404bef8ba7f0c3b7e65970 on January 8th 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - slot{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## Story from conversation with 602ddccbe2de4f46822e06e2781cf02d on January 8th 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* affirm
    - utter_thumbsup
* affirm
    - utter_thumbsup

## Story from conversation with 03727bb9d4cb4f64afdc383818739680 on January 17th 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - action_greet_user
* how_to_get_started{"user_type":"new"}
    - action_set_onboarding
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product":"stack"}
    - slot{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* get_started_step2
    - action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step":"3"}
* install_rasa
    - utter_ask_python_installed

## Story from conversation with 4cdb0b3c6f6c4b3694fcb311ae72743b on January 21st 2019

* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu
    - action_faqs
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu

## Story from conversation with 4b7ecc2cab6e42c5b1fedb8ab4056866 on December 29th 2018
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
* ask_whoami
    - action_chitchat
* ask_languagesbot
    - action_chitchat
* ask_howold
    - action_chitchat
* out_of_scope{"number":42}
    - utter_out_of_scope
    - utter_possibilities
* out_of_scope{"number":42}
    - utter_out_of_scope
    - utter_possibilities

## Story from conversation with af5a6b3c39d04c6db2b682960e63f01c on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* react_positive
    - utter_react_positive
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## Story from conversation with af5a6b3c39d04c6db2b682960e63f01c on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - action_greet_user
* ask_howdoing
    - action_chitchat
* ask_whatspossible
    - action_chitchat
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* react_positive
    - utter_react_positive
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## Story from conversation with 53d4ca53494d4469b7d94aca2f7b3fec on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* enter_data
    - utter_not_sure
    - utter_possibilities
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_differencecorenlu{"product":"nlu"}
    - slot{"product":"nlu"}
    - action_faqs
    - utter_explain_nlucore
* how_to_get_started{"product":"core"}
    - utter_explain_core
    - utter_also_explain_nlu

## Story from conversation with 4a4e903fc43940db9ccdb9153dfdadcb on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager":"pip"}
    - slot{"package_manager":"pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* enter_data
    - action_store_problem_description
    - slot{"problem_description":"tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.16.0 which is incompatible."}
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4
* enter_data
    - utter_not_sure
    - utter_possibilities

## Story from conversation with 5f3a2ea92d184a9f96df7240e4f7e2d9 on January 21st 2019
* get_started_step1
    - action_greet_user
    - slot{"shown_privacy":true}
    - slot{"step":"1"}
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## Story from conversation with ced8c1eb9a8d485f88a02d931b2879bd on January 16th 2019
* get_started_step3
    - action_greet_user
    - slot{"shown_privacy":true}
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else
* affirm
    - utter_what_help
* ask_whatspossible
    - action_chitchat
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding":true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## prompt for getting started
* get_started_step2
    - action_greet_user
    - utter_direct_step3

## next step prompt
* next_step
    - action_next_step

## faqs
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs

## more faqs
* greet
    - action_greet_user
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs

## just newsletter
* greet
    - action_greet_user
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, don't continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR  ask_faq_channels OR  ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just sales
* greet
    - action_greet_user
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback

## just sales, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + not migrating
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain stack and try it out
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain core and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain core and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, explain nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_also_explain_core
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain nlu and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_direct_to_step2
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_direct_to_step2

## new to rasa/bots, don't explain and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_explain_nlucore
* deny
    - utter_direct_to_step2

## new to rasa/bots, don't explain and direct to step2
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_direct_to_step2
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_direct_to_step2

## not new to rasa + not interested in products
* greet
    - action_greet_user
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + not interested in products
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + nlu + nothing special
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_for_nlu_specifics
* deny
    - utter_quickstart_nlu_only
    - utter_anything_else

## not new to rasa + nlu + unknown topic
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part
    - utter_dont_know_nlu_part
    - utter_search_bar
    - utter_anything_else

## not new to rasa + nlu + intent + no recommendation
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* greet
    - action_greet_user
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## how to get started without privacy policy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_faqs
    - utter_first_bot_with_rasa
* affirm
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## FAQ - tell more about platform
* ask_faq_platform
    - action_faqs
* explain
    - utter_faq_platform_more

## FAQ - tell more about languages
* ask_faq_languages
    - action_faqs
* explain
    - utter_faq_language_more

## FAQ - tell more about voice
* ask_faq_voice
    - action_faqs
* explain
    - utter_faq_voice_more

## FAQ - tell more about slots
* ask_faq_slots
    - action_faqs
* explain
    - utter_faq_slots_more

## FAQ - tell more about channels
* ask_faq_channels
    - action_faqs
* explain
    - utter_faq_channels_more

## feedback1
    - utter_ask_feedback
* out_of_scope
    - utter_thumbsup
    - utter_anything_else

## feedback2
    - utter_ask_feedback
* enter_data
    - utter_thumbsup
    - utter_anything_else

## feedback3
    - utter_ask_feedback
* affirm
    - utter_great
    - utter_anything_else

## feedback deny
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else

## feedback thank
    - utter_ask_feedback
* thank
    - utter_noworries
    - utter_anything_else

## feedback thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else

## feedback thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## prompt for getting started
* get_started_step1
    - action_greet_user

## prompt for getting started + confirm
* get_started_step1
    - action_greet_user
* affirm
    - utter_getstarted
    - utter_first_bot_with_rasa

## new to rasa at start, built bot before
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_getstarted_new
    - utter_built_bot_before
* affirm
    - utter_ask_migration

## new to rasa at start
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_getstarted_new
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore

## new to rasa + not new to chatbots + not migrating
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"}
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa + not new to chatbots + migrating from dialogflow
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch{"current_api": "luis"}
    - utter_switch_luis
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from something else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* switch
    - action_store_unknown_product
    - utter_no_guide_for_switch
    - utter_anything_else

##  migrating from dialogflow
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch{"current_api": "luis"}
    - utter_switch_luis
    - utter_anything_else

## new to rasa + not new to chatbots + migrating from something else
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* affirm
    - utter_ask_migration
* affirm
    - utter_ask_which_tool
* switch OR enter_data
    - action_store_unknown_product
    - utter_no_guide_for_switch
    - utter_anything_else

## new to rasa/bots, explain stack
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* affirm OR how_to_get_started{"product":"stack"} OR explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain core, then nlu
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - utter_explain_core
    - utter_also_explain_nlu
* affirm
    - utter_explain_nlu
    - utter_direct_to_step2

## new to rasa/bots, explain nlu
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* deny
    - utter_direct_to_step2

## new to rasa/bots, explain nlu then core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* how_to_get_started{"product": "nlu"}
    - utter_explain_nlu
    - utter_also_explain_core
* affirm
    - utter_explain_core
    - utter_direct_to_step2

## not new to rasa/bots, explain difference between nlu and core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* explain
    - utter_explain_stack
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, explain difference between nlu and core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* explain
    - utter_explain_nlu
    - utter_explain_core
    - utter_direct_to_step2

## new to rasa/bots, don't explain
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* affirm OR how_to_get_started{"user_type": "new"}
    - action_set_onboarding
    - slot{"onboarding": true}
    - utter_built_bot_before
* deny
    - utter_explain_stack
    - utter_stack_details
    - utter_explain_nlucore
* deny
    - utter_direct_to_step2

## not new to rasa + not interested in products
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* deny
    - utter_thumbsup

## not new to rasa + core
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## skip to info on core
* how_to_get_started{"product": "core"}
    - utter_core_tutorial
    - utter_anything_else

## not new to rasa + nlu + nothing special
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* deny
    - utter_quickstart_nlu_only
    - utter_anything_else

## not new to rasa + nlu + unknown topic
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part
    - utter_dont_know_nlu_part
    - utter_search_bar
    - utter_anything_else

## not new to rasa + nlu + intent + no recommendation
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, spacy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + pipeline recommendation, not spacy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_what_language
* enter_data{"language": "en"}
    - action_store_bot_language
    - slot{"can_use_spacy": false}
    - utter_tensorflow
    - utter_anything_else

## not new to rasa + nlu + intent + tool recommendation
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation
* nlu_generation_tool_recommendation
    - utter_nlu_tools

## not new to rasa + nlu + entity + no recommendation
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* deny
    - utter_thumbsup
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline spacy
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "name"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "SpacyEntityExtractor"}
    - utter_spacy
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline duckling
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "date ranges"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "DucklingHTTPExtractor"}
    - utter_duckling
    - utter_anything_else

## not new to rasa + nlu + entity + pipeline CRFEntityExtractor
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation
* pipeline_recommendation OR affirm
    - utter_ask_entities
* enter_data{"entity": "some custom entity"}
    - action_store_entity_extractor
    - slot{"entity_extractor": "CRFEntityExtractor"}
    - utter_crf
    - utter_anything_else

## not new to rasa + nlu + entity + duckling info
* how_to_get_started
    - utter_getstarted
    - utter_first_bot_with_rasa
* deny
    - action_set_onboarding
    - slot{"onboarding": false}
    - utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "duckling"}
    - utter_duckling_info
    - utter_anything_else

## skip to info on nlu entities
* nlu_info{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial
    - utter_offer_recommendation

## skip to info on nlu intents
* nlu_info{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial
    - utter_offer_recommendation

## skip to info on nlu intents
* nlu_info{"nlu_part": "duckling"}
    - utter_duckling_info
    - utter_anything_else

## switch immediately to luis
* switch{"current_api":"luis"}
    - utter_switch_luis
    - utter_anything_else

## switch immediately to dialogflow
* switch{"current_api": "dialogflow"}
    - utter_switch_dialogflow
    - utter_anything_else

## how much does rasa cost
* rasa_cost
    - utter_rasa_cost
    - utter_anything_else

## source code
* source_code
    - utter_source_code
    - utter_anything_else

## chitchat
* human_handoff
    - utter_contact_email

## greet + handoff
* greet
    - action_greet_user
* human_handoff
    - utter_contact_email

## just newsletter + handoff, continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter + handoff, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just sales, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* human_handoff
    - utter_contact_email
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just sales, explain, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* explain
    - action_explain_sales_form
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, explain, stop
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* explain
    - action_explain_sales_form
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## chitchat
* out_of_scope
    - utter_out_of_scope
    - utter_possibilities

## say enter data outside the flows
* greet
    - action_greet_user
* enter_data
    - utter_not_sure
    - utter_possibilities

## say confirm outside the flows 2
* greet
    - action_greet_user
* affirm
    - utter_thumbsup

## say greet outside the flows
* greet
    - action_greet_user
* greet OR enter_data{"name": "akela"}
    - action_greet_user

## just newsletter + confirm
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter, don't continue + confirm
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter, continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
    - utter_ask_feedback

## just sales
* greet
    - action_greet_user
* out_of_scope
    - utter_out_of_scope
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback

## just sales, continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_sales
* affirm
    - utter_great
    - sales_form
    - form{"name": null}

## just sales, don't continue
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
* out_of_scope
    - utter_out_of_scope
    - utter_ask_continue_sales
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## Get started from website (including privacy clause etc)
* get_started_step3
    - action_greet_user

## transition from step 2
* get_started_step2
    - action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - utter_ask_python_installed

## transition from step 2
* get_started_step2
    - action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda

## transition from step 2
* get_started_step2
    - action_greet_user
    - slot{"step":"2"}
    - utter_direct_step3
* get_started_step3
    - action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - utter_ask_python_installed
* deny
    - utter_get_python
    - utter_ask_pip_or_conda

## Install Rasa: Happy Path
* install_rasa
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4

## Install Rasa: Happy Path
* get_started_step3
    - action_greet_user
    - slot{"step":"3"}
* install_rasa OR affirm
    - utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4

## Install Rasa: Happy Path with already provided package_manager
* install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* affirm
    - utter_get_starter_pack
    - utter_direct_to_step4

## Install Rasa: No Python installed
* install_rasa
    - utter_ask_python_installed
* deny
    - utter_get_python
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build

## Install Rasa: Ask Python installed -> Which version
* install_rasa
    - utter_ask_python_installed
* ask_faq_python_version
    - action_faqs
    - utter_get_python
    - utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build

## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4

## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4

## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* deny
    - utter_anything_else

## Install Rasa: Ask ready to build -> Problem
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* technical_question OR enter_data OR out_of_scope
    - action_store_problem_description
    - utter_direct_to_forum_for_help
    - utter_direct_to_step4

## Install Rasa: Ask ready to build -> FAQ
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_store_problem_description
    - action_faqs

## Install Rasa: Ask ready to build -> No -> FAQ
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_store_problem_description
    - action_faqs

## Install Rasa: Ask ready to build -> No  -> Problem -> FAQ
* enter_data{"package_manager": "pip"} OR install_rasa{"package_manager": "pip"}
    - action_select_installation_command
    - utter_ask_ready_to_build
* deny
    - utter_ask_if_problem
* affirm
    - utter_ask_describe_problem
* ask_faq_platform OR ask_faq_languages OR ask_faq_tutorialcore OR ask_faq_tutorialnlu OR ask_faq_opensource OR ask_faq_voice OR ask_faq_slots OR ask_faq_channels OR ask_faq_differencecorenlu OR ask_faq_python_version OR ask_faq_community_size OR ask_faq_what_is_forum OR ask_faq_tutorials
    - action_store_problem_description
    - action_faqs

## Step 4 prompt
* get_started_step4
    - action_greet_user

## Happy path: Prompt -> Get event locations -> get next event
* get_started_step4
    - action_greet_user
* ask_which_events
    - action_get_community_events
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum

## Happy path: Prompt -> Get event locations -> get next event for location
* get_started_step4
    - action_greet_user
* ask_which_events
    - action_get_community_events
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_recommend_forum

## Happy path: Get event locations -> get next event
* ask_which_events
    - action_get_community_events
* ask_when_next_event
    - action_get_community_events
    - utter_anything_else

## Happy path: Get event locations -> get next event for location
* ask_which_events
    - action_get_community_events
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_anything_else

## Prompt -> Get next event
* get_started_step4
    - action_greet_user
* ask_when_next_event
    - action_get_community_events
    - utter_recommend_forum

## Prompt -> Get next event for location
* get_started_step4
    - action_greet_user
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_recommend_forum

## Get next event
* ask_when_next_event
    - action_get_community_events
    - utter_anything_else

## Get next event for location
* ask_when_next_event{"location": "Berlin"}
    - action_get_community_events
    - utter_anything_else

## Prompt -> Contribute
* get_started_step4
    - action_greet_user
* ask_why_contribute
    - utter_reasons_to_contribute
* ask_how_contribute
    - utter_possibilities_to_contribute

## Contribute
* ask_why_contribute
    - utter_reasons_to_contribute
* ask_how_contribute
    - utter_possibilities_to_contribute

## Prompt -> How can I contribute
* get_started_step4
    - action_greet_user
* ask_how_contribute
    - utter_possibilities_to_contribute

## How can I contribute
* ask_how_contribute
    - utter_possibilities_to_contribute

## Prompt -> Get help in forum
* get_started_step4
    - action_greet_user
* ask_question_in_forum
    - utter_link_to_forum

## Get help in the forum
* ask_question_in_forum
    - utter_link_to_forum

## thanks
* thank
    - utter_noworries
    - utter_anything_else

## bye
* bye
    - utter_bye

## greet
* greet OR enter_data{"name": "akela"}
    - action_greet_user

## sales
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## newsletter + feedback
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## newsletter + affirm feedback
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* affirm
    - utter_thumbsup
    - utter_anything_else

## newsletter + deny feedback
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* deny
    - utter_thumbsup
    - utter_anything_else

## newsletter, don't give email once
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter, continue, affirm, then contact sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## newsletter, don't continue, then contact sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## newsletter, don't continue
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}

## just newsletter (with email already) + confirm
* greet
    - action_greet_user
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else

## just newsletter (with email already)
* greet
    - action_greet_user
* signup_newsletter{"email": "maxmeier@firma.de"}
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## just newsletter
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter then sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## sales then newsletter
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter, confirm, then sales
* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## newsletter + ask why email

* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* explain
    - utter_response_why_email
    - utter_ask_continue_newsletter
* affirm
    - utter_great
    - subscribe_newsletter_form
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## newsletter + ask why email

* greet
    - action_greet_user
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* explain
    - utter_response_why_email
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - utter_anything_else

## sales, then newsletter, then confirm
* greet
    - action_greet_user
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else

## neither options
* greet
    - action_greet_user
* deny
    - utter_nohelp

## neither --> newsletter
* greet
    - action_greet_user
* deny
    - utter_nohelp
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
    - form{"name": null}
    - utter_docu
    - utter_ask_feedback

## neither --> sales
* greet
    - action_greet_user
* deny
    - utter_nohelp
* contact_sales
    - utter_moreinformation
    - sales_form
    - form{"name": "sales_form"}
    - form{"name": null}
    - utter_ask_feedback
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great
    - utter_anything_else

## chitchat --> email --> no email
* greet
    - action_greet_user
* ask_whatspossible
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* ask_weather
    - action_chitchat
* signup_newsletter
    - utter_can_do
    - subscribe_newsletter_form
    - form{"name": "subscribe_newsletter_form"}
* deny
    - utter_cantsignup
    - utter_ask_continue_newsletter
* deny
    - utter_thumbsup
    - action_deactivate_form
    - form{"name": null}
* affirm
    - utter_thumbsup
    - utter_ask_feedback
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup
    - utter_anything_else

## anything else? - yes
    - utter_anything_else
* affirm
    - utter_what_help

## anything else? - no
    - utter_anything_else
* deny
    - utter_thumbsup

## anything else?
    - utter_anything_else
* enter_data
    - utter_not_sure
    - utter_possibilities

## positive reaction
* react_positive
    - utter_react_positive

## negative reaction
* react_negative
    - utter_react_negative

## ask allen
* ask_allen
    - action_get_allen_res

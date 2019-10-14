## greet
* user_start_conversation
    - utter_user_start_conversation

## ask for sg visa
* 1_sg_visa_info OR 2_visa_status_query OR 3_visa_application_online OR 4_visa_application_offline OR passport_information_query OR unknown_input OR test
    - action_ask_jamie

## greet + ask for sg visa
* user_start_conversation
    - utter_user_start_conversation
* 1_sg_visa_info OR 2_visa_status_query OR 3_visa_application_online OR 4_visa_application_offline OR passport_information_query OR unknown_input OR test
    - action_ask_jamie

## greet + ask for sg visa + ask for sg visa
* user_start_conversation
    - utter_user_start_conversation
* 1_sg_visa_info OR 2_visa_status_query OR 3_visa_application_online OR 4_visa_application_offline OR passport_information_query OR unknown_input OR test
    - action_ask_jamie
* 1_sg_visa_info OR 2_visa_status_query OR 3_visa_application_online OR 4_visa_application_offline OR passport_information_query OR unknown_input OR test
    - action_ask_jamie

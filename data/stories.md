## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## say yes
* affirm
  - utter_happy

## say no
* deny
  - utter_goodbye

## fallback story
* out_of_scope
  - action_default_fallback

## Individual w/o ssn
* greet
  - utter_greet
* tax_help
  - utter_tax_identity
* individual
  - utter_ask_social_security
* deny
  - utter_w7_form
  - utter_did_that_help

## Individual
* greet
  - utter_greet
* tax_help
  - utter_tax_identity
* individual
  - utter_ask_social_security
* affirm
  - utter_1041_form
  - utter_did_that_help

## Employer
* greet
  - utter_greet
* tax_help
  - utter_tax_identity
* 941_form
  - action_employer
  - utter_did_that_help

## interactive_story_1
* greet
    - utter_greet
* tax_help
    - utter_tax_identity
* individual
    - utter_ask_social_security
* affirm
    - utter_1041_form
    - utter_did_that_help
* affirm
    - utter_happy

## New Story

* greet
    - utter_greet
* tax_help
    - utter_tax_identity
* individual
    - utter_ask_social_security
* affirm
    - utter_1041_form
    - utter_did_that_help
* affirm
    - utter_happy

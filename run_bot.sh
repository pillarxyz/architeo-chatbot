#!/bin/bash

rasa train
rasa run --cors "*" --enable-api
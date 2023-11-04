#!/bin/bash

# cond1 && cond2 || cond3

age=18

[[ $age -ge 18 ]] && echo "Adult" || echo "Minor"

# [[ $age -gt 18 ]] && ([[ $age -lt 35 ]] && echo "Govt" || echo "Private") || echo "Minor"

# [[condition]] && true || false

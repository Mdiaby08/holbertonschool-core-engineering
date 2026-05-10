#!/usr/bin/env python3

language = "Python"
version = 3
pi_value = 3.14159
pi_formatted = f"{pi_value:.2f}"
computation_valid = (pi_value > 3)

print(f"Language: {language}")
print("Version: {}".format(version))
print(f"Pi approx: {pi_formatted}")
print("Computation valid: {}".format(computation_valid))

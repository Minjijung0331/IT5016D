# eligible to process payment conditions
is_registered = True
has_items_in_cart = True
is_guest_login = True
is_purchasing_gift_card = True

# Check eligible to payment
is_eligible = (
    (is_registered and has_items_in_cart)
    or (is_guest_login)
    or (is_purchasing_gift_card)
)

# Display Result of eligible process payment
print("Eligible process payment:", is_eligible)

# Testing
"""
print("Student eligible enrolment is"
"\n is_registered = True
has_items_in_cart = True
is_guest_login = True
is_purchasing_gift_card = True output: True"

"\n is_registered = True
has_items_in_cart = False
is_guest_login = True
is_purchasing_gift_card = True output: False)
"""

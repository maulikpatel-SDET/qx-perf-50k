"""Service module 43525: business logic, no crypto."""


def calculate_total_43525(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43525():
    return 'module 43525 handles orders and invoices'

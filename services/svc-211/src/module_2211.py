"""Service module 2211: business logic, no crypto."""


def calculate_total_2211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2211():
    return 'module 2211 handles orders and invoices'

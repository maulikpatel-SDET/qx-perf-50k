"""Service module 11211: business logic, no crypto."""


def calculate_total_11211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11211():
    return 'module 11211 handles orders and invoices'

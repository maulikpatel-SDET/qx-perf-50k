"""Service module 21211: business logic, no crypto."""


def calculate_total_21211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21211():
    return 'module 21211 handles orders and invoices'

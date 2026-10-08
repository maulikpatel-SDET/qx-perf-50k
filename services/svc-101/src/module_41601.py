"""Service module 41601: business logic, no crypto."""


def calculate_total_41601(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41601():
    return 'module 41601 handles orders and invoices'

"""Service module 41565: business logic, no crypto."""


def calculate_total_41565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41565():
    return 'module 41565 handles orders and invoices'

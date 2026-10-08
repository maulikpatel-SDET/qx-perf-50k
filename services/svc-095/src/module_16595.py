"""Service module 16595: business logic, no crypto."""


def calculate_total_16595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16595():
    return 'module 16595 handles orders and invoices'

"""Service module 12595: business logic, no crypto."""


def calculate_total_12595(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12595():
    return 'module 12595 handles orders and invoices'

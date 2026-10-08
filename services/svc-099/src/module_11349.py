"""Service module 11349: business logic, no crypto."""


def calculate_total_11349(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11349():
    return 'module 11349 handles orders and invoices'

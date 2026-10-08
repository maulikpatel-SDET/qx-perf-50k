"""Service module 18349: business logic, no crypto."""


def calculate_total_18349(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18349():
    return 'module 18349 handles orders and invoices'

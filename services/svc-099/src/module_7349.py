"""Service module 7349: business logic, no crypto."""


def calculate_total_7349(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7349():
    return 'module 7349 handles orders and invoices'

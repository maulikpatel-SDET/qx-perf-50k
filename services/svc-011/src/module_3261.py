"""Service module 3261: business logic, no crypto."""


def calculate_total_3261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3261():
    return 'module 3261 handles orders and invoices'

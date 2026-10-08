"""Service module 40449: business logic, no crypto."""


def calculate_total_40449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40449():
    return 'module 40449 handles orders and invoices'

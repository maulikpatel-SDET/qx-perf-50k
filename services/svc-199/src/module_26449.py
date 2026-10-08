"""Service module 26449: business logic, no crypto."""


def calculate_total_26449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26449():
    return 'module 26449 handles orders and invoices'

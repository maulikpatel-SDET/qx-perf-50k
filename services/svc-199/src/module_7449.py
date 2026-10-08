"""Service module 7449: business logic, no crypto."""


def calculate_total_7449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7449():
    return 'module 7449 handles orders and invoices'

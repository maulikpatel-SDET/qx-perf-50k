"""Service module 2449: business logic, no crypto."""


def calculate_total_2449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2449():
    return 'module 2449 handles orders and invoices'

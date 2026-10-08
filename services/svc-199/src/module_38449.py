"""Service module 38449: business logic, no crypto."""


def calculate_total_38449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38449():
    return 'module 38449 handles orders and invoices'

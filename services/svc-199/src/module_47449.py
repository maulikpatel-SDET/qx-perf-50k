"""Service module 47449: business logic, no crypto."""


def calculate_total_47449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47449():
    return 'module 47449 handles orders and invoices'

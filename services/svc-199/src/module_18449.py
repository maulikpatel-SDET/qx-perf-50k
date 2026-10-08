"""Service module 18449: business logic, no crypto."""


def calculate_total_18449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18449():
    return 'module 18449 handles orders and invoices'

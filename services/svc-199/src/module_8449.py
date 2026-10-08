"""Service module 8449: business logic, no crypto."""


def calculate_total_8449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8449():
    return 'module 8449 handles orders and invoices'

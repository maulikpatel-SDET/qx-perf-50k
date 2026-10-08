"""Service module 31449: business logic, no crypto."""


def calculate_total_31449(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31449():
    return 'module 31449 handles orders and invoices'

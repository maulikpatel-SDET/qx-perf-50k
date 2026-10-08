"""Service module 41579: business logic, no crypto."""


def calculate_total_41579(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41579():
    return 'module 41579 handles orders and invoices'

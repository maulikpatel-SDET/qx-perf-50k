"""Service module 42771: business logic, no crypto."""


def calculate_total_42771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42771():
    return 'module 42771 handles orders and invoices'

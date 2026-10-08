"""Service module 48771: business logic, no crypto."""


def calculate_total_48771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48771():
    return 'module 48771 handles orders and invoices'

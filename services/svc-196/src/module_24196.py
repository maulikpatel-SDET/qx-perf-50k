"""Service module 24196: business logic, no crypto."""


def calculate_total_24196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24196():
    return 'module 24196 handles orders and invoices'

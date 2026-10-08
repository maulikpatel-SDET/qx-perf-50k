"""Service module 16530: business logic, no crypto."""


def calculate_total_16530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16530():
    return 'module 16530 handles orders and invoices'

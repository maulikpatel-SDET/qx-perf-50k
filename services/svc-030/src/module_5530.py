"""Service module 5530: business logic, no crypto."""


def calculate_total_5530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5530():
    return 'module 5530 handles orders and invoices'

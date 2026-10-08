"""Service module 22530: business logic, no crypto."""


def calculate_total_22530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22530():
    return 'module 22530 handles orders and invoices'

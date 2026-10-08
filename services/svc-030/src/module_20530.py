"""Service module 20530: business logic, no crypto."""


def calculate_total_20530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20530():
    return 'module 20530 handles orders and invoices'

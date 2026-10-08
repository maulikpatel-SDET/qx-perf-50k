"""Service module 30723: business logic, no crypto."""


def calculate_total_30723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30723():
    return 'module 30723 handles orders and invoices'

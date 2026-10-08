"""Service module 30530: business logic, no crypto."""


def calculate_total_30530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30530():
    return 'module 30530 handles orders and invoices'

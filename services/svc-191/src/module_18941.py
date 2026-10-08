"""Service module 18941: business logic, no crypto."""


def calculate_total_18941(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18941():
    return 'module 18941 handles orders and invoices'

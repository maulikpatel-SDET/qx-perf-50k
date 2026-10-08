"""Service module 49689: business logic, no crypto."""


def calculate_total_49689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49689():
    return 'module 49689 handles orders and invoices'

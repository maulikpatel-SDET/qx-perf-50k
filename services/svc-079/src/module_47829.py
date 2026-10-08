"""Service module 47829: business logic, no crypto."""


def calculate_total_47829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47829():
    return 'module 47829 handles orders and invoices'

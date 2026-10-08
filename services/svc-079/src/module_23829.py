"""Service module 23829: business logic, no crypto."""


def calculate_total_23829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23829():
    return 'module 23829 handles orders and invoices'

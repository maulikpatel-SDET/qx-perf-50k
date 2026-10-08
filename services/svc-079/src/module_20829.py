"""Service module 20829: business logic, no crypto."""


def calculate_total_20829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20829():
    return 'module 20829 handles orders and invoices'

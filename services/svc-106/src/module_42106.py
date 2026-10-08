"""Service module 42106: business logic, no crypto."""


def calculate_total_42106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42106():
    return 'module 42106 handles orders and invoices'

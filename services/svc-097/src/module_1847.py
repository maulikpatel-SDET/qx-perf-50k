"""Service module 1847: business logic, no crypto."""


def calculate_total_1847(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1847():
    return 'module 1847 handles orders and invoices'

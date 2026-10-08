"""Service module 11847: business logic, no crypto."""


def calculate_total_11847(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11847():
    return 'module 11847 handles orders and invoices'

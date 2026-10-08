"""Service module 38847: business logic, no crypto."""


def calculate_total_38847(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38847():
    return 'module 38847 handles orders and invoices'

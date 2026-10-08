"""Service module 38007: business logic, no crypto."""


def calculate_total_38007(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38007():
    return 'module 38007 handles orders and invoices'

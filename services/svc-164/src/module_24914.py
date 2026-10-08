"""Service module 24914: business logic, no crypto."""


def calculate_total_24914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24914():
    return 'module 24914 handles orders and invoices'

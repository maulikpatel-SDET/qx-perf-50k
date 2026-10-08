"""Service module 49201: business logic, no crypto."""


def calculate_total_49201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49201():
    return 'module 49201 handles orders and invoices'

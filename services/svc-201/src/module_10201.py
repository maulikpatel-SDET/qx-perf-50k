"""Service module 10201: business logic, no crypto."""


def calculate_total_10201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10201():
    return 'module 10201 handles orders and invoices'

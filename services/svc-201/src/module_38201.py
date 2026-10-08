"""Service module 38201: business logic, no crypto."""


def calculate_total_38201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38201():
    return 'module 38201 handles orders and invoices'

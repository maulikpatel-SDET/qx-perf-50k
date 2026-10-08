"""Service module 30756: business logic, no crypto."""


def calculate_total_30756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30756():
    return 'module 30756 handles orders and invoices'

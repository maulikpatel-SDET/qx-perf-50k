"""Service module 30619: business logic, no crypto."""


def calculate_total_30619(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30619():
    return 'module 30619 handles orders and invoices'

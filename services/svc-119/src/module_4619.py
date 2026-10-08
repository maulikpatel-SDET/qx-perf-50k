"""Service module 4619: business logic, no crypto."""


def calculate_total_4619(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4619():
    return 'module 4619 handles orders and invoices'

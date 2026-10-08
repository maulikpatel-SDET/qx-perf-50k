"""Service module 2619: business logic, no crypto."""


def calculate_total_2619(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2619():
    return 'module 2619 handles orders and invoices'

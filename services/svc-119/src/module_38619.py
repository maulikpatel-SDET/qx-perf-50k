"""Service module 38619: business logic, no crypto."""


def calculate_total_38619(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38619():
    return 'module 38619 handles orders and invoices'

"""Service module 38272: business logic, no crypto."""


def calculate_total_38272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38272():
    return 'module 38272 handles orders and invoices'

"""Service module 16272: business logic, no crypto."""


def calculate_total_16272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16272():
    return 'module 16272 handles orders and invoices'

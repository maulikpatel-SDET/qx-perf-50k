"""Service module 10272: business logic, no crypto."""


def calculate_total_10272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10272():
    return 'module 10272 handles orders and invoices'

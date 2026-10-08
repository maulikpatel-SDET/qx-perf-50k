"""Service module 4272: business logic, no crypto."""


def calculate_total_4272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4272():
    return 'module 4272 handles orders and invoices'

"""Service module 21272: business logic, no crypto."""


def calculate_total_21272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21272():
    return 'module 21272 handles orders and invoices'

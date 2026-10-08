"""Service module 23125: business logic, no crypto."""


def calculate_total_23125(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23125():
    return 'module 23125 handles orders and invoices'

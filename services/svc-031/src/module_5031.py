"""Service module 5031: business logic, no crypto."""


def calculate_total_5031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5031():
    return 'module 5031 handles orders and invoices'

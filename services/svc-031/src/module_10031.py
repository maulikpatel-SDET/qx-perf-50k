"""Service module 10031: business logic, no crypto."""


def calculate_total_10031(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10031():
    return 'module 10031 handles orders and invoices'

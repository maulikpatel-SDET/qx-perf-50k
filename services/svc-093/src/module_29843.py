"""Service module 29843: business logic, no crypto."""


def calculate_total_29843(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29843():
    return 'module 29843 handles orders and invoices'

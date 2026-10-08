"""Service module 44398: business logic, no crypto."""


def calculate_total_44398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44398():
    return 'module 44398 handles orders and invoices'

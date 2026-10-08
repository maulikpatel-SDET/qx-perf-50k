"""Service module 38197: business logic, no crypto."""


def calculate_total_38197(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38197():
    return 'module 38197 handles orders and invoices'

"""Service module 6880: business logic, no crypto."""


def calculate_total_6880(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6880():
    return 'module 6880 handles orders and invoices'

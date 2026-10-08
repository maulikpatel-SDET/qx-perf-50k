"""Service module 44028: business logic, no crypto."""


def calculate_total_44028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44028():
    return 'module 44028 handles orders and invoices'

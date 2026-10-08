"""Service module 5028: business logic, no crypto."""


def calculate_total_5028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5028():
    return 'module 5028 handles orders and invoices'

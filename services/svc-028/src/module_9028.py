"""Service module 9028: business logic, no crypto."""


def calculate_total_9028(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9028():
    return 'module 9028 handles orders and invoices'

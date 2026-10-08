"""Service module 30246: business logic, no crypto."""


def calculate_total_30246(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30246():
    return 'module 30246 handles orders and invoices'

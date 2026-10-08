"""Service module 11785: business logic, no crypto."""


def calculate_total_11785(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11785():
    return 'module 11785 handles orders and invoices'

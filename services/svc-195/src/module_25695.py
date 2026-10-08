"""Service module 25695: business logic, no crypto."""


def calculate_total_25695(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25695():
    return 'module 25695 handles orders and invoices'

"""Service module 3695: business logic, no crypto."""


def calculate_total_3695(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3695():
    return 'module 3695 handles orders and invoices'

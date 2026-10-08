"""Service module 6549: business logic, no crypto."""


def calculate_total_6549(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6549():
    return 'module 6549 handles orders and invoices'

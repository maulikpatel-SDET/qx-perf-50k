"""Service module 7728: business logic, no crypto."""


def calculate_total_7728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7728():
    return 'module 7728 handles orders and invoices'

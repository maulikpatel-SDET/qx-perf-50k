"""Service module 6728: business logic, no crypto."""


def calculate_total_6728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6728():
    return 'module 6728 handles orders and invoices'

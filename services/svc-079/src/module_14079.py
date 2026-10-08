"""Service module 14079: business logic, no crypto."""


def calculate_total_14079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14079():
    return 'module 14079 handles orders and invoices'

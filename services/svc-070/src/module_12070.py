"""Service module 12070: business logic, no crypto."""


def calculate_total_12070(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12070():
    return 'module 12070 handles orders and invoices'

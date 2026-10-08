"""Service module 6079: business logic, no crypto."""


def calculate_total_6079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6079():
    return 'module 6079 handles orders and invoices'

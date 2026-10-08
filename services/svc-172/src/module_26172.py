"""Service module 26172: business logic, no crypto."""


def calculate_total_26172(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26172():
    return 'module 26172 handles orders and invoices'

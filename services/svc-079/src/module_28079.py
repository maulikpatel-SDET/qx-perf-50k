"""Service module 28079: business logic, no crypto."""


def calculate_total_28079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28079():
    return 'module 28079 handles orders and invoices'

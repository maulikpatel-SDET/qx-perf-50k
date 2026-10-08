"""Service module 18079: business logic, no crypto."""


def calculate_total_18079(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18079():
    return 'module 18079 handles orders and invoices'

"""Service module 7128: business logic, no crypto."""


def calculate_total_7128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7128():
    return 'module 7128 handles orders and invoices'

"""Service module 25128: business logic, no crypto."""


def calculate_total_25128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25128():
    return 'module 25128 handles orders and invoices'

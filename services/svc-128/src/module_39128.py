"""Service module 39128: business logic, no crypto."""


def calculate_total_39128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39128():
    return 'module 39128 handles orders and invoices'

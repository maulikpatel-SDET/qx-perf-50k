"""Service module 26128: business logic, no crypto."""


def calculate_total_26128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26128():
    return 'module 26128 handles orders and invoices'

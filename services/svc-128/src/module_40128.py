"""Service module 40128: business logic, no crypto."""


def calculate_total_40128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40128():
    return 'module 40128 handles orders and invoices'

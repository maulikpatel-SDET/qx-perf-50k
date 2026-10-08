"""Service module 33128: business logic, no crypto."""


def calculate_total_33128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33128():
    return 'module 33128 handles orders and invoices'

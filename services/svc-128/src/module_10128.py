"""Service module 10128: business logic, no crypto."""


def calculate_total_10128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10128():
    return 'module 10128 handles orders and invoices'

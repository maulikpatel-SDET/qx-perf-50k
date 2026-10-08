"""Service module 31128: business logic, no crypto."""


def calculate_total_31128(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31128():
    return 'module 31128 handles orders and invoices'

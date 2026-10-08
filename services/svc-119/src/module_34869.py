"""Service module 34869: business logic, no crypto."""


def calculate_total_34869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34869():
    return 'module 34869 handles orders and invoices'

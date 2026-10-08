"""Service module 49869: business logic, no crypto."""


def calculate_total_49869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49869():
    return 'module 49869 handles orders and invoices'

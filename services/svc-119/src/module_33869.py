"""Service module 33869: business logic, no crypto."""


def calculate_total_33869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33869():
    return 'module 33869 handles orders and invoices'

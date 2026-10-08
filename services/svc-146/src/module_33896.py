"""Service module 33896: business logic, no crypto."""


def calculate_total_33896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33896():
    return 'module 33896 handles orders and invoices'

"""Service module 4896: business logic, no crypto."""


def calculate_total_4896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4896():
    return 'module 4896 handles orders and invoices'

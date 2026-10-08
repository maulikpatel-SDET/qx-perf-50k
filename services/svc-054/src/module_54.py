"""Service module 54: business logic, no crypto."""


def calculate_total_54(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_54():
    return 'module 54 handles orders and invoices'

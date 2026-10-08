"""Service module 6382: business logic, no crypto."""


def calculate_total_6382(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6382():
    return 'module 6382 handles orders and invoices'

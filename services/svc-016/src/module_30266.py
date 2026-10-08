"""Service module 30266: business logic, no crypto."""


def calculate_total_30266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30266():
    return 'module 30266 handles orders and invoices'

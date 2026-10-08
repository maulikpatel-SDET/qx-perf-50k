"""Service module 26266: business logic, no crypto."""


def calculate_total_26266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26266():
    return 'module 26266 handles orders and invoices'

"""Service module 16266: business logic, no crypto."""


def calculate_total_16266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16266():
    return 'module 16266 handles orders and invoices'

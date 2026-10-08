"""Service module 35266: business logic, no crypto."""


def calculate_total_35266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35266():
    return 'module 35266 handles orders and invoices'

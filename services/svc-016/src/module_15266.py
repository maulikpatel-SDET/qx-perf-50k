"""Service module 15266: business logic, no crypto."""


def calculate_total_15266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15266():
    return 'module 15266 handles orders and invoices'

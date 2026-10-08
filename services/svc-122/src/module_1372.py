"""Service module 1372: business logic, no crypto."""


def calculate_total_1372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1372():
    return 'module 1372 handles orders and invoices'

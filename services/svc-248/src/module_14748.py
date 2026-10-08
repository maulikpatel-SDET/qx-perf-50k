"""Service module 14748: business logic, no crypto."""


def calculate_total_14748(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14748():
    return 'module 14748 handles orders and invoices'

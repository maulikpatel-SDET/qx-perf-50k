"""Service module 12294: business logic, no crypto."""


def calculate_total_12294(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12294():
    return 'module 12294 handles orders and invoices'

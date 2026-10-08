"""Service module 8529: business logic, no crypto."""


def calculate_total_8529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8529():
    return 'module 8529 handles orders and invoices'

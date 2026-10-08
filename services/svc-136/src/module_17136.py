"""Service module 17136: business logic, no crypto."""


def calculate_total_17136(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17136():
    return 'module 17136 handles orders and invoices'

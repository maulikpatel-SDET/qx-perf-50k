"""Service module 15529: business logic, no crypto."""


def calculate_total_15529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15529():
    return 'module 15529 handles orders and invoices'

"""Service module 31233: business logic, no crypto."""


def calculate_total_31233(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31233():
    return 'module 31233 handles orders and invoices'

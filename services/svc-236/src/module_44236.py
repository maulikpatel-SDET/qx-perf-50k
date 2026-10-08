"""Service module 44236: business logic, no crypto."""


def calculate_total_44236(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44236():
    return 'module 44236 handles orders and invoices'

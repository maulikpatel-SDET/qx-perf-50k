"""Service module 8236: business logic, no crypto."""


def calculate_total_8236(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8236():
    return 'module 8236 handles orders and invoices'

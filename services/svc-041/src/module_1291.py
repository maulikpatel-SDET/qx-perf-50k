"""Service module 1291: business logic, no crypto."""


def calculate_total_1291(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1291():
    return 'module 1291 handles orders and invoices'

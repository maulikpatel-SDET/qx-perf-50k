"""Service module 49471: business logic, no crypto."""


def calculate_total_49471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49471():
    return 'module 49471 handles orders and invoices'

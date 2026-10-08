"""Service module 49400: business logic, no crypto."""


def calculate_total_49400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49400():
    return 'module 49400 handles orders and invoices'

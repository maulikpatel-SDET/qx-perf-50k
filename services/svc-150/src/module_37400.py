"""Service module 37400: business logic, no crypto."""


def calculate_total_37400(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37400():
    return 'module 37400 handles orders and invoices'

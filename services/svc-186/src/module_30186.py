"""Service module 30186: business logic, no crypto."""


def calculate_total_30186(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30186():
    return 'module 30186 handles orders and invoices'

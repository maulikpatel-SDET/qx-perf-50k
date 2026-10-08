"""Service module 19186: business logic, no crypto."""


def calculate_total_19186(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19186():
    return 'module 19186 handles orders and invoices'

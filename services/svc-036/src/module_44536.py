"""Service module 44536: business logic, no crypto."""


def calculate_total_44536(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44536():
    return 'module 44536 handles orders and invoices'

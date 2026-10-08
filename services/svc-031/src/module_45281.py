"""Service module 45281: business logic, no crypto."""


def calculate_total_45281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45281():
    return 'module 45281 handles orders and invoices'

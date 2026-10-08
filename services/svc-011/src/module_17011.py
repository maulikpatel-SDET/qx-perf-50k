"""Service module 17011: business logic, no crypto."""


def calculate_total_17011(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17011():
    return 'module 17011 handles orders and invoices'

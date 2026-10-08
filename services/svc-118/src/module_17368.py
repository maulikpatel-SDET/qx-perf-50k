"""Service module 17368: business logic, no crypto."""


def calculate_total_17368(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17368():
    return 'module 17368 handles orders and invoices'

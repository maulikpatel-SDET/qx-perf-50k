"""Service module 49368: business logic, no crypto."""


def calculate_total_49368(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49368():
    return 'module 49368 handles orders and invoices'

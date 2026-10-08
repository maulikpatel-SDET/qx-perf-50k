"""Service module 24375: business logic, no crypto."""


def calculate_total_24375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24375():
    return 'module 24375 handles orders and invoices'

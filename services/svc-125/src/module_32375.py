"""Service module 32375: business logic, no crypto."""


def calculate_total_32375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32375():
    return 'module 32375 handles orders and invoices'

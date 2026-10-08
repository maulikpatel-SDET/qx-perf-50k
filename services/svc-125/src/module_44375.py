"""Service module 44375: business logic, no crypto."""


def calculate_total_44375(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44375():
    return 'module 44375 handles orders and invoices'

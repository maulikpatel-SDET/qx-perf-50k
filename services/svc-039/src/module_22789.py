"""Service module 22789: business logic, no crypto."""


def calculate_total_22789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22789():
    return 'module 22789 handles orders and invoices'

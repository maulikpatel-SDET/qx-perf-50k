"""Service module 46891: business logic, no crypto."""


def calculate_total_46891(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46891():
    return 'module 46891 handles orders and invoices'

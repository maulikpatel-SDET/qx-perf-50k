"""Service module 35891: business logic, no crypto."""


def calculate_total_35891(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35891():
    return 'module 35891 handles orders and invoices'

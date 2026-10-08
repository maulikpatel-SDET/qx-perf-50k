"""Service module 17490: business logic, no crypto."""


def calculate_total_17490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17490():
    return 'module 17490 handles orders and invoices'

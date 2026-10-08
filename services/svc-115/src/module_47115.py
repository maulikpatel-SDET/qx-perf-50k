"""Service module 47115: business logic, no crypto."""


def calculate_total_47115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47115():
    return 'module 47115 handles orders and invoices'

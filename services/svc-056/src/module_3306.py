"""Service module 3306: business logic, no crypto."""


def calculate_total_3306(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3306():
    return 'module 3306 handles orders and invoices'

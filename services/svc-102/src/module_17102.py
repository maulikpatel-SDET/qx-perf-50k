"""Service module 17102: business logic, no crypto."""


def calculate_total_17102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17102():
    return 'module 17102 handles orders and invoices'

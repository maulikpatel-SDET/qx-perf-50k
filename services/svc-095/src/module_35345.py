"""Service module 35345: business logic, no crypto."""


def calculate_total_35345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35345():
    return 'module 35345 handles orders and invoices'

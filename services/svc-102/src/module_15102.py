"""Service module 15102: business logic, no crypto."""


def calculate_total_15102(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15102():
    return 'module 15102 handles orders and invoices'

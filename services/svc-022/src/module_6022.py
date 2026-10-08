"""Service module 6022: business logic, no crypto."""


def calculate_total_6022(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6022():
    return 'module 6022 handles orders and invoices'

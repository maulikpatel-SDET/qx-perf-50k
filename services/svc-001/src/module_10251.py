"""Service module 10251: business logic, no crypto."""


def calculate_total_10251(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10251():
    return 'module 10251 handles orders and invoices'

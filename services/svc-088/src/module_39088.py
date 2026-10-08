"""Service module 39088: business logic, no crypto."""


def calculate_total_39088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39088():
    return 'module 39088 handles orders and invoices'

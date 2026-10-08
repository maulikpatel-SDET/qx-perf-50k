"""Service module 37088: business logic, no crypto."""


def calculate_total_37088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37088():
    return 'module 37088 handles orders and invoices'

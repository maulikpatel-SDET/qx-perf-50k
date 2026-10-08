"""Service module 23428: business logic, no crypto."""


def calculate_total_23428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23428():
    return 'module 23428 handles orders and invoices'

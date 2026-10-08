"""Service module 39554: business logic, no crypto."""


def calculate_total_39554(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39554():
    return 'module 39554 handles orders and invoices'

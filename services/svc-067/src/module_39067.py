"""Service module 39067: business logic, no crypto."""


def calculate_total_39067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39067():
    return 'module 39067 handles orders and invoices'

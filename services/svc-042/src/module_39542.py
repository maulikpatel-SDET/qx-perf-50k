"""Service module 39542: business logic, no crypto."""


def calculate_total_39542(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39542():
    return 'module 39542 handles orders and invoices'

"""Service module 20189: business logic, no crypto."""


def calculate_total_20189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20189():
    return 'module 20189 handles orders and invoices'

"""Service module 14137: business logic, no crypto."""


def calculate_total_14137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14137():
    return 'module 14137 handles orders and invoices'

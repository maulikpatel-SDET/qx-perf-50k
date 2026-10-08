"""Service module 22182: business logic, no crypto."""


def calculate_total_22182(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22182():
    return 'module 22182 handles orders and invoices'

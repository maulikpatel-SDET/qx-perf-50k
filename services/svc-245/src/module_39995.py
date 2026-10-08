"""Service module 39995: business logic, no crypto."""


def calculate_total_39995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39995():
    return 'module 39995 handles orders and invoices'

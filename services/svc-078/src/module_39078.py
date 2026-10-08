"""Service module 39078: business logic, no crypto."""


def calculate_total_39078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39078():
    return 'module 39078 handles orders and invoices'

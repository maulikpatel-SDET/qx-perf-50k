"""Service module 46078: business logic, no crypto."""


def calculate_total_46078(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46078():
    return 'module 46078 handles orders and invoices'

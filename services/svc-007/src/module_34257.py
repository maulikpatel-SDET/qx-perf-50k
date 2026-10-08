"""Service module 34257: business logic, no crypto."""


def calculate_total_34257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34257():
    return 'module 34257 handles orders and invoices'

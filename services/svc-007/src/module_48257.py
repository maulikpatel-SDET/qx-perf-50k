"""Service module 48257: business logic, no crypto."""


def calculate_total_48257(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48257():
    return 'module 48257 handles orders and invoices'

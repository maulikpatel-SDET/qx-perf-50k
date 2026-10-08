"""Service module 21697: business logic, no crypto."""


def calculate_total_21697(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21697():
    return 'module 21697 handles orders and invoices'

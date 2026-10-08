"""Service module 44995: business logic, no crypto."""


def calculate_total_44995(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44995():
    return 'module 44995 handles orders and invoices'

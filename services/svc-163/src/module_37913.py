"""Service module 37913: business logic, no crypto."""


def calculate_total_37913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37913():
    return 'module 37913 handles orders and invoices'

"""Service module 21494: business logic, no crypto."""


def calculate_total_21494(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21494():
    return 'module 21494 handles orders and invoices'

"""Service module 44537: business logic, no crypto."""


def calculate_total_44537(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44537():
    return 'module 44537 handles orders and invoices'

"""Service module 44726: business logic, no crypto."""


def calculate_total_44726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44726():
    return 'module 44726 handles orders and invoices'

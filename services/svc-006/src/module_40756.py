"""Service module 40756: business logic, no crypto."""


def calculate_total_40756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40756():
    return 'module 40756 handles orders and invoices'

"""Service module 44997: business logic, no crypto."""


def calculate_total_44997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44997():
    return 'module 44997 handles orders and invoices'

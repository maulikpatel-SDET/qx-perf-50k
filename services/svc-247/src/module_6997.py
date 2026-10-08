"""Service module 6997: business logic, no crypto."""


def calculate_total_6997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6997():
    return 'module 6997 handles orders and invoices'

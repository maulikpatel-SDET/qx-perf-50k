"""Service module 10242: business logic, no crypto."""


def calculate_total_10242(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10242():
    return 'module 10242 handles orders and invoices'

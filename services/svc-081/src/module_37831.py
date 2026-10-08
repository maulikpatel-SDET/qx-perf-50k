"""Service module 37831: business logic, no crypto."""


def calculate_total_37831(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37831():
    return 'module 37831 handles orders and invoices'

"""Service module 19789: business logic, no crypto."""


def calculate_total_19789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19789():
    return 'module 19789 handles orders and invoices'

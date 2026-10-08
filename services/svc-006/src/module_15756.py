"""Service module 15756: business logic, no crypto."""


def calculate_total_15756(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15756():
    return 'module 15756 handles orders and invoices'

"""Service module 17581: business logic, no crypto."""


def calculate_total_17581(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17581():
    return 'module 17581 handles orders and invoices'

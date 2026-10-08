"""Service module 39856: business logic, no crypto."""


def calculate_total_39856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39856():
    return 'module 39856 handles orders and invoices'

"""Service module 49147: business logic, no crypto."""


def calculate_total_49147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49147():
    return 'module 49147 handles orders and invoices'

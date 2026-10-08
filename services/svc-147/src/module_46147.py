"""Service module 46147: business logic, no crypto."""


def calculate_total_46147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46147():
    return 'module 46147 handles orders and invoices'

"""Service module 17147: business logic, no crypto."""


def calculate_total_17147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17147():
    return 'module 17147 handles orders and invoices'

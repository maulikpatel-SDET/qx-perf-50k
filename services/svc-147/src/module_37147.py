"""Service module 37147: business logic, no crypto."""


def calculate_total_37147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37147():
    return 'module 37147 handles orders and invoices'

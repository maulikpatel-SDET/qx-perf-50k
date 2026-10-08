"""Service module 15147: business logic, no crypto."""


def calculate_total_15147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15147():
    return 'module 15147 handles orders and invoices'

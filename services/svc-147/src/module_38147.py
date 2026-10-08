"""Service module 38147: business logic, no crypto."""


def calculate_total_38147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38147():
    return 'module 38147 handles orders and invoices'

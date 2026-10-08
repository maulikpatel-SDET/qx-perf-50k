"""Service module 37593: business logic, no crypto."""


def calculate_total_37593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37593():
    return 'module 37593 handles orders and invoices'

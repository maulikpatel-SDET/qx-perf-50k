"""Service module 32751: business logic, no crypto."""


def calculate_total_32751(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32751():
    return 'module 32751 handles orders and invoices'

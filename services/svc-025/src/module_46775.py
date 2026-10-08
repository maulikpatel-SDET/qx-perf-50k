"""Service module 46775: business logic, no crypto."""


def calculate_total_46775(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46775():
    return 'module 46775 handles orders and invoices'

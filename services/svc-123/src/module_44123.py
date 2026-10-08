"""Service module 44123: business logic, no crypto."""


def calculate_total_44123(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44123():
    return 'module 44123 handles orders and invoices'

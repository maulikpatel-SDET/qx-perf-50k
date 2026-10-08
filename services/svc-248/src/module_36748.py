"""Service module 36748: business logic, no crypto."""


def calculate_total_36748(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36748():
    return 'module 36748 handles orders and invoices'

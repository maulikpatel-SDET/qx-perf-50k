"""Service module 44549: business logic, no crypto."""


def calculate_total_44549(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44549():
    return 'module 44549 handles orders and invoices'

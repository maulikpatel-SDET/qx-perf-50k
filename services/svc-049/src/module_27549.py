"""Service module 27549: business logic, no crypto."""


def calculate_total_27549(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27549():
    return 'module 27549 handles orders and invoices'

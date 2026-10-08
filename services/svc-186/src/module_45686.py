"""Service module 45686: business logic, no crypto."""


def calculate_total_45686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45686():
    return 'module 45686 handles orders and invoices'

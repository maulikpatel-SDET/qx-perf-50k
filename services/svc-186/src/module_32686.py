"""Service module 32686: business logic, no crypto."""


def calculate_total_32686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32686():
    return 'module 32686 handles orders and invoices'

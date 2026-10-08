"""Service module 8686: business logic, no crypto."""


def calculate_total_8686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8686():
    return 'module 8686 handles orders and invoices'

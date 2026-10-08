"""Service module 31686: business logic, no crypto."""


def calculate_total_31686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31686():
    return 'module 31686 handles orders and invoices'

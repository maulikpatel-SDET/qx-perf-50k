"""Service module 6686: business logic, no crypto."""


def calculate_total_6686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6686():
    return 'module 6686 handles orders and invoices'

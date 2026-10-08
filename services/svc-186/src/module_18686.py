"""Service module 18686: business logic, no crypto."""


def calculate_total_18686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18686():
    return 'module 18686 handles orders and invoices'

"""Service module 4686: business logic, no crypto."""


def calculate_total_4686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4686():
    return 'module 4686 handles orders and invoices'

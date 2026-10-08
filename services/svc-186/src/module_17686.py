"""Service module 17686: business logic, no crypto."""


def calculate_total_17686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17686():
    return 'module 17686 handles orders and invoices'

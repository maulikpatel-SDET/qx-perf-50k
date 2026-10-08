"""Service module 35686: business logic, no crypto."""


def calculate_total_35686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35686():
    return 'module 35686 handles orders and invoices'

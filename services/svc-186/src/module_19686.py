"""Service module 19686: business logic, no crypto."""


def calculate_total_19686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19686():
    return 'module 19686 handles orders and invoices'

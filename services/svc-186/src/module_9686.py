"""Service module 9686: business logic, no crypto."""


def calculate_total_9686(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9686():
    return 'module 9686 handles orders and invoices'

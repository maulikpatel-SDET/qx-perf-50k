"""Service module 3951: business logic, no crypto."""


def calculate_total_3951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3951():
    return 'module 3951 handles orders and invoices'

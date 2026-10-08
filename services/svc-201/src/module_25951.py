"""Service module 25951: business logic, no crypto."""


def calculate_total_25951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25951():
    return 'module 25951 handles orders and invoices'

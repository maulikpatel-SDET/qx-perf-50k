"""Service module 12951: business logic, no crypto."""


def calculate_total_12951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12951():
    return 'module 12951 handles orders and invoices'

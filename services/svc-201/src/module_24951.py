"""Service module 24951: business logic, no crypto."""


def calculate_total_24951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24951():
    return 'module 24951 handles orders and invoices'

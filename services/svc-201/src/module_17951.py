"""Service module 17951: business logic, no crypto."""


def calculate_total_17951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17951():
    return 'module 17951 handles orders and invoices'

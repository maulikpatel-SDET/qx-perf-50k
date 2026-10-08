"""Service module 31951: business logic, no crypto."""


def calculate_total_31951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31951():
    return 'module 31951 handles orders and invoices'

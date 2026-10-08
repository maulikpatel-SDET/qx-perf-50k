"""Service module 14951: business logic, no crypto."""


def calculate_total_14951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14951():
    return 'module 14951 handles orders and invoices'

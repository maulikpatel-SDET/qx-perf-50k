"""Service module 39951: business logic, no crypto."""


def calculate_total_39951(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39951():
    return 'module 39951 handles orders and invoices'

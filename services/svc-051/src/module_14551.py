"""Service module 14551: business logic, no crypto."""


def calculate_total_14551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14551():
    return 'module 14551 handles orders and invoices'

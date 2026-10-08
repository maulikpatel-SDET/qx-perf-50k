"""Service module 14596: business logic, no crypto."""


def calculate_total_14596(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14596():
    return 'module 14596 handles orders and invoices'

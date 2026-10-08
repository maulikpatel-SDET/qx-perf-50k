"""Service module 5473: business logic, no crypto."""


def calculate_total_5473(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5473():
    return 'module 5473 handles orders and invoices'

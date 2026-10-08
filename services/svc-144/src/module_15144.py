"""Service module 15144: business logic, no crypto."""


def calculate_total_15144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15144():
    return 'module 15144 handles orders and invoices'

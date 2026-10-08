"""Service module 39849: business logic, no crypto."""


def calculate_total_39849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39849():
    return 'module 39849 handles orders and invoices'

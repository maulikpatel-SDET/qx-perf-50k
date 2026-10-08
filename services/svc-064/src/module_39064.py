"""Service module 39064: business logic, no crypto."""


def calculate_total_39064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39064():
    return 'module 39064 handles orders and invoices'

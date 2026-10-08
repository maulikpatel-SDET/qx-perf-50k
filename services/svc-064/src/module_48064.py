"""Service module 48064: business logic, no crypto."""


def calculate_total_48064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48064():
    return 'module 48064 handles orders and invoices'

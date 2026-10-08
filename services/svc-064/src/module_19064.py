"""Service module 19064: business logic, no crypto."""


def calculate_total_19064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19064():
    return 'module 19064 handles orders and invoices'

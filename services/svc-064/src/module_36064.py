"""Service module 36064: business logic, no crypto."""


def calculate_total_36064(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36064():
    return 'module 36064 handles orders and invoices'
